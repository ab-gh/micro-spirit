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

l_h_roll = Image("00000:"
                 "90000:"
                 "09990:"
                 "00009:"
                 "00000")

r_h_roll = Image("00000:"
                 "00009:"
                 "09990:"
                 "90000:"
                 "00000")

h_roll = Image("00900:"
               "00900:"
               "00900:"
               "00900:"
               "00900")

if button_a.is_pressed():
    button = "a"
else:
     button = "b"

while True:
    roll = accelerometer.get_x()
    if -100 <= roll <= -10:
        display.show(c_roll)
    elif 10 <= roll <= 100:
        display.show(c_roll)
    elif -10 <= roll <= 10
        display.show(h_roll)
    elif 100 <= roll <= 500:
        display.show(r_h_roll)
    elif -500 <= roll <= 100:
        display.show(l_h_roll)
    elif 500 <= roll <= 1000:
        display.show(r_roll)
    elif -1000 <= roll <= -500:
        display.show(l_roll)
    else:
        display.show(h_roll)


#flat = -1024
