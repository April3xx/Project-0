from __future__ import print_function
from __future__ import division
import platform
import numpy as np
import socket
import time
_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#p = np.tile(1, (3, 240))
#print(p)
m=[]
#เริ่มที่ E บาร์ล่าง กลาง บน เเล้วค่อยเส้นตั้ง  
ite =[100,101,102,
      139,138,137,
      160,161,162,
      117,122,142,157,
      163,164,165,
      104,115,124,135,144,155,
      166,167,168,
      106,107,108,
      127,147,112,127,132,152]
for i in ite:
    m.append(i)  
    m.append(0)  
    m.append(255)  
    m.append(0)
print(m)
#print(p)
m = bytes(m)
while True:
    _sock.sendto(m,('172.20.10.5',7777))
    
    time.sleep(.1)