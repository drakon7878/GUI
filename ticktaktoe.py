import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

from tkinter import *
from tkinter import messagebox
turn = "X"
win = False
turns = 0

def ticktacktoe(buttonName):
    global turn , win , turns
    buttonName.config(text = turn)
    buttonName.config(state = DISABLED)
    if turn == "X":
        buttonName.config(bg = "red")
    else:
        buttonName.config(bg = "blue")
    turns +=1

    if button1.cget("text") == button2.cget("text") == button3.cget("text") != "":
        win = True
        messagebox.showinfo("Win!!" , "You win: "+ turn)
        disabled()
        return
    elif button4.cget("text") == button5.cget("text") == button6.cget("text") != "":
        win = True
        messagebox.showinfo("Win!!" , "You win: "+ turn)
        disabled
        return
    elif button7.cget("text") == button8.cget("text") == button9.cget("text") != "":
        win = True
        messagebox.showinfo("Win!!" , "You win: "+ turn)
        disabled()
        return
    elif button1.cget("text") == button4.cget("text") == button7.cget("text") != "":
        win = True
        messagebox.showinfo("Win!!" , "You win: "+ turn)
        disabled()
        return
    elif button2.cget("text") == button5.cget("text") == button8.cget("text") != "":
        win = True
        messagebox.showinfo("Win!!" , "You win: "+ turn)
        disabled()
        return
    elif button3.cget("text") == button6.cget("text") == button9.cget("text") != "":
        win = True
        messagebox.showinfo("Win!!" , "You win: "+ turn)
        disabled()
        return
    elif button1.cget("text") == button5.cget("text") == button9.cget("text") != "":
        win = True
        messagebox.showinfo("Win!!" , "You win: "+ turn)
        disabled()
        return
    elif button3.cget("text") == button5.cget("text") == button7.cget("text") != "":
        win = True
        messagebox.showinfo("Win!!" , "You win: "+ turn)
        disabled()
        return
    elif turns == 9 and win == False:
        messagebox.showinfo("DRAW" , "It's a draw..")

    if turn == "X": 
        turn = "O"
    else:
        turn = "X"
    
    turnLabel.config(text='Turn: '+turn)

def disabled():
    global win
    if win == True:
        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)

def enabled():
    global win , turn, turns
    win = False
    turn = "X"
    turns = 0
    turnLabel.config(text="Turn: "+turn)
    button1.config(state=NORMAL  , text = "")
    button2.config(state=NORMAL, text = "")
    button3.config(state=NORMAL, text = "")
    button4.config(state=NORMAL, text = "")
    button5.config(state=NORMAL, text = "")
    button6.config(state=NORMAL, text = "")
    button7.config(state=NORMAL, text = "")
    button8.config(state=NORMAL, text = "")
    button9.config(state=NORMAL, text = "")

main_screen = Tk()
main_screen.geometry("600x600")
main_screen.config(bg = "black")
main_screen.title("Tick Tak Toe Game")

headingLabel = Label(text = "Tick Tack Toe" , width = 20 , height = 2 , font=("Arial" , 20) , bg = "black" , fg = "white"  ,relief="raised")
headingLabel.place(x =70 , y = 50)

turnLabel = Label(text="Turn: "+turn , bg = "black" , fg = "white" , relief="sunken" , width = 15 , height= 1 , font = ("Arial" , 15))
turnLabel.place(x = 120 , y = 150)

button1 = Button(text = "" , width = 15 , height = 3 , bg = "white" , relief="raised" , command=lambda: ticktacktoe(button1))
button1.place(x = 50 , y = 200)

button2 = Button(text = "" , width = 15 , height = 3 , bg = "white" , relief="raised" , command=lambda: ticktacktoe(button2))
button2.place(x = 200 , y = 200)

button3 = Button(text = "" , width = 15 , height = 3 , bg = "white" , relief="raised", command=lambda: ticktacktoe(button3) )
button3.place(x = 350 , y = 200)

button4 = Button(text = "" , width = 15 , height = 3 , bg = "white" , relief="raised", command=lambda: ticktacktoe(button4) )
button4.place(x = 50 , y = 300)

button5 = Button(text = "" , width = 15 , height = 3 , bg = "white" , relief="raised" , command=lambda: ticktacktoe(button5))
button5.place(x = 200 , y = 300)

button6 = Button(text = "" , width = 15 , height = 3 , bg = "white" , relief="raised" , command=lambda: ticktacktoe(button6))
button6.place(x = 350 , y = 300)


button7 = Button(text = "" , width = 15 , height = 3 , bg = "white" , relief="raised" , command=lambda: ticktacktoe(button7))
button7.place(x = 50 , y = 400)

button8 = Button(text = "" , width = 15 , height = 3 , bg = "white" , relief="raised" , command=lambda: ticktacktoe(button8))
button8.place(x = 200 , y = 400)

button9 = Button(text = "" , width = 15 , height = 3 , bg = "white" , relief="raised" , command=lambda: ticktacktoe(button9))
button9.place(x = 350 , y = 400)

reset = Button(text = "Reset" , width = 20 , height= 1 , bg = "black" , fg = "white" ,relief="raised" , font = ("Arial" , 15), command = enabled)
reset.place(x = 100 , y = 500)
main_screen.mainloop()