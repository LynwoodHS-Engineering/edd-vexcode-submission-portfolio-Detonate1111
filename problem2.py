
from vex import *

brain=Brain()

#Declare hardware components
bumperA = Bumper(brain.three_wire_port.a)
bumperB = Bumper(brain.three_wire_port.b)
redLed = Led(brain.three_wire_port.c)
greenLed = Led(brain.three_wire_port.d)


#Continuous loop
while True:

    #Check if both conditions are being met
    if bumperA.pressing() and bumperB.pressing():
        greenLed.on()
        redLed.off()

    #If condition is false
    else:
        greenLed.off()
        redLed.on()

    wait(20, MSEC) #While loop delay
