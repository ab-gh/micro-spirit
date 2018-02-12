from microbit import *
# Images
# /
r_roll = Image("00009:" "00090:" "00900:" "09000:" "90000")
# -
c_roll = Image("00000:" "00000:" "99999:" "00000:" "00000")
# \
l_roll = Image("90000:" "09000:" "00900:" "00090:" "00009")
# \-\
l_h_roll = Image("00000:" "90000:" "09990:" "00009:" "00000")
# /-/
r_h_roll = Image("00000:" "00009:" "09990:" "90000:" "00000")
# |
h_roll = Image("00900:" "00900:" "00900:" "00900:" "00900")
# +
d_roll = Image("00000:" "00500:" "99999:" "00500:" "00000")
# /|/
r_n_roll = Image("00090:" "00900:" "00900:" "00900:" "09000")
# \|\
l_n_roll = Image("09000:" "00900:" "00900:" "00900:" "00090")
# <->
startim = Image("00000:" "09090:" "99999:" "09090:" "00000")
# Main
compass.calibrate()
while True:
    button = 2
    display.show(startim)
    if button_a.is_pressed() == True:
        button = 0
    elif button_b.is_pressed() == True:
        button = 1
    else:
        button = button
    if button == 0:
        display.show(" ")
        while True:
            roll = accelerometer.get_x()
            pitch = accelerometer.get_y()
            if -1024 <= roll <= -900:  # horizontal
                display.show(h_roll)
            elif -900 <= roll <= -700:  # near horizontal left
                display.show(l_n_roll)
            elif -700 <= roll <= -500:  # left
                display.show(l_roll)
            elif -500 <= roll <= -100:  # near vertical left
                display.show(l_h_roll)
            elif -100 <= roll <= -40:  # vertical
                display.show(c_roll)
            elif -40 <= roll <= 40:  # dead centre
                display.show(d_roll)
            elif 40 <= roll <= 100:  # vertical
                display.show(c_roll)
            elif 100 <= roll <= 500:  # near vertical right
                display.show(r_h_roll)
            elif 500 <= roll <= 700:  # right
                display.show(r_roll)
            elif 700 <= roll <= 900:  # near horizontal right
                display.show(r_n_roll)
            elif 900 <= roll <= 1024:  # horizontal
                display.show(h_roll)
            elif button_b.is_pressed() == True:
                button = 1
    elif button == 1:
        display.show(" ")
        while True:
            pitch = accelerometer.get_y()
            if -1024 <= pitch <= -500:
                display.set_pixel(2, 0, 9)
                display.set_pixel(2, 1, 0)
                display.set_pixel(2, 2, 0)
                display.set_pixel(2, 3, 0)
                display.set_pixel(2, 4, 0)
            elif -500 <= pitch <= -100:
                display.set_pixel(2, 0, 0)
                display.set_pixel(2, 1, 9)
                display.set_pixel(2, 2, 0)
                display.set_pixel(2, 3, 0)
                display.set_pixel(2, 4, 0)
            elif -100 <= pitch <= 100:
                display.set_pixel(2, 0, 0)
                display.set_pixel(2, 1, 0)
                display.set_pixel(2, 2, 9)
                display.set_pixel(2, 3, 0)
                display.set_pixel(2, 4, 0)
            elif 100 <= pitch <= 500:
                display.set_pixel(2, 0, 0)
                display.set_pixel(2, 1, 0)
                display.set_pixel(2, 2, 0)
                display.set_pixel(2, 3, 9)
                display.set_pixel(2, 4, 0)
            elif 500 <= pitch <= 1024:
                display.set_pixel(2, 0, 0)
                display.set_pixel(2, 1, 0)
                display.set_pixel(2, 2, 0)
                display.set_pixel(2, 3, 0)
                display.set_pixel(2, 4, 9)
            else:
                display.show(" ")
            yaw = accelerometer.get_z()
            if -1200 <= yaw <= -1024:
                display.set_pixel(0, 2, 0)
                display.set_pixel(1, 2, 0)
                display.set_pixel(2, 2, 9)
                display.set_pixel(3, 2, 0)
                display.set_pixel(4, 2, 0)
            elif -1024 <= yaw <= -500:
                display.set_pixel(0, 2, 0)
                display.set_pixel(1, 2, 9)
                display.set_pixel(3, 2, 9)
                display.set_pixel(4, 2, 0)
            elif -500 <= yaw <= 1024:
                display.set_pixel(0, 2, 9)
                display.set_pixel(1, 2, 0)
                display.set_pixel(3, 2, 0)
                display.set_pixel(4, 2, 9)
            else:
                display.show(" ")
