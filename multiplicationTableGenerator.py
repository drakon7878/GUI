import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

from tkinter import *

def setHeight():
    height = int(range1.get())
    table.config(height = height)


def generateTable():
    number = int(entry.get())
    selrange = int(range1.get()) + 1
    table.delete(0,END)
    for i in range(1 , selrange):
        result = str(number) + "x" + str(i) + "=" + str(number*i)
        table.insert(END , result)

main = Tk()
main.geometry("600x1080")
main.title("Multiplication Table Generator")
main.config(bg = "white")
range1 = IntVar()
labelTitle  = Label(text = "Multiplication Table Generator" , width = 30 , height = 2 , font = ("Arial" , 20) , bg = "white" , fg = "black" , relief="raised")
labelTitle.place(x = 20 , y = 20)

labelEnter = Label(text = "Enter a number" , width = 15 , height = 2 , font = ("Arial" , 15) , bg = "pink" ,fg = "black" , relief="sunken")
labelEnter.place(x = 20 , y = 120)

entry = Entry(width = 10 , font = ("Arial" , 15) , bg = "blue" , fg = "white")
entry.place(x = 270 , y = 120)

labelRange = Label(text = "Select your range" , width = 15 , height = 2 , font=("Arial" , 15) , bg = "#58abc6" , fg = "black")
labelRange.place(x = 30 , y = 200)

rd1 = Radiobutton(text = "10" , value = 10 , variable=range1 , bg = "pink" , fg = "black" , command = setHeight)
rd2 = Radiobutton(text = "20" , value = 20 , variable=range1 , bg = "red" , fg = "black" , command=setHeight)
rd3 = Radiobutton(text = "30" , value = 30 , variable=range1 , bg = "purple" , fg = "black" , command=setHeight)

rd1.place(x = 300 ,  y = 200)
rd2.place(x = 360,  y = 200)
rd3.place(x = 420 ,  y = 200)


generate = Button(text = "Generate Table" , width = 20 , height = 2 , fg = "black" , bg = "#3e5ea6" , command = generateTable ,  font = ("Arial" , 15) , relief="raised")
generate.place(x = 40 , y = 300)

table = Listbox(width = 40 , height = 10 , bg = "#85c791" , fg = "black")
table.place(x = 40 , y = 400)


main.mainloop()