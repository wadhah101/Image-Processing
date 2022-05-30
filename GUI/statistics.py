from tkinter import *

import numpy as np


class StatisticsFrame(Frame):
    def __init__(self, parent, image: np.ndarray):
        super().__init__(parent)

        footer = LabelFrame(self, font=('Raleway', 25), width=1200,
                            height=100, bg='#3b3b3b', borderwidth=0)
        footer.grid(column=0)




