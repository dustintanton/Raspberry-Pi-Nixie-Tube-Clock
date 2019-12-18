import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time

sense = 20
relay = 21

#Setup my channel
GPIO.setup(sense, GPIO.IN)
GPIO.setup(relay, GPIO.OUT)

x = 6
while True:
	#To test the value of a pin use the .input method
	channelON = GPIO.input(sense) #returns 0 if OFF or 1 if ON
	print(GPIO.input(sense))
	if channelON:
		GPIO.output(relay,0)
		time.sleep(1)
	else:
		GPIO.output(relay,1)
	time.sleep(1)

