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


class SegmentationUtilsFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # sliders
        self.r_slider = tk.Scale(self, from_=0, to=256, orient=tk.HORIZONTAL)
        self.r_slider.grid(row=1)
        self.g_slider = tk.Scale(self, from_=0, to=256, orient=tk.HORIZONTAL)
        self.g_slider.grid(row=2)

        self.b_slider = tk.Scale(self, from_=0, to=256, orient=tk.HORIZONTAL)
        self.b_slider.grid(row=3)

        # def uploadFileCommand(self):
        #     self.filename = fd.askopenfilename(
        #         title='Open a file',
        #         initialdir='~',
        #         filetypes=self.filetypes)
        #     self.show_image()

        # def show_image(self):
        #     self.image = cv2.imread(self.filename)[:, :, ::-1]
        #     fig, (ax) = plt.subplots(1, 1)
        #     fig.suptitle('Selected Image :')
        #     fig.set_size_inches(5, 5)
        #     ax.imshow(self.image)
        #     canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
        #     canvas.draw()
        #     canvas.get_tk_widget().grid(row=2, column=1)


# root = tk.Tk()
# hc = SegmentationUtilsFrame(root)
# hc.pack(side="top")
#
# root.mainloop()
