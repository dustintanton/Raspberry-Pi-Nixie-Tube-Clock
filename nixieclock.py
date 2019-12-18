import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time

a = 5
d = 6
b = 13
c = 19

A = 5
D = 6
B = 13
C = 19

BCD = [0000,0001,0010,0011,0100,0101,0110,0111,1000,1001]

pin = "" 
level = ""

#Setup my channels
GPIO.setup(a, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)

GPIO.output(a, GPIO.LOW)
GPIO.output(b, GPIO.LOW)
GPIO.output(c, GPIO.LOW)
GPIO.output(d, GPIO.LOW)

#find time and set first variables to time values
localtime = time.localtime(time.time())
hour = localtime.tm_hour
min = localtime.tm_min
sec = localtime.tv_sec






try:
	while True:
		# set address of the tube cathode '0':
                		            #   ___ 
		GPIO.output(A,GPIO.LOW)     #  |   |
		GPIO.output(B,GPIO.LOW)     #  |   |
		GPIO.output(C,GPIO.LOW)     #  |   |
		GPIO.output(D,GPIO.LOW)     #  |___|
		time.sleep(1)
		# set address of the tube cathode '1':
		GPIO.output(A,GPIO.HIGH)    #   /|  
		GPIO.output(B,GPIO.LOW)     #  / |
		GPIO.output(C,GPIO.LOW)     #    |
		GPIO.output(D,GPIO.LOW)     #    |
		time.sleep(1)
		# set address of the tube cathode '2':
		                            #   ___ 
		GPIO.output(A,GPIO.LOW)     #      |   
		GPIO.output(B,GPIO.HIGH)    #   ___|   
		GPIO.output(C,GPIO.LOW)     #  |  
		GPIO.output(D,GPIO.LOW)     #  |___
		time.sleep(1)
		# set address of the tube cathode '3':
		                            #   ___ 
		GPIO.output(A,GPIO.HIGH)    #      |   
		GPIO.output(B,GPIO.HIGH)    #   ___|   
		GPIO.output(C,GPIO.LOW)     #      |  
		GPIO.output(D,GPIO.LOW)     #   ___|
		time.sleep(1)
		# set address of the tube cathode '4':
		GPIO.output(A,GPIO.LOW)     #  |   | 
		GPIO.output(B,GPIO.LOW)     #  |___|   
		GPIO.output(C,GPIO.HIGH)    #      |  
		GPIO.output(D,GPIO.LOW)     #      |
		time.sleep(1)
		# set address of the tube cathode '5':
		                            #   ___ 
		GPIO.output(A,GPIO.HIGH)    #  |      
		GPIO.output(B,GPIO.LOW)     #  |___   
		GPIO.output(C,GPIO.HIGH)    #      |  
		GPIO.output(D,GPIO.LOW)     #   ___|
		time.sleep(1)
		# set address of the tube cathode '6':
		                            #   ___ 
		GPIO.output(A,GPIO.LOW)     #  |      
		GPIO.output(B,GPIO.HIGH)    #  |___   
		GPIO.output(C,GPIO.HIGH)    #  |   |  
		GPIO.output(D,GPIO.LOW)     #  |___|
		time.sleep(1)
		# set address of the tube cathode '7':
		                            #   ___
		GPIO.output(A,GPIO.HIGH)    #      |   
		GPIO.output(B,GPIO.HIGH)    #      |   
		GPIO.output(C,GPIO.HIGH)    #      |  
		GPIO.output(D,GPIO.LOW)     #      |
		time.sleep(1)
		# set address of the tube cathode '8':
		                            #   ___ 
		GPIO.output(A,GPIO.LOW)     #  |   |   
		GPIO.output(B,GPIO.LOW)     #  |___|   
		GPIO.output(C,GPIO.LOW)     #  |   |  
		GPIO.output(D,GPIO.HIGH)    #  |___|
		time.sleep(1)
		# set address of the tube cathode '9':
		                            #   ___ 
		GPIO.output(A,GPIO.HIGH)    #  |   |   
		GPIO.output(B,GPIO.LOW)     #  |___|   
		GPIO.output(C,GPIO.LOW)     #      |  
		GPIO.output(D,GPIO.HIGH)    #   ___|
		time.sleep(1)

finally:
	GPIO.cleanup()

