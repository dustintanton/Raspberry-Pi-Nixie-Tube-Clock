import os
from scapy.all import srp, Ether, ARP
hostname = "google.com" #example
jmac = "00:9D:6B:01:50:11"
dmac = "00:9D:6B:22:6A:BD"

def online(hostname, mac):
    response = os.system("ping -c 1 " + hostname)
    #and then check the response...
    if response == 0:
        print hostname, 'is up!'
    else:
        print hostname, 'is down!'

online(hostname, jmac)
print("done")