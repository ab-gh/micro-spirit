from microbit import *
# /
r_roll = Image("00009:"
               "00090:"
               "00900:"
               "09000:"
               "90000")
# -
c_roll = Image("00000:"
               "00000:"
               "99999:"
               "00000:"
               "00000")
# \
l_roll = Image("90000:"
               "09000:"
               "00900:"
               "00090:"
               "00009")

# \-\
l_h_roll = Image("00000:"
                 "90000:"
                 "09990:"
                 "00009:"
                 "00000")

# /-/
r_h_roll = Image("00000:"
                 "00009:"
                 "09990:"
                 "90000:"
                 "00000")

# |
h_roll = Image("00900:"
               "00900:"
               "00900:"
               "00900:"
               "00900")

# +
d_roll = Image("00000:"
               "00500:"
               "99999:"
               "00500:"
               "00000")

# /|/
r_n_roll = Image("00090:"
                 "00900:"
                 "00900:"
                 "00900:"
                 "09000")

# \|\
l_n_roll = Image("09000:"
                 "00900:"
                 "00900:"
                 "00900:"
                 "00090")

if button_a.is_pressed():
    button = "a"
else:
    button = "b"

while True:
    roll = accelerometer.get_x()
    pitch = accelerometer.get_y()
    if -1024 <= roll <= -900:           # horizontal
        display.show(h_roll)
    elif -900 <= roll <= -700:          # near horizontal left
        display.show(l_n_roll)
    elif -700 <= roll <= -500:          # left
        display.show(l_roll)
    elif -500 <= roll <= -100:          # near vertical left
        display.show(l_h_roll)
    elif -100 <= roll <= -40:           # vertical
        display.show(c_roll)
    elif -40 <= roll <= 40:             # dead centre
        display.show(d_roll)
    elif 40 <= roll <= 100:             # vertical
        display.show(c_roll)
    elif 100 <= roll <= 500:            # near vertical right
        display.show(r_h_roll)
    elif 500 <= roll <= 700:            # right
        display.show(r_roll)
    elif 700 <= roll <= 900:            # near horizontal right
        display.show(r_n_roll)
    elif 900 <= roll <= 1024:           # horizontal
        display.show(h_roll)
    #elif 40 <= roll <= 40 and 40 <= pitch <= 40:

# flat = -1024
