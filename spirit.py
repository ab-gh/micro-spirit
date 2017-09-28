from microbit import *
## /
r_roll = Image("00009:"
               "00090:"
               "00900:"
               "09000:"
               "90000")
##-
c_roll = Image("00000:"
               "00000:"
               "99999:"
               "00000:"
               "00000")
##\
l_roll = Image("90000:"
               "09000:"
               "00900:"
               "00090:"
               "00009")
while True:
    roll = accelerometer.get_x()
    if -100 <= roll <= 100:
        display.show(c_roll)
    elif roll > 100:
        display.show(r_roll)
    else:
        display.show(l_roll)
while True:
    roll = accelerometer.get_x()
    if -10 <= roll <= 10:
        display.show(Image.YES)

