(from) # Imports go at the top
from microbit import *

for i in range(1, 101):
    display.scroll(str(i))
 (while)   
# Imports go at the top
from microbit import *

#invertido. para ir desde 101 hasta 1. 
for i in range (101, 1, -1):
    display.scroll(str(i))
    
from microbit import *
#para contar de 5 en 5 usando for. 
for i in range (1, 101, 5)
    display.scroll(str(i))
     (while) 
    # Imports go at the top
from microbit import *
i=1
while(i<31):
    display.scroll(str(i))
    i=i+5
______________________________________________________-    
    (nuevo)
    from microbit import*

for x in range(5):
    display.set_pixel(x,0,9)
    sleep(500)
    display.set_pixel(x,1,9)
    sleep(500)
    display.clear()
    sleep(500)
    
   __________________________________
from microbit import*

#mostrar una lista de vocales 

lista_numeros_primos = [2,3,5,7,11,13]

for i in lista_numeros_primos: 
    display.scroll(i)
    sleep(1000)
    _______________________________________________
    #import go at the top
from microbit import*

#mostrar una lista de vocales 
lista_vocales = ["A","E","I","O","U"]

index = 0

while(index<len(lista_vocales)):
    display.show(lista_vocales[index])
    index = index + 1
    sleep(1000)
    _________________________________________________________
    ##################
# ¿Que imprime?  #
##################
from microbit import * 



texto = "Microbit"
i=0
while(i<len(texto)):
    display.show(texto[i])
    i = i + 2
    sleep(500)

