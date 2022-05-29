import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Image Processor')

    canvas = tk.Canvas(root, width=800, height=400, bg='#3b3b3b')
    canvas.grid(rowspan=4)

    root.mainloop()
