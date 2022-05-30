import random
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


def extract_color_threshold(image: np.ndarray, threshold: int):
    return np.where(image >= threshold, 255, 0)


def image_seuil_and(image: np.ndarray, r, g, b):
    red_channel, green_channel, blue_channel = image[:,
                                                     :, 2],  image[:, :, 1], image[:, :, 0]
    image_seuil_red = extract_color_threshold(red_channel, r)
    image_seuil_green = extract_color_threshold(green_channel, g)
    image_seuil_blue = extract_color_threshold(blue_channel, b)
    result = np.bitwise_and(
        image_seuil_red, image_seuil_green, image_seuil_blue)
    return result.astype('uint8')


def image_seuil_or(image: np.ndarray, r, g, b):
    red_channel, green_channel, blue_channel = image[:,
                                                     :, 2],  image[:, :, 1], image[:, :, 0]
    image_seuil_red = extract_color_threshold(red_channel, r)
    image_seuil_green = extract_color_threshold(green_channel, g)
    image_seuil_blue = extract_color_threshold(blue_channel, b)
    result = np.bitwise_or(
        image_seuil_red, image_seuil_green, image_seuil_blue)
    return result.astype('uint8')


class SegmentationUtilsFrame(Frame):
    def update_r_slider(self, event):
        self.draw_binary_image(self.variable.get(), self.r_slider.get(),
                               self.g_slider.get(), self.b_slider.get())

    def update_g_slider(self, event):
        self.draw_binary_image(self.variable.get(), self.r_slider.get(),
                               self.g_slider.get(), self.b_slider.get())

    def update_b_slider(self, event):
        self.draw_binary_image(self.variable.get(), self.r_slider.get(),
                               self.g_slider.get(), self.b_slider.get())

    def radio_checked(self):
        self.draw_binary_image(self.variable.get(), self.r_slider.get(),
                               self.g_slider.get(), self.b_slider.get())

    def __init__(self, parent, image: np.ndarray):
        super().__init__(parent)
        self.b_slider = None
        self.g_slider = None
        self.r_slider = None
        self.variable = None
        self.image = image
        self.canvas = None
        self.transformed_image = None
        self.create_widgets()

    def init_plot(self):
        fig, (ax) = plt.subplots(1, 1)
        self.ax = ax
        fig.suptitle('Selected Image :')
        fig.set_size_inches(4, 3)
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('#3b3b3b')
        ax.spines['right'].set_color('#3b3b3b')
        ax.spines['left'].set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.title.set_color('white')
        fig.set_facecolor('#3b3b3b')
        canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
        canvas.draw()
        self.canvas = canvas
        canvas.get_tk_widget().grid(row=5, column=0, columnspan=1)

    def draw_binary_image(self, method: str,  r: int, g: int, b: int):

        self.transformed_image = image_seuil_and(
            self.image, r, g, b) if method == "AND" else image_seuil_or(self.image, r, g, b)

        self.ax.imshow(self.transformed_image, cmap='gray', vmin=0, vmax=255)
        self.canvas.draw()
        return

    def create_widgets(self):
        # otsu button
        otsu_button = Button(self, text='Otsu thresholds')
        otsu_button.grid(row=0)

        # sliders
        self.r_slider = Scale(self, from_=0, to=256, orient=HORIZONTAL)
        self.r_slider.grid(row=1)

        self.r_slider.bind("<ButtonRelease-1>", self.update_r_slider)

        self.g_slider = Scale(self, from_=0, to=256, orient=HORIZONTAL)
        self.g_slider.grid(row=2)

        self.g_slider.bind("<ButtonRelease-1>", self.update_g_slider)

        self.b_slider = Scale(self, from_=0, to=256, orient=HORIZONTAL)
        self.b_slider.grid(row=3)

        self.b_slider.bind("<ButtonRelease-1>", self.update_b_slider)

        switch_frame = LabelFrame(self)
        switch_frame.grid(row=4)
        self.init_plot()

        self.variable = StringVar(None, "AND")

        AND_button = Radiobutton(switch_frame, text="AND", variable=self.variable,
                                 indicatoron=False, value="AND", width=8, command=self.radio_checked)
        OR_button = Radiobutton(switch_frame, text="OR", variable=self.variable,
                                indicatoron=False, value="OR", width=8, command=self.radio_checked)

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
