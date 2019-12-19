import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# Time Variables Instances
localtime = time.localtime(time.time())
hour = localtime.tm_hour
min = localtime.tm_min
sec = localtime.tm_sec

# 2nd digit seconds bulb
bulb6 = ['a', 'b', 'c', 'd']
a = 5
d = 6
b = 13
c = 19

BCD = [0000,0001,0010,0011,0100,0101,0110,0111,1000,1001]

# Set bulbs and refresh variables

setOn(bulb6)
findTime()

def Time(bulb6):
	# 6th bulb time function
	findFunctionNumber(sec % 10, bulb6)


def findFunctionNumber(x,bulb):
	FunctionNumber = [ "set0()","set1()","set2()","set3()","set4()","set5()","set6()","set7()","set8()","set9()" ]
	if(x = 0)
		set0(bulb)

	if (x = 1)
		set1(bulb)

	if (x = 2)
		set2(bulb)

	if (x = 3)
		set3(bulb)

	if (x = 4)
		set4(bulb)

	if (x = 5)
		set5(bulb)

	if (x = 6)
		set6(bulb)

	if (x = 7)
		set7(bulb)

	if (x = 8)
		set8(bulb)

	if (x = 9)
		set9(bulb)

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


def setOn(bulb):
		# Set GPIO set to outputs so display is enabled and made on the tube
									 #
		GPIO.setup(bulb[0], GPIO.OUT)
		GPIO.setup(bulb[1], GPIO.OUT)
		GPIO.setup(bulb[2], GPIO.OUT)
		GPIO.setup(bulb[3], GPIO.OUT)


