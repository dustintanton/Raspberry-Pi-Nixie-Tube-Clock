import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time

a = 5
d = 6
b = 13
c = 19

pin = ""
level = ""

#Setup my channels
GPIO.setup(a, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)

GPIO.output(a, GPIO.HIGH)
GPIO.output(b, GPIO.LOW)
GPIO.output(c, GPIO.LOW)
GPIO.output(d, GPIO.LOW)

try:
	while True:
		pin = input("What channel? A,B,C,D?:")
		level = raw_input("what level?:")
		level = level.upper()
		print(level)
		GPIO.output(pin,level)
finally:
	GPIO.cleanup()

