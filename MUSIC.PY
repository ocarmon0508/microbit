
# Imports go at the top 
from microbit import *
import music

melodias= [music.POWER_UP,music.JUMP_DOWN,music.JUMP_UP,music.POWER_DOWN, music.DADADADUM]

i=0 
while True:
    if button_a.was_pressed():
        i = i + 1
        if(i==len(melodias)):
            i=0
    elif button_b.was_pressed():
        i = i - 1
        if
