from tkinter import *
from tkinter import ttk

from GUI.get_image_frame_seg import UploadFileSegFrame
from GUI.histogram_rgb_frame import HistogramRGBFrame
from GUI.segmentation_utils_frame import SegmentationUtilsFrame


class SegmentationFrame(ttk.Frame):
    def image_change_handler(self, image):
        print('image handler lauched')
        self.histogram = HistogramRGBFrame(
            self.body, image)
        self.histogram.grid(column=2)

    def __init__(self, root):
        super().__init__(root, width=800, height=400)

        self.histogram = None
        image = UploadFileSegFrame(self)
        image.grid(column=0)

        utils = SegmentationUtilsFrame(self)
        utils.grid(column=1)
