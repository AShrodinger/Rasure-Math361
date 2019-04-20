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
print(row)
#param = []
if (row).is_integer():
    row = int(row)

    offset =1 + (row %3)
    print("offset",offset)
    col = int(offset)

#    row -= int(offset)
#    param.append([row,col])
    print(row,col)
    
    total = 0
    while row//2 > col:
       if math.gcd(row,col) == 1:
          total += 1
#          param.append([row,col])

       col += 3
#       param.append([row,col])
       #Print statment below is for diplaying progress.
       if col%1000000 == 0:
          toc = time.time()
          print("{:.4f}% in {:.4f} seconds".format(col/(row//2)*100,toc-tic))

    print ("total number that reflect {} times is: {}".format(reflec,total * 2))
      
elif surf == 2:
    total = 1

else:
    print("total number that reflect {} times is: 0".format(reflec))

toc = time.time()

print("\nThe program took {:.4f} seconds to complete!!!".format(toc-tic)) 