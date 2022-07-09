from tkinter import *
from tkinter import messagebox
import RPi.GPIO as GPIO    
import time

def forward():
    moveForward(0)

def reverse():
    moveBackward(0)

def fastforward():
    moveForward(1)

def fastreverse():
    moveBackward(1)

def savePosition():
    global position
    file = open('position.txt', 'w')
    file.write(position.get())
    file.close()
    
def readPosition():
    global position
    file = open('position.txt', 'r')
    pos = file.read()
    file.close()
    return pos

def moveBackward(fast):

    global nbTurns1
    global delay
    global STEPPER1_PIN_1
    global STEPPER1_PIN_2
    global STEPPER1_PIN_3
    global STEPPER1_PIN_4

    nbTurns = int(nbTurns1.get())
    
    if fast == 1:
      nbTurns = nbTurns * 3
    
    # nombre de pas
    step_number = 0

    while step_number < (nbTurns * 4) and int(position.get()) > 0:
        moveCoilForward(step_number%4)
        step_number = step_number + 1
        position.set(int(position.get())-1)
        if int(position.get()) <= 0:
            break
        time.sleep(0.001 * int(delay.get()))
    
    GPIO.output(STEPPER1_PIN_1, GPIO.LOW)
    GPIO.output(STEPPER1_PIN_2, GPIO.LOW)
    GPIO.output(STEPPER1_PIN_3, GPIO.LOW)
    GPIO.output(STEPPER1_PIN_4, GPIO.LOW)
    savePosition()


def moveForward(fast):

    global nbTurns1
    global delay
    global STEPPER1_PIN_1
    global STEPPER1_PIN_2
    global STEPPER1_PIN_3
    global STEPPER1_PIN_4

    nbTurns = int(nbTurns1.get())
    
    if fast == 1:
      nbTurns = nbTurns * 3
    
    # nombre de pas
    step_number = 0

    while step_number < (nbTurns * 4) :
        moveCoilBackward(step_number%4)
        step_number = step_number + 1
        position.set(int(position.get())+1)
        time.sleep(0.001 * int(delay.get()))
    
    GPIO.output(STEPPER1_PIN_1, GPIO.LOW)
    GPIO.output(STEPPER1_PIN_2, GPIO.LOW)
    GPIO.output(STEPPER1_PIN_3, GPIO.LOW)
    GPIO.output(STEPPER1_PIN_4, GPIO.LOW)
    savePosition()


def moveCoilForward(coil_number) :
    global STEPPER1_PIN_1
    global STEPPER1_PIN_2
    global STEPPER1_PIN_3
    global STEPPER1_PIN_4
    
    if coil_number == 0:
        GPIO.output(STEPPER1_PIN_1, GPIO.HIGH)
        GPIO.output(STEPPER1_PIN_2, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_3, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_4, GPIO.LOW)
    elif coil_number == 1:
        GPIO.output(STEPPER1_PIN_1, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_2, GPIO.HIGH)
        GPIO.output(STEPPER1_PIN_3, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_4, GPIO.LOW)
    elif coil_number == 2:
        GPIO.output(STEPPER1_PIN_1, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_2, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_3, GPIO.HIGH)
        GPIO.output(STEPPER1_PIN_4, GPIO.LOW)
    elif coil_number == 3:
        GPIO.output(STEPPER1_PIN_1, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_2, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_3, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_4, GPIO.HIGH)
        
  
def moveCoilBackward(coil_number) :
    global STEPPER1_PIN_1
    global STEPPER1_PIN_2
    global STEPPER1_PIN_3
    global STEPPER1_PIN_4
    
    if coil_number == 0:
        GPIO.output(STEPPER1_PIN_1, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_2, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_3, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_4, GPIO.HIGH)
    elif coil_number == 1:
        GPIO.output(STEPPER1_PIN_1, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_2, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_3, GPIO.HIGH)
        GPIO.output(STEPPER1_PIN_4, GPIO.LOW)
    elif coil_number == 2:
        GPIO.output(STEPPER1_PIN_1, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_2, GPIO.HIGH)
        GPIO.output(STEPPER1_PIN_3, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_4, GPIO.LOW)
    elif coil_number == 3:
        GPIO.output(STEPPER1_PIN_1, GPIO.HIGH)
        GPIO.output(STEPPER1_PIN_2, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_3, GPIO.LOW)
        GPIO.output(STEPPER1_PIN_4, GPIO.LOW)



# init form
root = Tk()
root.title("AllSky camera focuser")
root.resizable(width=0, height=0)

#variables
delay = StringVar(root, value="5")    # delay between activation of each coil
nbTurns1 = StringVar(root, value="10")  # autostepping
position = StringVar(root, value=readPosition()) # position of motor
STEPPER1_PIN_1 = 35    # pin 1 of motor
STEPPER1_PIN_2 = 36
STEPPER1_PIN_3 = 37
STEPPER1_PIN_4 = 38

# GPIO initi
GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(STEPPER1_PIN_1, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(STEPPER1_PIN_2, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(STEPPER1_PIN_3, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(STEPPER1_PIN_4, GPIO.OUT, initial=GPIO.LOW) 

# Ligne 1 : Delay (def:2)
Label(root, text="Delay", width=20).grid(row=0, sticky=W) 
Entry(root, textvariable = delay, width=20).grid(row=0, column=1, sticky=E) 

# Ligne 2 : Autostepping (def:100)
Label(root, text="Autostepping", width=20).grid(row=1, sticky=W) 
Entry(root, textvariable = nbTurns1, width=20).grid(row=1, column=1, sticky=E)

# ligne 3 : Position
Label(root, text="Position", width=20).grid(row=2, sticky=W) 
Entry(root, textvariable = position, width=20,state=DISABLED).grid(row=2, column=1, sticky=E)

# ligne 4 : fr + reverse
Button(root ,text="<<", width=20, command=fastreverse).grid(row=3, sticky=W)
Button(root ,text="<", width=20,command=reverse).grid(row=3, column=1, sticky=E)

# ligne 5 : ff + forward
Button(root ,text=">", width=20, command=forward).grid(row=4, sticky=W)
Button(root ,text=">>", width=20,command=fastforward).grid(row=4, column=1, sticky=E)


root.mainloop()
