#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 12:25:42 2019

@author: AJRasure
"""


    
f = lambda x: x**2 - 9*x + 2
    
def main():
    a = 2
    b = 5
    
    print("\n", my_func(a,b))
    
    print("\n" ,f(0))

main()

def my_func(param1, param2):
    x= param1**2
    y = 2*param2 + 9
    if (x > y):
        return True
    else:
        return False
