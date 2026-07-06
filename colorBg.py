import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)


from tkinter import * 

def change():
    main.config(bg = changeColor.get())

main = Tk()
main.geometry("300x300")
main.title("Theme Changer")
main.config(bg = "red")

changeColor = StringVar(value="red")

label1 = Label(text = "Choose bg color" , width=20 , height=1 , bg = "white" , fg = "black" , font = ("Arial" , 10))
label1.place(x = 50 , y = 10)

radioRed = Radiobutton( text="Red", value="red" , variable=changeColor , command=change)
radioGreen = Radiobutton(text="Green" , value="green",variable=changeColor , command=change)
radioBlue = Radiobutton(text="Blue" , value="blue",variable=changeColor , command=change)

radioRed.place(x = 50, y = 50)
radioBlue.place(x = 50 , y  = 90)
radioGreen.place(x = 50 , y = 130)

main.mainloop()