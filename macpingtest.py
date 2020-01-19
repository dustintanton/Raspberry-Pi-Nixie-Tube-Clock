import os
hostname = "google.com" #example
mac = ""

def online(hostname, mac)
    response = os.system("ping -c 1 " + hostname)
    #and then check the response...
    if response == 0:
        print hostname, 'is up!'
    else:
        print hostname, 'is down!'

online(hostname, mac)
print("done")