# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:12:40 2019

@author: Window
"""
from numpy import arange , linspace , zeros

a = 0 + 500 * arange(0,26)
b = a[1:-1]
c =a[:-2]
d = a [2:] 
e = linspace(0.0, 16000 / 2.0, 513)
f = zeros((24, 513))
g = set(zip(b, c, d))
print('A :')
print(a)
print('b :')
print(b)
print('c :')
print(c)
print('d :')
print(d)
print('e :')
print(e)
print(e.size)
print('f :')
print(f)
print('g :')
print(g)