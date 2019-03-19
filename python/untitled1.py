# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 18:31:06 2018

@author: Window
"""

import numpy as np 
pixels = np.tile(1, (3, 250))
_prev_pixels = np.tile(253,(3,250))
pixels = np.clip(pixels, 0, 255).astype(int)
p=np.copy(pixels)
idx = (range(pixels.shape[1])) 
print(idx)
idx = [i for i in idx if not np.array_equal(p[:, i], _prev_pixels[:, i])]
n = len(idx) // 127
print(idx)
idx = np.array_split(idx,n) 
print(idx)