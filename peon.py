# Imports go at the top
from microbit import *
from Maqueen import * 
robot = Maqueen()
while True : 
    if button_a.was_pressed():
        robot.mover_celda()
    elif button_b.was_pressed():
        robot.mover_celda()
        robot.mover_celda()
