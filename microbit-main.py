# Imports go at the top
from microbit import *
#variable contador
cont = 0


while True:
    if button_a.was_pressed():
        cont = cont + 1
    if button_b.was_pressed():
        cont = cont -1
    display.scroll(cont)    
  
