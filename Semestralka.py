import tkinter
from PIL import ImageTk
from PIL import Image
import numpy as np


img = Image.open( "kvetina.jpg" )
try:
    data = np.asarray( img, dtype='uint8' )
except SystemError:
    data = np.asarray( img.getdata(), dtype='uint8' )
data.setflags(write=1)

width = data.shape[1]
height = data.shape[0]
root = tkinter.Tk()
root.title("Editor")
root.geometry(str(width)+"x"+str(height + 50)+"+600+300")
root.resizable(width=False, height = False)


photo = Image.fromarray(data.astype('uint8'))
imgTK = ImageTk.PhotoImage(photo)
canvas = tkinter.Canvas(root, width = width, height = height)
image = canvas.create_image((width,height),image=imgTK, anchor=tkinter.SE)
canvas.pack()


root.mainloop()