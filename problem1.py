from vex import *

#Define components connected
brain=Brain()

bumperA = Bumper(brain.three_wire_port.a)
ledA = Led(brain.three_wire_port.b)

#Initialize a count variable to keep track of light state
count = 10

#Infinite loop
while True:
    #When Bumper switch activated
    if bumperA.pressed():
        wait(50, MSEC) #Small Delay 50 milliseconds

        if count % 2 == 0: #If count can be divided without a remainder
            ledA.on()
        else:
            ledA.off()

        count = count + 1 #Increase Count variable by 1 for the next iteration 

    wait(20, MSEC) #While loop delay
