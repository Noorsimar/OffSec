#!/usr/bin/python

# Knock to ports 3\2\1 on host

import socket
import time

host = '192.168.1.10'

def connection(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
    except:
        sock.close()

i = 3

while i > 0:
    connection(i)
    time.sleep(1)
    i -= 1