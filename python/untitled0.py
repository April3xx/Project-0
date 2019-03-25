from __future__ import print_function
from __future__ import division
import platform
import numpy as np
import socket
import time
_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 while True:
        _sock.sendto(m, ('172.20.10.5', 7777 ))
        
        time.sleep(.1)
