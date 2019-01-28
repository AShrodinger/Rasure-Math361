#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 11:03:30 2019

@author: AJRasure
"""
def greet():
    greeting = "hello world"
    
    print("Who are you? \n")
    who = input()
    
    print("\nWell then, {} and hello {}!!!".format(greeting,who))
greet()

