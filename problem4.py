
from vex import *
import time

def updateDisplay():
    
    brain.screen.set_fill_color(Color.BLUE)
    brain.screen.draw_rectangle(180, 80, 140, 80) 
    potPin = potentiometer_e.value()
    brain.screen.set_cursor(6, 24)
    brain.screen.print(potPin)
    time.sleep(0.1)
    brain.screen.clear_screen()
        
    time.sleep(0.005)#I know it says 100ms but I couldn't stand the flickering so I reduced it alot

brain=Brain()
potentiometer_e = Potentiometer(brain.three_wire_port.e)
brain.screen.clear_screen()
  

while True:
    updateDisplay()
