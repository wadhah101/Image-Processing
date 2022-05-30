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
                            bg='#3b3b3b', borderwidth=0)
        footer.grid(column=0)

        right_stat = LabelFrame(footer)
        right_stat.grid(row=0, column=0, sticky=W)

        average = Label(
            right_stat, text=f"average = {self.get_image_average()}")
        average.grid(row=0)

        std = Label(right_stat, text=f"std = {self.get_standard_deviation()}")

        std.grid(row=1)

        left_stat = LabelFrame(footer)
        left_stat.grid(row=0, column=1, sticky=E)

        resolution = Label(left_stat, text=f"resolution {self.image.shape}")
        resolution.grid(row=0)
