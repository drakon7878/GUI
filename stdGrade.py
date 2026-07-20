import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

from tkinter import *

main = Tk()
main.geometry("1000x800")
main.title("Student Grading System")

percentage = 0
grade = "" 
name = "" 
rollNo = ""


def gradeCalc():
    global percentage , name , grade , rollNo   
    name = entName.get()
    rollNo = entRoll.get()
    maths = int(entMaths.get())
    eng = int(entEng.get())
    science = int(entScience.get())
    arts = int(entArts.get())
    IT = int(entIT.get())
    marks_obtained = maths+eng+science+arts+IT 
    percentage = (marks_obtained/500)*100
    if percentage >=80:
        grade = "A"
    elif percentage >=70:
        grade = "B"
    elif percentage >=60:
        grade = "C"
    elif percentage >=50:
        grade = "D"
    elif percentage <50:
        grade = "F"
    txtResult.delete("1.0" , "end-1c")
    txtResult.insert("1.0" , "Your Calculated Grade is "+grade+" with a \npercentage of "+str(percentage) )


def detailsSave():
    global percentage , name , grade , rollNo

    result = "Name: "+name+" RollNo: "+rollNo+" Grade: "+grade+" Percentage: "+str(percentage)+"\n"
    file = open("studentDetails.txt" , 'a')
    file.write(result)
    file.close()


heading = Label(text = "Student Grading System" , bg = "#ca93cc" , fg = "black" , font = ("Arial" , 25) , relief="raised")
heading.place(x =70 , y = 25)

labelName = Label(text = "Enter your name " , bg ="#8bbbbe" , fg = "black" , font = ("Arial" , 15) , width = 15 , height = 1 )
labelName.place(x = 70 , y = 125)

entName = Entry(width = 20 , bg ="#8bbbbe" , fg = "black" , font = ("Arial" , 15)  )
entName.place(x = 320, y = 125)

labelRoll = Label(text = "Enter your roll no. " , bg ="#98be8b" , fg = "black" , font = ("Arial" , 15) , width = 15 , height = 1 )
labelRoll.place(x = 70 , y = 175)

entRoll = Entry(width = 20 , bg ="#98be8b" , fg = "black" , font = ("Arial" , 15)  )
entRoll.place(x = 320, y = 175)

labelMaths = Label(text = "Enter your marks in Maths", bg ="#beba8b" , fg = "black" , font = ("Arial" , 15) , width = 20 , height = 1 )
labelMaths.place(x = 70 , y = 225)

entMaths = Entry(width = 20 , bg ="#beba8b" , fg = "black" , font = ("Arial" , 15)  )
entMaths.place(x = 400 , y= 225)

labelEng = Label(text = "Enter your marks in English", bg ="#beba8b" , fg = "black" , font = ("Arial" , 13) , width = 20 , height = 1 )
labelEng.place(x = 70 , y = 275)

entEng = Entry(width = 20 , bg ="#beba8b" , fg = "black" , font = ("Arial" , 15)  )
entEng.place(x = 400 , y= 275)

labelScience = Label(text = "Enter your marks in Science", bg ="#beba8b" , fg = "black" , font = ("Arial" , 13) , width = 20 , height = 1 )
labelScience.place(x = 70 , y = 325)

entScience = Entry(width = 20 , bg ="#beba8b" , fg = "black" , font = ("Arial" , 15)  )
entScience.place(x = 400 , y= 325)

labelIT = Label(text = "Enter your marks in IT", bg ="#beba8b" , fg = "black" , font = ("Arial" , 15) , width = 20 , height = 1 )
labelIT.place(x = 70 , y = 375)

entIT = Entry(width = 20 , bg ="#beba8b" , fg = "black" , font = ("Arial" , 15)  )
entIT.place(x = 400 , y= 375)

labelArts = Label(text = "Enter your marks in Arts", bg ="#beba8b" , fg = "black" , font = ("Arial" , 15) , width = 20 , height = 1 )
labelArts.place(x = 70 , y = 425)

entArts = Entry(width = 20 , bg ="#beba8b" , fg = "black" , font = ("Arial" , 15)  )
entArts.place(x = 400 , y= 425)


btnCalcGrade = Button(text = "Calculate Grade" ,  bg ="#c119a2" , fg = "black" , font = ("Arial" , 15) , width = 20 , height = 2  , command=gradeCalc)
btnCalcGrade.place(x = 70 , y = 475)


saveDetails = Button(text = "Save Details" ,  bg ="#d9748f" , fg = "black" , font = ("Arial" , 15) , width = 20 , height = 2  , command=detailsSave)
saveDetails.place(x = 500 , y = 475)

txtResult = Text(width = 30 , height = 3 , bg ="#81ada5" , fg = "black" , font = ("Arial" , 15) )
txtResult.place(x = 70 , y = 550)



main.mainloop()