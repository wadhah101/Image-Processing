import random
import tkinter
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.messagebox import showinfo

import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure


class HistogramFrame(tk.Frame):

    def __init__(self, parent, image: np.ndarray):
        super().__init__(parent)
        self.image = image
        self.createWidgets()

    @staticmethod
    def get_histogram(image: np.ndarray):
        histogram = []
        flattened_image = image.flatten()
        for i in range(0, 256):
            histogram.append(np.count_nonzero(flattened_image == i))
        return np.array(histogram)

    def createWidgets(self):
        fig, (ax) = plt.subplots(1, 1)
        fig.set_size_inches(4, 2)
        histogram = self.get_histogram(self.image)
        ax.plot(range(256), histogram)
        canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=1)


# img = cv2.imread("../cat.jpg", cv2.IMREAD_GRAYSCALE)
#
# root = tk.Tk()
# hc = HistogramFrame(root, img)
# hc.pack(side="top")
#
# root.mainloop()
