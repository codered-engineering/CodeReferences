import math

def calc_odometry(wdist, dpt, start_x, start_y, start_direction, list):

        gamma = start_direction * math.pi / 180
        dx = start_x
        dy = start_y
        total_s = 0

        for value in list:
            dl = value[0] * dpt
            dr = value[1] * dpt
            alpha = (dr - dl) / wdist
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
        # gamma = (math.degrees(gamma) + 180) % 360
        gamma = math.degrees(gamma)-30
        #convert total_s to cm
        total_s = total_s
        
        return dx, dy + 1, gamma, total_s