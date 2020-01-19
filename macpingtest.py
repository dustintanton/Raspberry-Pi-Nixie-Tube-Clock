import subprocess
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#from scapy.all import srp, Ether, ARP
hostname = "google.com" #example
jmac = "00:9D:6B:01:50:11"
dmac = "00:9D:6B:22:6A:BD"
zmac = "00:00:00:00:00:00"
jeip = "192.168.1.65"
dtip = "192.168.1.84"
rrip = "192.168.1.64"
dpip = "192.168.1.62"
jpin = 3
rpin = 2
dpin = 4
dtpin = 17

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)


def mac_to_ip(mac):
    cmd = 'arp -a | findstr ' + mac + ' '
    returned_output = subprocess.check_output((cmd), shell=True, stderr=subprocess.STDOUT)
    print(returned_output)
    parse = str(returned_output).split(' ', 1)
    ip = parse[1].split(' ')
    print(ip[1])

def online(hostname):
    response = os.system("ping -c 1 " + hostname)
    #and then check the response...
    if response == 0:
        print hostname, 'is up!'
        return True
    else:
        print hostname, 'is down!'
        return False

def main():
    while (True):
        if (online(rrip)):                      #Ryan
            GPIO.output(rpin, GPIO.HIGH)
        else:
            GPIO.output(rpin, GPIO.Low)
        if (online(jeip)):                      #John
            GPIO.output(jpin, GPIO.HIGH)
        else:
            GPIO.output(jpin, GPIO.Low)
        if (online(dpip)):                      #David
            GPIO.output(dpin, GPIO.HIGH)
        else:
            GPIO.output(dpin, GPIO.Low)
        if (online(dtip)):                      #Dustin
            GPIO.output(dtpin, GPIO.HIGH)
        else:
            GPIO.output(dtpin, GPIO.Low)
        print("done")
        time.sleep(5)

