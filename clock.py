import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

from tkinter import *

import datetime

def showtime():
    currentTime = datetime.datetime.now()
    x = currentTime.strftime("%I:%M:%S %p")
    timeLabel.config(text=x)
    timeLabel.after(1000 , showtime)

main_screen = Tk()
main_screen.title("clock")
main_screen.geometry("500x500")
main_screen.configure(bg="#5fb0dd")


mainLabel = Label(text="Digital Clock" , width = 20 , height =3 , bg = "#6ed278" , font= ("Arial" , 15) )
mainLabel.place(x = 100 , y = 100)

showTimeButton = Button(command= showtime , text= "Show Time" , width = 20 , height =2 , font = ("Times New Roman" , 10) , bg = "#db8143", fg = "black")
showTimeButton.place(x = 100, y = 200)

timeLabel = Label(width = 20 , height = 2 , bg = "#36f2da" , fg = "#920874", font = ("Arial" , 15))
timeLabel.place(x = 100 , y = 300)


main_screen.mainloop()
