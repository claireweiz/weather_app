from tkinter import Tk, Frame, Label
from PIL import Image, ImageTk

root = Tk()

global_frame = Frame(root, border=10)
global_frame.grid()

img = Image.open("/Users/claire/coding/weatherapp/icon/logo.png")
img_tk = ImageTk.PhotoImage(img)

Label(global_frame, image=img_tk).pack()
Label(global_frame, text="I am a label").pack()

root.mainloop()