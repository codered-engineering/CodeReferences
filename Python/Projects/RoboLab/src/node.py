import time

from communication import Communication
from odometry import Odometry, calc_direction

class Node():
    def __init__(self, movement, communication, robot, color, planet):
        self.move = movement
        self.com = communication
        self.robot = robot
        self.color = color
        self.od = Odometry(robot)
        self.planet = planet
        #spot variables
        self.find_node = False
        #scan variables
        self.SCAN_VELOCITY = 350
        self.SCAN_POS_LEFT = 400
        self.SCAN_POS_RIGHT = 350
        self.SCAN_POS_MID = 200
        self.SECOND_SCAN_POS = 100
        self.SCAN_TIME = 2
        self.COLOR_THRESHOLD = 650
    
    def first(self):
        self.com.send_ready()
        self.robot.current_orientation = self.robot.start_direction    
        self.robot.end_direction = (self.robot.start_direction + 180) % 360
        self.move.visited.append((self.robot.start_x, self.robot.start_y))

    def spot(self):
        count_blue = 0
        count_red = 0
        i = 0
        while i < 3:
            if self.color.current_color[i] in range(self.color.cal_blue_low[i], self.color.cal_blue_high[i]):
                count_blue += 1
            if self.color.current_color[i] in range(self.color.cal_red_low[i], self.color.cal_red_high[i]):
                count_red += 1
            i += 1
        if count_blue == 3 or count_red == 3:
            self.move.engine_off()
            self.move.reset_motors()
            self.find_node = True
            self.move.reset_motors_position()
        
    def calc_new_path_direction(self):
        self.direction_path_left = calc_direction(self.robot.end_direction + 90)
        self.direction_path_right = calc_direction(self.robot.end_direction + 270)
        self.direction_path_mid = calc_direction(self.robot.end_direction + 180)

    def scan(self):
        distance_mm = 70
       
        #positioning
        self.move.reset_motors()
        self.move.distances = []
        self.move.move_straight_mm(distance_mm)
        self.move.insert_motors_position()

        #scanning process
        self.calc_new_path_direction()
        self.scanning()
        
    def spot_path(self):
        self.color.calc_current_color_value()
        if int(self.color.current_color_value) < self.COLOR_THRESHOLD:
            return True
        return False

    def scanning(self):
        right = True
        left = True
        mid = True
        i = 0

        self.move.rotate_to_deg(120)
        while i < 18:
            if self.spot_path() and i < 6 and right:
                self.insert_to_queue(self.direction_path_right)
                right = False
            elif self.spot_path() and i >= 6 and i < 12 and mid:
                self.insert_to_queue(self.direction_path_mid)
                mid = False
            elif self.spot_path() and i >= 12 and left:
                self.insert_to_queue(self.direction_path_left)
                left = False
            self.move.rotate_to_deg(-15)
            i += 1
        self.move.rotate_to_deg(120)

    def insert_to_queue(self, direction):
        insert = True
        if (self.robot.end_x, self.robot.end_y) in self.planet.get_paths():
            if direction in self.planet.get_paths()[(self.robot.end_x, self.robot.end_y)]:
                insert = False
        if insert:
            self.robot.queue.insert(0, ((self.robot.end_x, self.robot.end_y), direction))
