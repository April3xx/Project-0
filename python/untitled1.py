from __future__ import print_function
from __future__ import division
import platform
import numpy as np
import socket
import time
_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

m = []
count = 0
while(count < 240):
    m.append(count)
    m.append(0)  
    m.append(0)  
    m.append(0)
    count += 1 
    
m = bytes(m)
print(m)
while True:
    _sock.sendto(m,('192.168.43.62',7777))
    time.sleep(.1)