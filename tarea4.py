from microbit import*

cascada1 = Image("50000:09000:99900:09000:00005") 
cascada2 = Image("50000:00900:09990:00900:00000")
cascada3 = Image("50000:00090:00999:00090:00000")
cascada4 = Image("50000:00009:90099:00009:00000")
cascada5 = Image("50000:90000:99009:90000:00005")


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
