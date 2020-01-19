import subprocess
import os
#from scapy.all import srp, Ether, ARP
hostname = "google.com" #example
jmac = "00:9D:6B:01:50:11"
dmac = "00:9D:6B:22:6A:BD"
zmac = "00:00:00:00:00:00"
jip = "192.168.1.65"

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
    else:
        print hostname, 'is down!'

online(jip)
print("done")

