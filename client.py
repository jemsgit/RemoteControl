# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('192.168.0.47', 9092))

sock.send('pm-suspend')

data = sock.recv(1024)
sock.close()

print data
