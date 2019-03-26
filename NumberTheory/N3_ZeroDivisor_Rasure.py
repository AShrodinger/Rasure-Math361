#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Zero Divisor
Determine what elements of Z_m are zero divisors
"""
import time
import numpy as np

tic = time.time()

m = 27 #Modulo
mZeros = [] #The set Z_m that are zero divisors

for ii in range (0,m):
    for jj in range (1,m):
        if (ii *jj)%m == 0:
            mZeros.append(ii)
mZeros = set(mZeros)
print("The set of numbers that make up the zero devisor for mod{} is:\n{}".format(m,mZeros))
print("There are {} elements in the set".format(len(mZeros)))


toc = time.time()
print("\nThe program took {:.4f} seconds to complete!!!".format(toc-tic)) 