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
        self.button_neg.pack(side=RIGHT, padx=5, pady=5)

        self.button_dark = Button(self.btn_oper_frame, text="Ztmavit", fg="black", command=self.Darken)
        self.button_dark.pack(side=RIGHT, padx=5, pady=5)

        self.button_bright = Button(self.btn_oper_frame, text="Zesvětlit", fg="black", command=self.Brighten)
        self.button_bright.pack(side=RIGHT, padx=5, pady=5)

        self.button_gray = Button(self.btn_oper_frame, text="Odstíny šedi", fg="black", command=self.GrayScale)
        self.button_gray.pack(side=RIGHT, padx=5, pady=5)

        self.button_rot = Button(self.btn_oper_frame, text="Otočit", fg="black", command=self.Rotate)
        self.button_rot.pack(side=RIGHT, padx=5, pady=5)

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
        self.Update()

    def Darken(self):
        self.modified = self.modified*0.6
        self.modified = np.ceil(self.modified)
        self.Update()

    def Brighten(self):
        shape = self.modified.shape
        self.modified = self.modified.flatten()
        self.modified = self.modified * 1.6
        self.modified = np.clip(self.modified, 1, 255)
        self.modified.shape = shape
        self.Update()

    def Rotate(self):
        self.modified = np.rot90(self.modified, 1)
        self.Update()

    def GrayScale(self):
        r, g, b = self.modified[:, :, 0], self.modified[:, :, 1], self.modified[:, :, 2]
        self.modified = 0.2989 * r + 0.5870 * g + 0.1140 * b
        self.Update()

    def Update(self):
        im = Image.fromarray(self.modified.astype("uint8"))
        photo = ImageTk.PhotoImage(im)
        self.parent.geometry(str(self.modified.shape[1])+"x"+str(self.modified.shape[0]+150)+"+500+100")
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