import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

from tkinter import *

import datetime

def showdate():
    currentdate = datetime.datetime.now()
    if currentdate.strftime("%d") == "1" or currentdate.strftime("%d") == "21" or currentdate.strftime("%d") == "31":
        x = currentdate.strftime("%A, the %dst of %B, %Y")
    elif currentdate.strftime("%d") == "2" or currentdate.strftime("%d") == "22":
        x = currentdate.strftime("%A, the %dnd of %B, %Y")
    elif currentdate.strftime("%d") == "3" or currentdate.strftime("%d") == "23":
        x = currentdate.strftime("%A, the %drd of %B, %Y")
    else:
        x = currentdate.strftime("%A, the %dth of %B, %Y")

    mainLabel.configure(text=x)
    main_screen.after(1000 , showdate)

main_screen = Tk()
main_screen.title("clock")
main_screen.geometry("400x60")
main_screen.configure(bg="#ffcf61")


mainLabel = Label(text="" , width = 23 , height =2 , bg = "#ffcf61" , fg = "white" , font= ("Arial" , 15) )
mainLabel.place(x = 30 , y = 0)

showdate()

main_screen.mainloop()