#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
"""Inverse of Z_m
Determine whitch elements of Z_m have a multiplicative inverse
"""
   
import time

tic = time.time()

m = 27 #Modulo
mOnes = [] #The set Z_m that are multiplicative inverses

for ii in range (0,m):
    for jj in range (1,m):
        if (ii *jj)%m == 1:
            mOnes.append(ii)
mOnes = set(mOnes)

print("The set of numbers that make up the zero devisor for mod {} is:\n{}".format(m,mOnes))
print("There are {} elements in the set".format(len(mOnes)))
toc = time.time()

print("\nThe program took {:.4f} seconds to complete!!!".format(toc-tic))