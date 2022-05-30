from tkinter import *
from tkinter import ttk
import numpy as np
import random
import cv2


from GUI.get_image_frame import UploadFileFrame


def rand_helper(i):
    a = random.randint(0, 20)
    if a == 20:
        return 255
    elif a == 0:
        return 0
    else:
        return i


class OverviewFrame(ttk.Frame):
    def equalize(self):
        equ = cv2.equalizeHist(self.image.image)
        self.image.set_image(equ)

    def linear_transform(self):
        print('linear transformation ..')

    def apply_noise(self):

        flat_noisy_image = np.array([rand_helper(i)
                                    for i in self.image.image.flatten()])
        a = flat_noisy_image.reshape(self.image.image.shape)
        self.image.set_image(a)
        print('making noise ..')

    options = ['choose filter', 'median', 'moyenneur']

    def image_change_hanlder(self, image):
        print("yolo")

    def __init__(self, root):
        super().__init__(root, width=800, height=400)

        header = LabelFrame(self, font=('Raleway', 25),
                            width=800, height=100, bg='#585858')
        header.grid_propagate(False)
        header.grid(row=0)

        # contrast section
        contrast_frame = LabelFrame(
            header, borderwidth=0, bg='#585858', padx=10)
        contrast_frame.grid(row=0, column=0)

        contrast = Label(contrast_frame, text='Contrast',
                         fg='white', bg='#585858', pady=5)
        contrast.grid(row=0, sticky=W)

        equ_button = Button(contrast_frame, text='Equalize',
                            bg='#828282', fg='white', command=self.equalize, padx=20)
        equ_button.grid(row=1, pady=5, sticky=W)

        lin_button = Button(contrast_frame, text='linear transformation', bg='#828282', fg='white',
                            command=self.linear_transform)
        lin_button.grid(row=3)

        # filters section
        filters_frame = LabelFrame(
            header, borderwidth=0, bg='#585858', padx=50)
        filters_frame.grid(row=0, column=1)

        filters = Label(filters_frame, text='Filters',
                        fg='white', bg='#585858', pady=5)
        filters.grid(row=0, sticky=W)

        type_frame = LabelFrame(filters_frame, bg='#585858', borderwidth=0)
        type_frame.grid(row=1)

        type_text = Label(type_frame, text='Type:', fg='white', bg='#585858')
        type_text.grid(row=0, column=0)

        variable = StringVar(type_frame)
        variable.set(self.options[0])

        drop_down = OptionMenu(type_frame, variable, *self.options)
        drop_down.grid(row=0, column=1)

        dimension_frame = LabelFrame(filters_frame, borderwidth=0)
        dimension_frame.grid(row=2, pady=5, sticky=W)

        dimension_text = Label(
            dimension_frame, text='Dim:', fg='white', bg='#585858')
        dimension_text.grid(row=1, column=0)

        space = Label(dimension_frame, text='', fg='white', bg='#585858')
        space.grid(row=1, column=1)

        dimension = Entry(dimension_frame, width=10)
        dimension.grid(row=1, column=2)

        # noise section
        noise_frame = LabelFrame(header, borderwidth=0, bg='#585858')
        noise_frame.grid(row=0, column=3)

        noise = Label(noise_frame, text='Noise',
                      fg='white', bg='#585858', pady=5)
        noise.grid(row=0, sticky=W)

        noise_button = Button(noise_frame, text='Apply noise', bg='#828282', fg='white', command=self.apply_noise,
                              padx=20)
        noise_button.grid(row=1, sticky=W)

        body = LabelFrame(self, font=('Raleway', 25), width=800,
                          height=300, bg='#3b3b3b', borderwidth=0)
        body.grid_propagate(False)
        body.grid(row=2)

        self.image = UploadFileFrame(
            body, image_change_hanlder=self.image_change_hanlder)
        self.image.grid(row=0, column=0)
