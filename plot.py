import random
import tkinter

import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure

img = cv2.imread("./cat.jpg", cv2.IMREAD_GRAYSCALE)


# Implement the default Matplotlib key bindings.

def get_histogram(image: np.ndarray):
    histogram = []
    flattened_image = image.flatten()
    for i in range(0, 256):
        histogram.append(np.count_nonzero(flattened_image == i))
    return np.array(histogram)


histogram = get_histogram(img)

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Horizontally stacked subplots')
ax1.imshow(img, cmap='gray', vmin=0, vmax=255)
ax2.plot(range(256), histogram)
ax2.set(xlabel='niveau de gris', title="histogram")


canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


# button = tkinter.Button(master=root, text="Quit", command=_quit)
# button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
