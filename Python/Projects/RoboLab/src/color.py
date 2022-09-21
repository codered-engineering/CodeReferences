import time
import ev3dev.ev3 as ev3

class Color:
    def __init__(self):
        #Color Sensor
        self.cs = ev3.ColorSensor()
        self.cs.mode = "RGB-RAW"
        #Color Variables
        self.cal_color_value = 0
        self.current_color_value = 0
        self.current_color = ()
        self.cal_white = 0
        self.cal_black = 0
        self.cal_blue = 0
        self.cal_red = 0
        self.cal_blue_low = (0,0,0)
        self.cal_blue_high = (0,0,0)
        self.cal_red_low = (0,0,0)
        self.cal_red_high = (0,0,0)

    def calibrate_white(self):
        input("Press Enter to calibrate WHITE")
        print(self.cs.bin_data("hhh"))
        self.cal_white = self.cs.bin_data("hhh")

    def calibrate_black(self):
        input("Press Enter to calibrate BLACK")
        print(self.cs.bin_data("hhh"))
        self.cal_black = self.cs.bin_data("hhh")

    def calibrate_red(self):
        input("Press Enter to calibrate RED")
        print(self.cs.bin_data("hhh"))
        self.cal_red = self.cs.bin_data("hhh")

    def calibrate_blue(self):
        input("Press Enter to calibrate BLUE")
        print(self.cs.bin_data("hhh"))
        self.cal_blue = self.cs.bin_data("hhh")
    
    def calc_blue_and_red_range(self, offset):
        self.cal_blue_low = (self.cal_blue[0] - offset,
                             self.cal_blue[1] - offset,
                             self.cal_blue[2] - offset)
        self.cal_blue_high = (self.cal_blue[0] + offset,
                              self.cal_blue[1] + offset,
                              self.cal_blue[2] + offset)
        self.cal_red_low = (self.cal_red[0] - offset,
                            self.cal_red[1] - offset,
                            self.cal_red[2] - offset)
        self.cal_red_high = (self.cal_red[0] + offset,
                             self.cal_red[1] + offset,
                             self.cal_red[2] + offset)

    def calc_cal_color_value(self):
        cal_white_value = 0
        cal_black_value = 0

        i = 0
        while i < 3:
            cal_white_value += self.cal_white[i]
            cal_black_value += self.cal_black[i]
            i += 1
        self.cal_color_value = (cal_white_value + cal_black_value) / 2

    def calc_current_color_value(self):
        self.current_color = self.cs.bin_data("hhh")
        self.current_color_value = 0

        i = 0
        while i < 3:
            self.current_color_value += self.current_color[i]
            i += 1

    def color_calibration(self):
        offset = 40

        #calibrate the colors
        self.calibrate_white()
        self.calibrate_black()
        self.calibrate_blue()
        self.calibrate_red()

        #  Samples
        # self.cal_white = (240, 360, 224)
        # self.cal_black = (18, 33, 11)
        # self.cal_blue = (46, 153, 132)
        # self.cal_red = (181, 58, 29)

        self.calc_cal_color_value()
        self.calc_blue_and_red_range(offset)
        time.sleep(1)
        input("Press Enter to START")
