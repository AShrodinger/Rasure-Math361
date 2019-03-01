#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 12:47:17 2019

@author: AJRasure
"""

import numpy as np
import matplotlib.pyplot as plt

f_n = lambda n: n**3 + n**2 + n + 135
g_n = lambda n: n**5 


def main():
    z= 15
          #z must always be 1 more than the number of values you want as the first value will always be 1
          # the first 1 can be ignored as any number multiplied by 1 will return the number
          # and this is a product not summation.
          
    b= -.5

    divList = [1]
    bList = [1]
    for ii in range(1,z):

        divList.append((1.0+(f_n(ii)/(g_n(ii))))* divList[ii-1])
        bList.append((1.0 + b**ii) * bList[ii-1])

    listx = np.linspace(1,len(divList),len(divList))

    print()
    print("Here is a list of the first 15 terms in the 1st series: \n",divList[1:15])
    print()
    print("Here is a list of the last 15 terms in the 1st series: \n",divList[-15:])
    print()
    print("Here is a list of the first 15 terms in the 2nd series: \n",bList[1:15])
    print()
    print("Here is a list of the last 15 terms in the 2nd series: \n",bList[-15:])
    print()
    
    plt.plot(listx,bList)
#    plt.plot(listx,divList)
    plt.plot
    plt.show()
    
main()