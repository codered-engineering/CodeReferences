import math
from planet import Direction 

class Odometry:
    def __init__(self, robot):
        self.robot = robot
        self.WHEEL_DISTANCE = 0.076
        self.DISTANCE_PER_TICK = 1/2150

    def calc_odometry(self, distances):
        gamma = self.robot.start_direction * math.pi / 180
        dx = self.robot.start_x
        dy = self.robot.start_y
        total_s = 0

        for dist in distances:
            dl = dist[0] * self.DISTANCE_PER_TICK
            dr = dist[1] * self.DISTANCE_PER_TICK
            alpha = (dr - dl) / self.WHEEL_DISTANCE
            beta = alpha /2

            if alpha == 0:
                s = dl
            else:
                s = ((dr + dl) / alpha) * math.sin(beta)

            dx -= math.sin(gamma + beta) * s 
            dy += math.cos(gamma + beta) * s

            gamma += alpha
            total_s += s

        #convert gamma to degree
        gamma = calc_direction(math.degrees(gamma) - 30)

        if self.robot.start_direction == 0 and gamma == 0:
            dy += 1
            gamma = 180
        elif self.robot.start_direction == 0 and gamma == 90:
            dy += 1
            gamma = 270
        elif self.robot.start_direction == 0 and gamma == 180:
            gamma = 0
        elif self.robot.start_direction == 0 and gamma == 270:
            dy += 1
            gamma = 90

        elif self.robot.start_direction == 90 and gamma == 0:
            dy -= 1
            gamma = 270
        elif self.robot.start_direction == 90 and gamma == 90:
            gamma = 0
        elif self.robot.start_direction == 90 and gamma == 180:
            dy += 1
            gamma = 90
        elif self.robot.start_direction == 90 and gamma == 270:
            gamma = 180

        elif self.robot.start_direction == 180 and gamma == 0:
            gamma = 180
        elif self.robot.start_direction == 180 and gamma == 90:
            dy -= 1
            gamma = 270
        elif self.robot.start_direction == 180 and gamma == 180:
            dy -= 1
            gamma = 0
        elif self.robot.start_direction == 180 and gamma == 270:
            dy -= 1
            gamma = 90

        elif self.robot.start_direction == 270 and gamma == 0:
            dy -= 1
            gamma = 90
        elif self.robot.start_direction == 270 and gamma == 90:
            gamma = 180
        elif self.robot.start_direction == 270 and gamma == 180:
            dy += 1
            gamma = 90
        elif self.robot.start_direction == 270 and gamma == 270:
            gamma = 90
                    
        #convert total_s to cm
        total_s = round(total_s * 100)  

        return round(dx), round(dy), gamma

def calc_direction(direction):
    #North 0, East 90, South 180, West 270
    direction %= 360
    if direction <= 45:
        return Direction.NORTH
    elif direction <= 135:
        return Direction.EAST
    elif direction <= 225:
        return Direction.SOUTH
    elif direction <= 315:
        return Direction.WEST
    else:
        return Direction.NORTH


        
