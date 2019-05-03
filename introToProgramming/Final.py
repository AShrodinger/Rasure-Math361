#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:43:36 2019

@author: AJRasure
"""

#%%

import math
import time
tic = time.time()

reflec = 12017639147
row = (reflec + 3)/2
#param = []
total = 0
if reflec == 1:
    total = 1
elif row%3 == 0:
    total = 0
elif (row).is_integer():
    row = int(row)
    col = 1 +(row)%3
    print(row,col)
    while (row+1)//2 >= col:
       if math.gcd(row,col) == 1:
          total += 1
#          param.append([row,col])
       col += 3

       if col%1000000 == 0:
          toc = time.time()
          print("{:.4f}% in {:.4f} seconds".format(col/(row//2)*100,toc-tic))
          

print ("Total number that reflect {} times is: {}".format(reflec,total * 2))


toc = time.time()

print("\nThe program took {:.4f} seconds to complete!!!".format(toc-tic)) 