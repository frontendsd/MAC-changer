#!/usr/bin/python

import socket

from termcolor import colored
internet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(3)

host = input("-[#]- IP adressni kiting: ")
# port = int(input("-[#]- portni kiriting: "))

def portscaner(port):
    if internet.connect_ex((host, port)):
        print(colored("%d porti yopiq ekan" % (port), 'red'))
    else:
        print(colored("%d porti ochiq ekan" % (port), 'green'))
for port in range(1,100):
    portscaner(port)


