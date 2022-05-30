from tkinter import *

import numpy as np


class StatisticsFrame(Frame):
    def get_image_average(self):
        return np.average(self.image)

    def get_standard_deviation(self):
        return np.std(self.image)

    def __init__(self, parent, image: np.ndarray):
        super().__init__(parent)
        self.image = image

        footer = LabelFrame(self, font=('Raleway', 25),
                            bg='#585858', borderwidth=0, width=600, height=100)
        footer.grid_propagate(False)
        footer.grid(row=3, column=0, sticky=W)

        right_stat = LabelFrame(footer, borderwidth=0, bg='#585858', padx=20)
        right_stat.grid(row=0, column=0, sticky=W)

        average = Label(
            right_stat, text=f"average = {self.get_image_average()}", bg='#585858', fg='white')
        average.grid(row=0, sticky=W)

        std = Label(right_stat, text=f"standard deviation = {self.get_standard_deviation()}", bg='#585858', fg='white')

        std.grid(row=1, sticky=W)

        left_stat = Frame(footer, bg='#585858')
        left_stat.grid(row=0, column=1)

        resolution = Label(left_stat, borderwidth=1, text=f"resolution {self.image.shape}", bg='#585858', fg='white', padx=100)
        resolution.grid(row=0)
