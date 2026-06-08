import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

from tkinter import *
#making a screen
main_screen = Tk()
main_screen.title("My first GUI")
main_screen.config(bg="blue")
main_screen.geometry("800x800")

#PLACEMENT
#pack --> 1 below other
#grid  --> screen divided into rows and columns (a grid)
#place --> coords


#labels
l1 = Label(text="Welcome to tk Inter" , width=30 , height= 2 , bg = "black" , fg="white" , font=("Arial" , 20) )
l1.place(x = 100 , y=50)

l2 = Label(text="Enter your name here -->" , width = 20, height = 1 , bg = "white" , fg = "blue" , font= ("Arial" , 10))
l2.place(x = 50 , y = 150)



#input methods
E1 = Entry(width=20 , bg = "white" , fg = "red")
E1.place(x = 280 , y = 150)

l3 = Label(text = "Enter something about yourself -->" , width= 30, height = 2 , bg="white" , fg = "black" , font=("Arial" , 10))
l3.place(x = 50 , y = 250)

t1 = Text(width= 30 , height = 4 , bg = "white" , fg = "purple")
t1.place(x = 350  , y = 250)


#BUTTONS
#radiobuttons --> Multiple choices but 1 answer

l4 = Label(text="Select Your Gender" , width = 30 , height= 2 , bg = "white"  , fg = "blue" , font=("Arial" , 10))
l4.place(x = 50 , y = 400)


r1 = Radiobutton(text="Female" , value=1)
r1.place(x = 350 , y = 400 )

r2 = Radiobutton(text="Male" , value = 2)
r2.place(x = 550 , y = 400)

#normal buttons
b1 = Button(text = "Submit" , width = 20 , height = 1 , font = ("Arial" , 10) ,  bg = "black" , fg = "white")
b1.place(x =300 , y = 700)
main_screen.mainloop()
