#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:25:23 2019

@author: AJRasure

Calculator.py
"""
def Calculator():
    #initial variable values
    x = 1
    y = 1
    z = 1
    
    #Create List of 5 components
    component = [x+y, (y*z)+(3*x)]
    component.append(component[0]**2)
    component.append((2*component[1]-(x/2))/component[0])
    component.append(7%3)
    
    #add 3 to the third component
    component[2] = (component[2] + 3)
    
    #multiply the last component by 3/4
    component[4] = component[4]*(3/4)
    
    #print sum of components
    summation = 0
    for i in range (0,5):
        summation = summation + component[i]
    print("The sum of all components is: ", summation)

Calculator()