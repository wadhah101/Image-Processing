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

from tp1 import rand_helper


class UploadFileFrame(tk.Frame):

    filetypes = (
        ('jpgs', '*.jpg'),
        ('pngs', '*.pngs'),
    )

    def __init__(self, parent, image_change_hanlder):
        super().__init__(parent)
        self.createWidgets()
        self.filename = ""
        self.image_change_hanlder = image_change_hanlder

    def createWidgets(self):
        self.uploadFileButton = tk.Button(
            self, text='Upload Image', command=self.uploadFileCommand)

        self.uploadFileButton.grid(row=1, column=1)

    def uploadFileCommand(self):
        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='~',
            filetypes=self.filetypes)
        image = cv2.imread(self.filename, cv2.IMREAD_GRAYSCALE)
        self.set_image(image)

    def set_image(self, newimg: np.ndarray):
        self.image = newimg
        self.image_change_hanlder(newimg)
        print("drawing new image")
        fig, (ax) = plt.subplots(1, 1)
        fig.suptitle('Selected Image :')
        fig.set_size_inches(4, 2.4)
        ax.imshow(newimg, cmap='gray', vmin=0, vmax=255)
        canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=1)

    def linear_transform(self):
        img = self.image
        lin_img = (img - img.min()) / (img.max() - img.min())
        lin_img = lin_img * 255
        self.set_image(lin_img)

    def equalize(self):
        equ = cv2.equalizeHist(self.image)
        self.set_image(equ)

    def apply_noise(self):
        flat_noisy_image = np.array([rand_helper(i)
                                    for i in self.image.image.flatten()])
        a = flat_noisy_image.reshape(self.image.image.shape)
        self.set_image(a)

    def mean_filter(self, w=1):
        image = self.image
        filtered = image.copy()
        for i in range(w, image.shape[0]-w):
            for j in range(w, image.shape[1]-w):
                block = image[i-w:i+w+1, j-w:j+w+1]
                mean_result = np.mean(block, dtype=np.float32)
                filtered[i][j] = int(mean_result)
        self.set_image(filtered)

    def median_filter(self, w=1):
        image = self.image
        filtered = image.copy()
        for i in range(w, image.shape[0]-w):
            for j in range(w, image.shape[1]-w):
                block: np.ndarray = image[i-w:i+w+1, j-w:j+w+1]
                flat_sorted_block = np.sort(block.flatten())
                median_value = flat_sorted_block[4]
                filtered[i][j] = int(median_value)
        self.set_image(filtered)


# root = tk.Tk()
# hc = UploadFileFrame(root)
# hc.pack(side="top")
#
# root.mainloop()
