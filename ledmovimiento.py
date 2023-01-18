from microbit import*

cascada1 = Image("00000:13731:37973:13731:00000") 
cascada2 = Image("00000:00000:13731:37973:13731")
cascada3 = Image("13731:00000:00000:13731:37973")
cascada4 = Image("37973:13731:00000:00000:13731")
cascada5 = Image("13731:37973:13731:00000:00000")


while True:
    display.show(cascada1)
    sleep(200)
    display.show(cascada2)
    sleep(200)
    display.show(cascada3)
    sleep(200)
    display.show(cascada4)
    sleep(200)
    display.show(cascada5)
    sleep(200)
