import random
import tkinter
from tkinter import *
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


class SegmentationUtilsFrame(Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.variable = None
        self.create_widgets()

    def create_widgets(self):
        # sliders
        self.r_slider = Scale(self, from_=0, to=256, orient=HORIZONTAL)
        self.r_slider.grid(row=1)
        self.g_slider = Scale(self, from_=0, to=256, orient=HORIZONTAL)
        self.g_slider.grid(row=2)

        self.b_slider = Scale(self, from_=0, to=256, orient=HORIZONTAL)
        self.b_slider.grid(row=3)

        switch_frame = LabelFrame(self)
        switch_frame.grid(row=4)

        self.variable = StringVar(None, "AND")

        AND_button = Radiobutton(switch_frame, text="AND", variable=self.variable,
                                 indicatoron=False, value="AND", width=8)
        OR_button = Radiobutton(switch_frame, text="OR", variable=self.variable,
                                indicatoron=False, value="OR", width=8)

        AND_button.grid(row=0, column=0)
        OR_button.grid(row=0, column=1)


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
