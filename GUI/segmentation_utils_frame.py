from tkinter import *


class SegmentationUtilsFrame(Frame):
    def update_r_slider(self, event):
        print(int(self.r_slider.get()))

    def update_g_slider(self, event):
        print(int(self.g_slider.get()))

    def update_b_slider(self, event):
        print(int(self.b_slider.get()))

    def radio_checked(self):
        print(self.variable.get())

    def __init__(self, parent):
        super().__init__(parent)
        self.b_slider = None
        self.g_slider = None
        self.r_slider = None
        self.variable = None
        self.create_widgets()

    def create_widgets(self):
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
