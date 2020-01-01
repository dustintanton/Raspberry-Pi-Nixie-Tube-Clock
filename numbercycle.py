import time
import RPi.GPIO as GPIO
import random
GPIO.setmode(GPIO.BCM)

# Time Variables Instances
localtime = time.localtime(time.time())
hour = localtime.tm_hour
min = localtime.tm_min
sec = localtime.tm_sec
global count = 0

# 2nd digit seconds bulb
#        a  b   c   d
bulb1 = [4, 17, 27, 22]
bulb2 = [10, 9, 11, 5]
bulb3 = [6, 13, 19, 26]
bulb6 = [14, 15, 18, 23]
bulb5 = [24, 25, 8, 7]
bulb4 = [12, 16, 20, 21]

def main():
    try:
        while count < 10:
               findFunctionNumber(count, bulb1)
               findFunctionNumber(count, bulb2)
               findFunctionNumber(count, bulb3)
               findFunctionNumber(count, bulb4)
               findFunctionNumber(count, bulb5)
               findFunctionNumber(count, bulb6)
               count = count + 1
    finally:
        setOff(bulb1)
        setOff(bulb2)
        setOff(bulb3)
        setOff(bulb4)
        setOff(bulb5)
        setOff(bulb6)


def flicker():
    time.sleep(.3)
    x = int(random.random() * 10)
    y = int(random.random() * 10)
    if (x == 1):
        if (y % 2 == 0):
            setOff(bulb6)
            time.sleep(.1)
            setOn(bulb6)
            time.sleep(.6)
        if (y % 2 == 1):
            setOff(bulb5)
            time.sleep(.1)
            setOn(bulb5)
            time.sleep(.6)
    else:
        time.sleep(.7)

def findTube(tube):
    if (tube == 1):
        bulb1
        return bulb1
    if (tube == 2):
        bulb2
        return bulb2
    if (tube == 3):
        bulb3
        return bulb3
    if (tube == 4):
        bulb4
        return bulb4
    if (tube == 5):
        bulb5
        return bulb5
    if (tube == 6):
        bulb6
        return bulb6

def findFunctionNumber(x,bulb):
    if(x == 0):
        set0(bulb)

    if (x == 9):
        set1(bulb)

    if (x == 8):
        set2(bulb)

    if (x == 7):
        set3(bulb)

    if (x == 6):
        set4(bulb)

    if (x == 5):
        set5(bulb)

    if (x == 4):
        set6(bulb)

    if (x == 3):
        set7(bulb)

    if (x == 2):
        set8(bulb)

    if (x == 1):
        set9(bulb)

    if (x == 11):
        setOff(bulb)

    if (x == 12):
        setOn(bulb)


def findTime():
    # find time and set first variables to time values
    localtime = time.localtime(time.time())
    hour = localtime.tm_hour
    min = localtime.tm_min
    sec = localtime.tm_sec
    print(localtime)
    print("Hours:",hour)
    print("Minutes:",min)
    print("Seconds:",sec)


def set0(bulb):
        # set address of the tube cathode '0':
                                          #   ___
        GPIO.output(bulb[0],GPIO.LOW)     #  |   |
        GPIO.output(bulb[1],GPIO.LOW)     #  |   |
        GPIO.output(bulb[2],GPIO.LOW)     #  |   |
        GPIO.output(bulb[3],GPIO.LOW)     #  |___|


def set1(bulb):
        # set address of the tube cathode '1':
        GPIO.output(bulb[0],GPIO.HIGH)    #   /|
        GPIO.output(bulb[1],GPIO.LOW)     #  / |
        GPIO.output(bulb[2],GPIO.LOW)     #    |
        GPIO.output(bulb[3],GPIO.LOW)     #    |


def set2(bulb):
        # set address of the tube cathode '2':
                                          #   ___
        GPIO.output(bulb[0],GPIO.LOW)     #      |
        GPIO.output(bulb[1],GPIO.HIGH)    #   ___|
        GPIO.output(bulb[2],GPIO.LOW)     #  |
        GPIO.output(bulb[3],GPIO.LOW)     #  |___


def set3(bulb):
        # set address of the tube cathode '3':
                                          #   ___
        GPIO.output(bulb[0],GPIO.HIGH)    #      |
        GPIO.output(bulb[1],GPIO.HIGH)    #   ___|
        GPIO.output(bulb[2],GPIO.LOW)     #      |
        GPIO.output(bulb[3],GPIO.LOW)     #   ___|


def set4(bulb):
        # set address of the tube cathode '4':
        GPIO.output(bulb[0],GPIO.LOW)     #  |   |
        GPIO.output(bulb[1],GPIO.LOW)     #  |___|
        GPIO.output(bulb[2],GPIO.HIGH)    #      |
        GPIO.output(bulb[3],GPIO.LOW)     #      |


def set5(bulb):
        # set address of the tube cathode '5':
                                          #   ___
        GPIO.output(bulb[0],GPIO.HIGH)    #  |
        GPIO.output(bulb[1],GPIO.LOW)     #  |___
        GPIO.output(bulb[2],GPIO.HIGH)    #      |
        GPIO.output(bulb[3],GPIO.LOW)     #   ___|


def set6(bulb):
        # set address of the tube cathode '6':
                                          #   ___
        GPIO.output(bulb[0],GPIO.LOW)     #  |
        GPIO.output(bulb[1],GPIO.HIGH)    #  |___
        GPIO.output(bulb[2],GPIO.HIGH)    #  |   |
        GPIO.output(bulb[3],GPIO.LOW)     #  |___|


def set7(bulb):
        # set address of the tube cathode '7':
                                          #   ___
        GPIO.output(bulb[0],GPIO.HIGH)    #      |
        GPIO.output(bulb[1],GPIO.HIGH)    #      |
        GPIO.output(bulb[2],GPIO.HIGH)    #      |
        GPIO.output(bulb[3],GPIO.LOW)     #      |


def set8(bulb):
        # set address of the tube cathode '8':
                                          #   ___
        GPIO.output(bulb[0],GPIO.LOW)     #  |   |
        GPIO.output(bulb[1],GPIO.LOW)     #  |___|
        GPIO.output(bulb[2],GPIO.LOW)     #  |   |
        GPIO.output(bulb[3],GPIO.HIGH)    #  |___|


def set9(bulb):
        # set address of the tube cathode '9':
                                          #   ___
        GPIO.output(bulb[0],GPIO.HIGH)    #  |   |
        GPIO.output(bulb[1],GPIO.LOW)     #  |___|
        GPIO.output(bulb[2],GPIO.LOW)     #      |
        GPIO.output(bulb[3],GPIO.HIGH)    #   ___|


def setOff(bulb):
        # Set GPIO set to inputs so no display is made on the tube
                                     #
        GPIO.setup(bulb[0], GPIO.IN)
        GPIO.setup(bulb[1], GPIO.IN)
        GPIO.setup(bulb[2], GPIO.IN)
        GPIO.setup(bulb[3], GPIO.IN)
        print("Off")

def setOn(bulb):
        # Set GPIO set to outputs so display is enabled and made on the tube
                                     #
        GPIO.setup(bulb[0], GPIO.OUT)
        GPIO.setup(bulb[1], GPIO.OUT)
        GPIO.setup(bulb[2], GPIO.OUT)
        GPIO.setup(bulb[3], GPIO.OUT)
        print("On")

setOn(bulb1)
setOn(bulb2)
setOn(bulb3)
setOn(bulb4)
setOn(bulb5)
setOn(bulb6)
main()


