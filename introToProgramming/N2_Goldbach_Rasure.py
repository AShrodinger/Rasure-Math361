#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: AJRasure
"""

#%%
"""Goldbach 2
need prime nubers less than a number
need the square of numbers less than the number
"""

#PRIME CHECK
# Checks to see if the prime value contendor is a multiple of any previous prime.
# If it is, then it is not prime.
# As 2 is the first prime, this eliminates a need for an even check
import numpy as np
import time

def prime_check(pCan):
    isPrime = True
    
    for ii in range (2,pCan):
        if pCan % ii == 0:
            isPrime = False
   
    return isPrime
def Goldbach(num):           
    N = num
    Goldtrue = False
    for ii in range (1,N):
        if prime_check(ii):
            x = np.sqrt((N-ii)/2.0)
            if (x).is_integer():
                Goldtrue = True
                break

    return Goldtrue

tic = time.time()    

truth = True
low = 1
high = 1000000


for ii in range(low,high):
    if prime_check(ii)==False and ii%2 == 1:
        if Goldbach(ii) == False:
            print("\nAt {}, the second Goldbach Conjecture is False.".format(ii))
            break
        else:
            print('Goldbach holds for {}.'.format(ii))

toc = time.time()

print("\nProgram took {:.4f} seconds to complete!!!".format(toc-tic))