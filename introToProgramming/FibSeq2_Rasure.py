#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:42:34 2019

@author: AJRasure
"""

def main():
    #initialize variables   
    z = 10000 #terms to run
    m = 25
    fiboSeq = [0,1]
#    divList = []
    percList =[]
#    intList = list(range(1,m+1))
    #create terms
    for ii in range(2,z):
        fiboSeq.append(fiboSeq[ii-2]+fiboSeq[ii-1])
    for nn in range(1,m+1): 
        divList = []
        for ii in range(0,z):
            if fiboSeq[ii]%nn == 0:
                divList.append(fiboSeq[ii])
        perc = len(divList)/len(fiboSeq)*100
        percList.append(perc)
        
#    print(divList)
#    perc = len(divList)/len(fiboSeq)*100
#    print(len(fiboSeq))
#    print(len(divList))
#    print()
    print("The percentage of the first {} terms of the Fibonacci Sequence divisible by {} is: {:0.2f}%".format(z,m,(len(divList)/len(fiboSeq)*100)))
#    for ii in range(0,len(intList)):
#        print("{} -> {}".format(intList[ii],percList[ii]))
#       print(intList)
    
main()