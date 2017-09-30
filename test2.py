from microbit import *

while True:
    if button_a.is_pressed() == True:
        button = 0
    else:
        button = 1
while True:
    if button == 0:
        display.show("x")
    else:
        display.show(" ")
