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


class UploadFileFrame(tk.Frame):

    filetypes = (
        ('jpgs', '*.jpg'),
        ('pngs', '*.pngs'),
    )

    def __init__(self, parent):
        super().__init__(parent)
        self.createWidgets()
        self.filename = ""

    def createWidgets(self):
        self.uploadFileButton = tk.Button(
            self, text='Upload Image', command=self.uploadFileCommand)

        self.uploadFileButton.grid(row=1, column=1)

    def uploadFileCommand(self):
        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='~',
            filetypes=self.filetypes)
        self.show_image()

    def show_image(self):
        self.image = cv2.imread(self.filename, cv2.IMREAD_GRAYSCALE)
        fig, (ax) = plt.subplots(1, 1)
        fig.suptitle('Selected Image :')
        fig.set_size_inches(4, 2.4)
        ax.imshow(self.image, cmap='gray', vmin=0, vmax=255)
        canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=1)

    def set_image(self, newimg: np.ndarray):
        self.image = newimg
        print("drawing new image")
        fig, (ax) = plt.subplots(1, 1)
        fig.suptitle('Selected Image :')
        fig.set_size_inches(4, 2.4)
        ax.imshow(newimg, cmap='gray', vmin=0, vmax=255)
        canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=1)


# root = tk.Tk()
# hc = UploadFileFrame(root)
# hc.pack(side="top")
#
# root.mainloop()
