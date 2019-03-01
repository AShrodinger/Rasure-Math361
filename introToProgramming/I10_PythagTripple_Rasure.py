#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:31:47 2019

@author: AJRasure
"""


#%%
""" Pythagorean Tripple
Finds the first time a specific sum of a, b, and c is achieved when looking at
Pythagorean Tripples.
"""
#import
import numpy as np
#initialize variables

my_array = np.zeros([0,4])
my_array = np.vstack([my_array, np.array(["a","b","c","a+b+c"])])

tripA = 0
tripB = 0
tripC = 0
tripSum = 0
goalSum = 1026
checkSum = 2000

while tripSum <= checkSum:
    for ii in range(1,tripB):
        tripC = np.sqrt(ii**2 + tripB**2)
        tripSum = ii +tripB + tripC
        if (tripC.is_integer() == True):
            tripA = ii            
            my_array = np.vstack([my_array, np.array([tripA,tripB,tripC,tripSum])])
        if tripSum == goalSum:
            break
    if tripSum == goalSum:
        break 
    
#for ii in range (8):
#    my_array = np.vstack([my_array,np.array([4*ii, 4*ii+1, 4*ii+2, 4*ii+3])])
print("The first Pythagorean Triple that sums to {} is:".format(goalSum))
print("a = {}, b = {}, and c = {}".format(my_array[-1,0], my_array[-1,1], my_array[-1,2]))

