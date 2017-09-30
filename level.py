from microbit import *

while True:
    roll = accelerometer.get_x()
    pitch = accelerometer.get_y()
    if 500 <= pitch <= 600:
        display.show(Image.HEART)
    else:
        display.show("x")
