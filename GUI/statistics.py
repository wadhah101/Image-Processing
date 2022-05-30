from tkinter import *

import numpy as np


class StatisticsFrame(Frame):
    def get_image_average(self):
        return np.average(self.image)

    def get_standard_deviation(self):
        return np.std(self.image)

    def __init__(self, parent, image: np.ndarray):
        super().__init__(parent)

        footer = LabelFrame(self, font=('Raleway', 25), bg='#3b3b3b', borderwidth=0, width=1200,
                            height=100)
        footer.grid(column=0)

        right_stat = LabelFrame(footer)
        right_stat.grid(row=0, column=0, sticky=W)

        average = Label(right_stat, text='0.00')
        average.grid(row=0)

        std = Label(right_stat, text='0.00')
        std.grid(row=1)

        left_stat = LabelFrame(footer)
        left_stat.grid(row=0, column=1, sticky=E)

        resolution = Label(left_stat, text='000x000')
        resolution.grid(row=0)
