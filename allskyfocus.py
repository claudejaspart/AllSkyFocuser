from email import message
from tkinter import *
from tkinter import messagebox
#import RPi.GPIO as GPIO    
from time import sleep

def forward():
    #GPIO.output(8, GPIO.HIGH) # Turn on
    a=0
    messagebox.showinfo("", "hello")


def reverse():
    #GPIO.output(8, GPIO.LOW) # Turn off
    b=0

def fastforward():
    #GPIO.output(8, GPIO.HIGH) # Turn on
    a=0
    messagebox.showinfo("", "hello")


def fastreverse():
    #GPIO.output(8, GPIO.LOW) # Turn off
    b=0



# GPIO initi
#GPIO.setwarnings(False)  
#GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
#GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 
#GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 
#GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 
#GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 

# init form
root = Tk()
root.title("AllSky camera focuser")
#mf.geometry('200x150')
root.resizable(width=0, height=0)

#variables
delay = StringVar(root, value="1")    # delay between activation of each coil
nbTurns = StringVar(root, value="100")  # autostepping
position = StringVar(root, value="0") # position of motor
st_p1 = 35    # pin 1 of motor
st_p2 = 36
st_p3 = 37
st_p4 = 38

# Ligne 1 : Delay (def:2)
Label(root, text="Delay", width=20).grid(row=0, sticky=W) 
Entry(root, textvariable = delay, width=20).grid(row=0, column=1, sticky=E) 

# Ligne 2 : Autostepping (def:100)
Label(root, text="Autostepping", width=20).grid(row=1, sticky=W) 
Entry(root, textvariable = nbTurns, width=20).grid(row=1, column=1, sticky=E)

# ligne 3 : Position
Label(root, text="Position", width=20).grid(row=2, sticky=W) 
Entry(root, textvariable = position, width=20).grid(row=2, column=1, sticky=E)

# ligne 4 : fr + reverse
Button(root ,text="<<", width=20, command=fastreverse).grid(row=3, sticky=W)
Button(root ,text="<", width=20,command=reverse).grid(row=3, column=1, sticky=E)

# ligne 5 : ff + forward
Button(root ,text=">", width=20, command=fastreverse).grid(row=4, sticky=W)
Button(root ,text=">>", width=20,command=reverse).grid(row=4, column=1, sticky=E)


root.mainloop()