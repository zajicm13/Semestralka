import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import showerror
from PIL import ImageTk
from PIL import Image
import numpy as np



class Editor(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.start()
    def start(self):
        self.parent.title("Editor")
        self.parent.geometry("+500+100")

        self.pack()
        self.img_frame = tk.Label(self, border = 25)
        self.img_frame.pack(fill=BOTH, expand=1)
        self.OpenImage()
        self.btn_frame = Frame(self.parent)
        self.btn_frame.pack(fill=BOTH, expand=1)
        self.btn_oper_frame = Frame(self.parent)
        self.btn_oper_frame.pack(fill=BOTH, expand=1)
        self.button_close = Button(
            self.btn_frame, text="ZAVŘÍT", fg="red", command=self.btn_frame.quit
        )
        self.button_close.pack(side=LEFT, padx=5, pady=5)
        self.button_load = Button(self.btn_frame, text="Otevřít", fg="blue", command=self.OpenImage)
        self.button_load.pack(side=RIGHT, padx=5, pady=5)

        self.button_save = Button(self.btn_frame, text="Uložit", fg="green", command=self.SaveImage)
        self.button_save.pack(side=RIGHT, padx=5, pady=5)

        self.button_orig=Button(self.btn_frame, text="Původní obrázek", fg="purple", command=self.Original)
        self.button_orig.pack(side=LEFT, padx=5, pady=5)

        self.button_neg = Button(self.btn_oper_frame, text="Negativ", fg="black", command=self.Negative)
        self.button_neg.pack(side=TOP, padx=5, pady=5)

    def OpenImage(self):
        filepath = askopenfilename(filetypes=([("Image files", "*.jpg;*.png;*.ppm")]))
        self.filename = filepath
        self.LoadImage()
    def LoadImage(self):
        self.img = Image.open(self.filename)
        self.data = np.asarray(self.img)
        self.modified = self.data
        width, height = self.img.size
        size = str(width) + "x" + str(height+150) + "+500+100"
        self.parent.geometry(size)
        photo = ImageTk.PhotoImage(self.img)
        self.img_frame.configure(image=photo)
        self.img_frame.image = photo
    def Negative(self):

        self.modified = 255-self.modified
        im = Image.fromarray(self.modified.astype("uint8"))
        photo = ImageTk.PhotoImage(im)
        self.img_frame.configure(image=photo)
        self.img_frame.image = photo

    def Original(self):
        self.modified = self.data
        im = Image.fromarray(self.data.astype("uint8"))
        photo = ImageTk.PhotoImage(im)
        self.img_frame.configure(image=photo)
        self.img_frame.image = photo

    def SaveImage(self):
        im = Image.fromarray(self.modified.astype("uint8"))
        filepath = asksaveasfilename(filetypes=([("Image files", "*.jpg;*.png;*.ppm")]))
        im.save(filepath + ".jpg")
root = tk.Tk()
Editor(root)

root.mainloop()