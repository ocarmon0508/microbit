# Imports go at the top
from microbit import *
import music


texto= "";
notas = ['F4:3','C4:3','A4:3','F4:2','C5:2','B4:2','A4:3','G4:3','F4:2','F4:3','E4:3','D4:2','C4:2',]
         
    

display.scroll(texto, delay=40)
music.play(notas, wait=False, loop=True)

while True:
    display.show(Image.HEART)
    sleep(1000)
    display.show(Image.HEART_SMALL)
    sleep(1000)
