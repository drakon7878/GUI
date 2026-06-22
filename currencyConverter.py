import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)


from tkinter import *

def convert(event):
    inrEntry.delete(0, END)
    usd = float(usdEntry.get())
    inr = round(usd * 94.66 , 2)
    inrEntry.insert(0 , inr)    

main_screen = Tk()
main_screen.title("Currency Converter")
main_screen.configure(bg = "white")
main_screen.geometry("500x500")

headingLabel = Label(text="CURRENCY CONVERTER" , bg = "white" , fg = "black" , font = (50) , width= 30, height= 2 , relief= 'raised')
headingLabel.place(x=100 , y=0)

usdLabel = Label(text="USD" , bg = "white" , fg = "black" , font= (50) , width = 10, height = 1 , relief = "sunken")
usdLabel.place(x=20 , y = 100)

usdEntry = Entry(width= 20 , relief= "solid" , bg = "white" , fg = "black")
usdEntry.place(x = 150 , y = 100)

inrLabel = Label(text="INR" , bg = "white" , fg = "black" , font= (50) , width = 10, height = 1 , relief = "sunken")
inrLabel.place(x=20 , y = 200)

inrEntry = Entry(width= 20 , relief= "solid" , bg = "white" , fg = "black")
inrEntry.place(x = 150 , y = 200)


usdEntry.bind("<KeyRelease>" , convert)

main_screen.mainloop() 