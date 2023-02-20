# Imports goat the top
from microbit import* 


lista_numeros = [3, 4, 2, 4, 2]
total = 0
for i in lista_numeros:
    total = total + i 

    display.scroll(total)
