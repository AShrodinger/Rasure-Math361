#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:59:30 2019

@author: AJRasure
"""

#import numpy as np

# Variable names ---
# pCan -> Prime Candidate

#%%PRIME CHECK
# Checks to see if the prime value contendor is a multiple of any previous prime.
# If it is, then it is not prime.
# As 2 is the first prime, this eliminates a need for an even check
def prime_check(pCan):
    isPrime = True
    
    for ii in range (2,pCan):
        if pCan % ii == 0:
            isPrime = False
   
    return isPrime
              
#%% CREATE LIST OF PRIMES  
def pList(itter):
    primeList =[]
    
    #get primes
    #number of primes wanted
    check = 2 #first number to check
    
    while len(primeList) < itter:
        
        prime = False
        
        while prime == False:
            prime = (prime_check(check))
            check += 1
        
        primeList.append(check-1)
    return primeList

#%%
n = 13      
primeList = pList(n)

print("The {}th prime is {}.".format(n,primeList[-1]))