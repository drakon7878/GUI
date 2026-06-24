import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

from tkinter import *
import random
from tkinter import messagebox

attempts = 0
actualNumber = random.randint(1 , 20)

def guessTheNumber():
    global attempts , actualNumber
    try:
        guessNumber = int(guessEntry.get())
    except ValueError:
        messagebox.showinfo("String Value!" , "Please enter integer values only")

    if guessNumber == actualNumber:
        messagebox.showinfo("Correct" , "You guessed the number correct it was "+str(actualNumber))
        attempts +=1
    elif guessNumber > actualNumber:
        messagebox.showinfo("Incorrect" , "the number is smaller")
        attempts +=1
    elif guessNumber < actualNumber:
        messagebox.showinfo("Incorrect" , "the number is bigger")
        attempts+=1
    atpsLabel.config(text="Attempts : "+str(attempts))
    

main_screen = Tk()
main_screen.title("Guess the Number")
main_screen.geometry("800x800")
main_screen.configure(bg ="#111c22")

headingLabel = Label(text= "Guess the Number Game" , width= 30 , height = 3 , font = ("Times New Roman" , 20) , bg = "#111c22" , fg = "white" , relief="raised")
headingLabel.place(x=100 , y = 50)

guessLabel = Label(text="Guess the Number here --> " , width = 20 , height = 2 , font = ("Times New Roman" , 15) , relief="raised" , bg = "#111c22"  , fg = "#eb5a5c" )
guessLabel.place(x = 50 , y = 300)

guessEntry = Entry(width = 20 , bg = "#111c22" , fg = "#90edac"  , font = ("Times New Roman" , 15))
guessEntry.place(x = 350, y = 300)

checkButton = Button(command= guessTheNumber , text= "Check" , width = 20 , height = 2 , font = ("Times New Roman" , 20) , bg = "#111c22" , fg = "#898bd3")
checkButton.place(x = 200 , y = 400)

atpsLabel = Label(text = "Attempts : 0" , font = ("Times New Roman" , 15) , bg = "#111c22" , fg = "#7069a0" , width = 10 , height= 1)
atpsLabel.place(x = 300 , y = 540)



main_screen.mainloop()