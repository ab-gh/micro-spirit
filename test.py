from microbit import *

while True:
    roll = accelerometer.get_x()
    pitch = accelerometer.get_y()
    if -50 <= pitch <= 50:
        display.show(Image.HEART)
    else:
        display.show("x")