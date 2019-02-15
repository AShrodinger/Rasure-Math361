#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 11:36:16 2019

@author: AJRasure
"""

import numpy as np
import matplotlib.pyplot as plt

def eq1(x):
    y = -3 *(x +2)**2 +1
    return y

def eq2(x):
    y = 1
    return y

def eq3(x):
    y = (x-1)**3 +3
    return y
def eq4(x):
    y = np.sin(np.pi *x) + 3
    return y

def eq5(x):
    y = 3 * np.sqrt(x-2) +4
    return y

def main():
    
    leftBound = -3
    rightBound = 3
    yRange = []
    xDomain = []
    interval = 10
    
    for ii in range(leftBound,rightBound+1):
        nn = 0
        while nn < interval:
            ll = ii+nn/interval
            if ii < -2:
                yRange.append(eq1(ll))
            elif ii < -1:
                yRange.append(eq2(ll))
            elif ii <= 1:
                yRange.append(eq3(ll))
            elif ii < 2:
                yRange.append(eq4(ll))
            else:
                yRange.append(eq5(ll))
            
            xDomain.append(ll)
            nn +=1
            
    
#    print(yRange)
#    print(xDomain)

    plt.plot(xDomain,yRange)
    plt.xlabel('Domain')
    plt.ylabel('Range')
    plt.suptitle('Piecewise function with {} intervals between integrals'.format(interval), fontsize=16)
        
main()