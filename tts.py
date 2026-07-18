import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

from tkinter import * 
import gtts

def textToSpeech():
    text1 = entry1.get("1.0" , "end-1c")
    print(text1)
    audioData = gtts.gTTS(text=text1 , lang="en" , slow= False)
    audioData.save("result.mp3")

main = Tk()
main.title("Text to Speech")
main.geometry("900x900")
main.config(bg = "white")

heading1 = Label(text = "Text To Speech" , font = ("Arial" , 25) , bg = "pink" , fg = "black" , width = 30 , height = 3)
heading1.place(x = 50,y = 0)

entry1 = Text(fg = "black" , bg = "#cddc3f" , width = 80 , height = 5 , font = ("Arial" , 10))
entry1.place(x  = 100 , y = 220)

submit = Button(width = 30 , height = 2 , bg = "#72f123" , text = "Submit" , font = ("Arial" , 15) , command=textToSpeech) 
submit.place(x = 200 , y = 400 )

main,mainloop()