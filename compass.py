from microbit import *
# Images

compa_N = Image("00900:"
                "00000:"
                "00000:"
                "00000:"
                "00000")
compa_NNE = Image("00090:"
                "00000:"
                "00000:"
                "00000:"
                "00000")
compa_NE = Image("00009:"
                "00000:"
                "00000:"
                "00000:"
                "00000")
compa_ENE = Image("00000:"
                "00009:"
                "00000:"
                "00000:"
                "00000")
compa_E = Image("00000:"
                "00000:"
                "00009:"
                "00000:"
                "00000")
compa_ESE = Image("00000:"
                "00000:"
                "00000:"
                "00009:"
                "00000")
compa_SE = Image("00000:"
                "00000:"
                "00000:"
                "00000:"
                "00009")
compa_SSE = Image("00000:"
                "00000:"
                "00000:"
                "00000:"
                "00090")
compa_S = Image("00000:"
                "00000:"
                "00000:"
                "00000:"
                "00900")
compa_SSW = Image("00000:"
                "00000:"
                "00000:"
                "00000:"
                "09000")
compa_SW = Image("00000:"
                "00000:"
                "00000:"
                "00000:"
                "90000")
compa_WSW = Image("00000:"
                "00000:"
                "00000:"
                "90000:"
                "00000")
compa_W = Image("00000:"
                "00000:"
                "90000:"
                "00000:"
                "00000")
compa_WNW = Image("00000:"
                "90000:"
                "00000:"
                "00000:"
                "00000")
compa_NW = Image("90000:"
                "00000:"
                "00000:"
                "00000:"
                "00000")
compa_NWW = Image("09000:"
                "00000:"
                "00000:"
                "00000:"
                "00000")

# Main

compass.calibrate()
while True:
    button = 2
    button = 3
    if button == 3:
        display.show(" ")
        while True:
            degrees = compass.heading()
            if degrees < 22:
                display.show(compa_N)
            elif degrees < 45:
                display.show(compa_NNE)
            elif degrees < 67:
                display.show(compa_NE)
            elif degrees < 90:
                display.show(compa_ENE)
            elif degrees < 112:
                display.show(compa_E)
            elif degrees < 135:
                display.show(compa_ESE)
            elif degrees < 158:
                display.show(compa_SE)
            elif degrees < 180:
                display.show(compa_SSE)
            elif degrees < 202:
                display.show(compa_SSW)
            elif degrees < 225:
                display.show(compa_SW)
            elif degrees < 247:
                display.show(compa_WSW)
            elif degrees < 270:
                display.show(compa_W)
            elif degrees < 292:
                display.show(compa_WNW)
            elif degrees < 315:
                display.show(compa_NW)
            elif degrees < 337:
                display.show(compa_NWW)
            else:
                display.show(compa_N)
