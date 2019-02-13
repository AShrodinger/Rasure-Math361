#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 11:31:37 2019

@author: AJRasure
"""
#imports



def main():
    #initialize variables   
    z = 20 #terms to run
    fiboSeq = [0,3]
    proof = True
    
    #create terms
    for ii in range(2,z):
        fiboSeq.append(fiboSeq[ii-2]+fiboSeq[ii-1])
        
    #Cassini's Identity
    for ii in range(1,z-1):
        cassIdent = fiboSeq[ii]**2 - fiboSeq[ii-1]*fiboSeq[ii+1]
        if cassIdent != (-1)**(ii-1)*9:
            print("NOT THE FIBONACCI SEQUENCE!!!")
            proof = False
            break
        
    if proof:    
        print("Here are the last 10 terms ({} through {}) of the Fibonacci sequence if it is run for {} terms: ".format(z-10, z, z))
        print(fiboSeq[-10:])
    else:
        print("STILL NOT THE FIBONACCI SEQUENCE!!!")
    print(fiboSeq)
main()
   