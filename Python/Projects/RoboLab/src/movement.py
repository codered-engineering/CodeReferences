import ev3dev.ev3 as ev3
import time
import math

from odometry import Odometry, calc_direction
from communication import Communication
from planet import Direction
from color import Color
from node import Node

class Movement:
    def __init__(self, robot, com, color, planet):
        self.robot = robot
        self.com = com
        self.color = color
        self.planet = planet
        self.node = Node(self, self.com, self.robot, self.color, self.planet)
        self.od = Odometry(robot)
        #Large Motors
        self.motor_left = ev3.LargeMotor("outA")
        self.motor_left.reset()
        self.motor_left.stop_action = "brake"
        self.motor_right = ev3.LargeMotor("outC")
        self.motor_right.reset()
        self.motor_right.stop_action = "brake"
        #Ultrasonic Sensor
        self.us = ev3.UltrasonicSensor()
        self.us.mode = 'US-DIST-CM'
        self.find_obstacle = False
        #follow_line() variables
        self.LF_VELOCITY_MAX = 100
        self.KP = 12
        self.KD = 4.5   
        self.LF_OFFSET = 45
        self.LF_VELOCITY = 45
        self.last_error = 0
        self.derivative = 0
        self.distances = [] 
        #visited nodes
        self.visited = []  
    
    def move_straight_mm(self, mm, speed=200):
        wheel_diameter = 30
        wheel_circumference = wheel_diameter * math.pi
        # set speed
        self.motor_left.speed_sp = speed
        self.motor_right.speed_sp = speed

        # speed is in tacho counts pro second (tcps)
        # moving_time = number of wheel revolutions / revolutions pro second (rps)
        moving_time = (mm / wheel_circumference) / (speed / self.motor_left.count_per_rot)

        # start
        self.motor_left.command = "run-forever"
        self.motor_right.command = "run-forever"

        time.sleep(moving_time)

        # stop
        self.motor_left.stop()
        self.motor_right.stop()

    def rotate_to_deg(self, degree):
        rot_wheel_distance = 76
        degree %= 360 # positive remainder 0 <= degree < 360
        # force degree into range -180 < degree <= 180
        if degree > 180:
            degree -= 360

        # (pi * wheelbase) / 360 degrees
        way_length = ((math.pi * rot_wheel_distance) / 360) * abs(degree)

        if degree < 0:
            self.motor_left.polarity = "inversed"
        else:
            self.motor_right.polarity = "inversed"
        self.move_straight_mm(way_length)
        self.motor_left.polarity = "normal"
        self.motor_right.polarity = "normal"

    def rotate_to_pos(self, direction: Direction):
        degree = direction - self.robot.current_orientation

        self.rotate_to_deg(degree)
        self.robot.current_orientation = direction

    def engine_off(self, t = 0):
        self.motor_left.stop_action = "brake"
        self.motor_right.stop_action = "brake"
        self.motor_left.stop()
        self.motor_right.stop()
        time.sleep(t)
    
    def reset_motors(self):
        self.motor_left.reset()
        self.motor_right.reset()

    def reset_motors_position(self):
        self.motor_left.position = 0
        self.motor_right.position = 0

    def insert_motors_position(self):
        self.distances.append((self.motor_left.position, self.motor_right.position))

    def obstacle_check(self):
        if self.us.distance_centimeters < 10:
            self.find_obstacle = True
            self.engine_off()
            ev3.Sound.beep()

            # change end variables
            self.robot.end_x = self.robot.start_x
            self.robot.end_y = self.robot.start_y
            self.robot.end_direction = self.robot.start_direction
            self.robot.path_status = "blocked"
            self.robot.current_orientation = (self.robot.end_direction + 180) % 360

            #communication
            self.com.send_path()

            # turn around
            self.rotate_to_deg(190)

    def follow_line(self):
        self.obstacle_check()
        self.reset_motors_position()
        self.color.calc_current_color_value()
        error = (self.color.cal_color_value - self.color.current_color_value)/2 - self.LF_OFFSET
        derivative = error - self.last_error
        Turn = (self.KP * error + self.KD * derivative)/100
        #duty_cycle_sp = [-100, 100] percent
        if self.LF_VELOCITY + Turn > self.LF_VELOCITY_MAX: #Turn is positive
            Turn = self.LF_VELOCITY_MAX - self.LF_VELOCITY
        elif self.LF_VELOCITY - Turn < -self.LF_VELOCITY_MAX:
            Turn = self.LF_VELOCITY_MAX + self.LF_VELOCITY
        elif self.LF_VELOCITY - Turn > self.LF_VELOCITY_MAX: #Turn is negative
            Turn = -1 * (self.LF_VELOCITY_MAX - self.LF_VELOCITY)
        elif self.LF_VELOCITY + Turn < -self.LF_VELOCITY_MAX:
            Turn = -1 * (self.LF_VELOCITY_MAX + self.LF_VELOCITY)
        self.motor_left.duty_cycle_sp = self.LF_VELOCITY + Turn
        self.motor_right.duty_cycle_sp = self.LF_VELOCITY - Turn
        self.motor_left.command = "run-direct"
        self.motor_right.command = "run-direct"
        self.last_error = error
        #odometry: fill self.distances[]
        self.insert_motors_position()

    def go_to_target(self):
        self.robot.shortest_path = self.planet.shortest_path((self.robot.end_x, self.robot.end_y), (self.robot.target_x, self.robot.target_y))
        if self.robot.shortest_path is not None:
            i = 0
            while i < len(self.robot.shortest_path):
                self.go_to(self.robot.shortest_path[i])  
                i += 1
            if (self.robot.end_x, self.robot.end_y) == (self.robot.target_x, self.robot.target_y):
                self.com.send_target_reached()
                self.robot.queue = []
                self.robot.target_reached = True

    def explore(self):
        
        while self.robot.queue:
            #checking if a target is selected
            if self.robot.target_x is not None and self.robot.target_y is not None:
                self.go_to_target()
                if not self.robot.queue:
                    continue

            # checking if path is already explored
            if self.robot.queue[0][0] in self.planet.get_paths():
                if self.robot.queue[0][1] in self.planet.get_paths()[self.robot.queue[0][0]]:
                    self.robot.queue.pop(0)
                    continue 
                
            # checking for shortest path
            self.robot.shortest_path = []
            if self.robot.queue[0][0] != (self.robot.end_x, self.robot.end_y):
                #creating [queue + unvisited] - list
                nearest_nodes = []
                for (node, direction) in self.robot.queue:
                    nearest_nodes.append(node)
                for node in list(self.planet.get_paths()):
                    if node not in self.visited:
                        nearest_nodes.append(node)

                # find nearest node
                sp_weight_list = []
                for node in nearest_nodes:
                    tmp_sp = self.planet.shortest_path((self.robot.end_x,self.robot.end_y), node)
                    # calc path weight
                    path_weight = 0
                    if tmp_sp:
                        for (node, direction) in tmp_sp:
                            for dir, (_, _, weight) in self.planet.get_paths()[node].items():
                                if dir == direction:
                                    path_weight += weight
                        sp_weight_list.append((tmp_sp, path_weight))

                if sp_weight_list:
                    self.robot.shortest_path = min(sp_weight_list, key = lambda t: t[1])[0]
                    
                if self.robot.shortest_path:
                    i = 0
                    while i < len(self.robot.shortest_path):
                        self.go_to(self.robot.shortest_path[i])  
                        i += 1
                else:
                    # path is blocked
                    self.robot.queue.pop(0)
            else:
                self.go_to(self.robot.queue.pop(0))


    def go_to(self, path):
            # transfer selected path to robot and mothership
            self.robot.start_x = path[0][0]
            self.robot.start_y = path[0][1]
            self.robot.start_direction = path[1]
            self.com.send_path_select(path[0][0], path[0][1], path[1])

            # handle force messages
            if path[1] != self.robot.start_direction:
                if self.robot.start_direction in self.planet.get_paths()[(self.robot.start_x, self.robot.start_y)] and self.planet.get_paths()[(self.robot.start_x, self.robot.start_y)][self.robot.start_direction][2] == -1 and (self.robot.start_x, self.robot.start_y) != (self.robot.end_x, self.robot.end_y):
                        ev3.Sound.beep()
                        self.robot.queue.insert(0, path)
                        #send path status
                        self.robot.end_direction = self.robot.start_direction
                        self.robot.path_status = "blocked"
                        self.com.send_path() 
                        self.robot.end_x = self.robot.start_x
                        self.robot.end_y = self.robot.start_y
                        return

                elif self.robot.shortest_path:
                    self.robot.shortest_path = []
                else:
                    self.robot.queue.insert(0, path)
            path = ((self.robot.start_x, self.robot.start_y), self.robot.start_direction)

            # turn in the correct start direction 
            self.rotate_to_pos(self.robot.start_direction)
            self.rotate_to_deg(10)

            # follow the line until you spot a node
            while not self.node.find_node:
                self.follow_line()
                self.node.spot()
 
            # reset node.spot()
            self.node.find_node = False

            # if path is free -> no obstacle detected
            if not self.find_obstacle:
                self.robot.end_x, self.robot.end_y, self.robot.end_direction  = self.od.calc_odometry(self.distances)
                self.robot.path_status = "free"
                self.com.send_path()  
                self.robot.current_orientation = (self.robot.end_direction + 180) % 360

            #reset check_obstacle()
            self.find_obstacle = False

            # checking if spotted node were visited already
            if (self.robot.end_x, self.robot.end_y) not in self.visited:
                self.visited.append((self.robot.end_x, self.robot.end_y))
                self.node.scan()
                time.sleep(1)            
            else:
                self.move_straight_mm(70)
            
    def go_to_first_node(self):
        # move until you spot the first node
        while self.node.find_node == False:
            self.follow_line()
            self.node.spot()

        self.node.first()
        self.node.scan()

        #reset node.spot()
        self.node.find_node = False
