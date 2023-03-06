# Imports go at the top
from microbit import *
#Import sounds
imagenes = [Image.ALL_ARROWS,
            Image.ALL_CLOCKS,
            Image.ANGRY,
            Image.ARROW_E,
            Image.ARROW_N]

sonidos = [Sound.MYSTERIOUS,
             Sound.GIGGLE,
             Sound.HAPPY]
while True:

    if button_a.was_pressed():
        imagenes = imagenes 
