import matplotlib.pyplot as plt

from random import randrange
from calc_odometry import calc_odometry

class Od():
    def __init__(self) -> None:
        pass

    def calibrate_odometry(self, list):
        #plot variables
        self.wdist_values = []
        self.calc_values_wdist = []
        self.dpt_values = []
        self.calc_values_dpt = []

        end_plot_wdist = []
        end_plot_dpt = []

        values = []
        self.calc_end_x = []
        self.calc_end_y = []
        self.calc_gamma = []
        self.calc_tot_s = []
        
        # referenz werte plot
        self.end_x_plot = []
        self.end_y_plot = []
        self.gamma_plot = []
        self.tot_s_plot = []

        # adjustable parameters 
        self.wdist = 0.076
        self.dpt_div = 2150
        self.dpt = 1/self.dpt_div

        # start variables
        start_x = -1
        start_y = -2
        start_direction = 0

        # end variables - SETPOINTS
        end_x = -1
        end_y = -1
        end_direction = 0
        end_s = 0.5
        
        #range values
        self.range_start = 1
        self.range_end = 101
        self.cal_value = 1

        for i in range(self.range_start, self.range_end):
            # Wheel distance 
            self.wdist_values.append(self.wdist * i)
            end_plot_wdist.append(end_x)

            values.append(calc_odometry(self.wdist * i, self.dpt, start_x, start_y, start_direction, list))

        for calcs in values:
            self.calc_end_x.append(calcs[0])
            self.calc_end_y.append(calcs[1])
            self.calc_gamma.append(calcs[2])
            self.calc_tot_s.append(calcs[3])
            self.calc_end_values(end_x, end_y, end_direction, end_s)

        print(values[0])
        self.plot_odometry()

    def plot_odometry(self):
        fig, axs = plt.subplots(2,2)
        fig.suptitle(f'Wheel Distance: {self.wdist}, Distance per Tick: 1/{self.dpt_div}\n [{self.calc_end_x[0]}, {self.calc_end_y[0]},\n {self.calc_gamma[0]}, {self.calc_tot_s[0]}]')

        axs[0,0].plot(self.wdist_values, self.end_x_plot, 'r-', self.wdist_values, self.calc_end_x, 'g-', linewidth=1)
        axs[0,0].set(xlabel='Wheel distance', ylabel='end_x')

        axs[1,0].plot(self.wdist_values, self.end_y_plot, 'r-', self.wdist_values, self.calc_end_y, 'g-', linewidth=1)
        axs[1,0].set(xlabel='Wheel distance', ylabel='end_y')

        axs[0, 1].plot(self.wdist_values, self.gamma_plot, 'r-', self.wdist_values, self.calc_gamma, 'g-', linewidth=1)
        axs[0, 1].set(xlabel='Wheel distance', ylabel='gamma')

        axs[1,1].plot(self.wdist_values, self.tot_s_plot, 'r-', self.wdist_values, self.calc_tot_s, 'g-', linewidth=1)
        axs[1,1].set(xlabel='Wheel distance', ylabel='total_s')
        # plt.axis([self.range_start/self.cal_value, self.range_end/self.cal_value, setpoint-1, setpoint+1])
        plt.show()

    def calc_end_values(self, end_x, end_y, end_direction, tot_s):
        self.end_x_plot.append(end_x)
        self.end_y_plot.append(end_y)
        self.gamma_plot.append(end_direction)
        self.tot_s_plot.append(tot_s)


def main():
    list = [(265, 263), (15, -36), (2, 2), (6, 12), (6, 15), (7, 14), (7, 18), (7, 16), (13, 29), (9, 22), (10, 23), (24, 35), (25, 21), (17, 12), (19, 11), (23, 17), (24, 27), (18, 22), (22, 22), (42, 31), (25, 23), (18, 19), (17, 27), (20, 26), (14, 12), (16, 12), (18, 15), (18, 16), (14, 15), (12, 16), (16, 18), (13, 13), (12, 11), (20, 17), (17, 15), (20, 23), (14, 18), (13, 15), (12, 11), (16, 13), (16, 13), (13, 14), (14, 13), (13, 15), (17, 16), (15, 13), (13, 13), (15, 13), (13, 14), (14, 15), (15, 14), (11, 11), (19, 19), (20, 18), (16, 15), (18, 16), (18, 21), (12, 12), (13, 15), (12, 14), (18, 20), (14, 17), (16, 16), (16, 14), (13, 12), (16, 14), (14, 13), (16, 16), (22, 25), (20, 20), (19, 19), (14, 14), (13, 12), (15, 15), (14, 14), (24, 21), (14, 17), (11, 14), (35, 35), (37, 37), (31, 28)]
    od = Od()
    od.calibrate_odometry(list)

main()






