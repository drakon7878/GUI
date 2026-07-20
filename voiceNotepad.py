import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

from tkinter import *
import pyaudio
import speech_recognition as sr


main = Tk()
main.geometry("1000x500")
main.configure(bg="white")
main.title("Speech To Text")

def speechToText():
    try:
        recognizer  = sr.Recognizer()
        with sr.Microphone() as source:
            audioData = recognizer.listen(source)
        textData = recognizer.recognize_google(audioData)
        text1.insert("end-1c" , textData)
    except sr.UnknownValueError:
        print("Can't recognize your message")

def savetext():
    file = open("savedText.txt", "a")
    file.write("\n")
    file.write(text1.get("1.0" , "end-1c"))
    file.close()

def cleartext():
    text1.delete("1.0" , "end-1c")

heading =  Label(text="Speech to Text" , bg = "#6cc291" , fg = "black" , width = 12 , height = 1 , font = ("Arial" , 15))
heading.place(x = 50 , y =25)

start = Button(text = "Click to Start" , bg = "#cf92cb" , fg = "black" , width =15 , height = 2 , font = ("Arial" , 15) , relief = "raised" , command=speechToText)
start.place(x = 50 , y = 100)

text1 = Text(width = 50 , height = 5, bg = "#dfb562" , fg = "black")
text1.place(x = 300 , y = 100)

save = Button(text= "Save Text" , fg = "black" , bg ="#5fb1d4" , width = 10 , height = 2 , command=savetext )
save.place(x =300 , y = 250 )

clear= Button(text= "Clear Text" , fg = "black" , bg ="#ed5d6b" , width = 10 , height = 2, command=cleartext )
clear.place(x =400 , y = 250 )


main.mainloop()