from microbit import *
while True:
    roll = accelerometer.get_x()
    pitch = accelerometer.get_y()
        if -1024 <= pitch <= -900:
            display.show(Image.HEART)