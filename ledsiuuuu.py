# Imports go at the top
from microbit import *
import music
# Definición de una función
def encender_y_apagar_led(veces):
   for i in range(veces):
        display.show("X")
        sleep(500)
        music.play("D2:2")
        display.show("O")
        sleep(500)
#Llama a la función
encender_y_apagar_led(2)
