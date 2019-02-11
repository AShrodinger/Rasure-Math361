#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: AJRasure
"""
#imports
import numpy as np
import matplotlib.pyplot as plt
import math

#variable initiation
def main():
    z = 1000
    
    acumS = np.array([])
    acumT = np.array([])
    acumR = np.array([])
    summed = 0
    #calc sn
    for ii in range(1,z):
        ii += 0.0
        formS = np.log(ii**4 + ii + 3)/(np.sqrt(ii+3))
        summed += formS
        acumS = np.append(acumS, summed)
    
    #calc tn
    summed = 0
    for ii in range(1,z):
        ii += 0.0
        formT = (np.exp(ii/100)/(ii**10))
        summed += formT
        acumT = np.append(acumT, summed)
    summed = 0    
    for ii in range(1,z):
        formR = ((-1)**ii*90**(2*ii + 1))/(math.factorial(2 * ii + 1))
        summed += formR
        acumR = np.append(acumR, summed)
        
    

    print("Running each of the series for {:} terms: " .format(z))
    print()
    print()
    print("Series 1:")
    print("Here is a list of the first 15 terms in the series: \n",acumS[:15])
    print()
    print("Here is a list of the last 15 terms in the series: \n",acumS[-15:])
    print()
    listx = []
    for ii in range (1, z):
        listx.append(ii)
    
    x = listx
    y = acumS
    
    plt.plot(x,y)
    plt.show()
    
    print()
    print()
    print("Series 2:")
    print("Here is a list of the first 15 terms in the series: \n",acumT[:15])
    print()
    print("Here is a list of the last 15 terms in the series: \n",acumT[-15:])
    print()
    listx = []
    for ii in range (1, z):
        listx.append(ii)
    
    x = listx
    y = acumT
    plt.ylim(0,2)
    plt.plot(x,y)
    plt.show()

    
    print()
    print()
    print("Series 3:")
    print("Here is a list of the first 15 terms in the series: \n",acumR[:15])
    print()
    print("Here is a list of the last 15 terms in the series: \n",acumR[-15:])
    print()
    listx = []
    for ii in range (1, z):
        listx.append(ii)
    
    x = listx
    y = acumR
    plt.plot(x,y)
    plt.show()
    
main()


    
    
    