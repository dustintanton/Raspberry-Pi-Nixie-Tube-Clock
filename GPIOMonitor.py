import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

def main():

        while True:
                x=1
                while x<27:
                        GPIO.setup(x, GPIO.IN)
                        print "Pin ", x, " Value ", GPIO.input(x)
                        x=x+1
                print "--------------------------------------------------------"
                time.sleep(1)
                os.system("clear")
                time.sleep(.1)
                
main()
