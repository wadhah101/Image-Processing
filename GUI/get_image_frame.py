import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


import tkinter as tk


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
            initialdir='/',
            filetypes=self.filetypes)
        print(self.filename)


# root = tk.Tk()
# hc = UploadFileFrame(root)
# hc.pack(side="top")

# root.mainloop()
