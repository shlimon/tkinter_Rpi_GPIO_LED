from tkinter import *
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)


def sel():
    selection = var.get()
    if selection == 1:
        GPIO.output(11,0)
        GPIO.output(12,1)
    elif selection == 2:
        GPIO.output(11,1)
        GPIO.output(12,0)

window = Tk()
window.title("LED Switch")

var = IntVar()

R1 = Radiobutton(window, text= "Turn Blue", variable = var, value =1, command = sel) .grid(row=0,column=0)

R2 = Radiobutton(window, text= "Turn Red", variable = var, value =2, command = sel) .grid(row=0,column=1)

R3 = Radiobutton(window, text= "Turn Yellow", variable = var, value =3, command = sel) .grid(row=0,column=2)

Label(window, text = "CLICK THE Button TO EXIT",fg ="black",font = "none 12 bold") .grid(row =2, column =1)

def close_window():
    GPIO.cleanup()
    window.destroy()
    exit()

Button(window, text ="EXIT", width = 5, command = close_window) .grid(row=3, column =1)


window.mainloop()