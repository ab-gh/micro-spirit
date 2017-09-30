from microbit import *

## Bitmapping

##  0 1 2 3 4
##  1
##  2
##  3
##  4

## Bitmaps
#  Top
t_pitch = Image("00900:"
                "00000:"
                "00000:"
                "00000:"
                "00000")
#  Up
u_pitch = Image("00000:"
                "00900:"
                "00000:"
                "00000:"
                "00000")
# Centre
c_pitch = Image("00000:"
                "00000:"
                "00900:"
                "00000:"
                "00000")
# Down
d_pitch = Image("00000:"
                "00000:"
                "00000:"
                "00900:"
                "00000")
# Bottom
b_pitch = Image("00000:"
                "00000:"
                "00000:"
                "00000:"
                "00900")



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



