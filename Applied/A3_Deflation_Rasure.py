#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:44:57 2019

@author: AJRasure
"""


""" Division Algorithm

Input: fx,gx
Output: quotient and remeinder (q,r)

q = 0, r = fx

(LT = leading term)
while r !=0 and LT(g) divides LT(f) do
    q = q + LT(r)/LT(gx)
    r = r - (LT(r)/LT(gx))*gx
"""
#coefficient from LT(fx)/LT(gx)
def coef(r,gx):
    return r[-1]/gx[-1]


fx = [3,-1,0,0,0,-5,0,5] #polynomial to be divided (eg. [1,2,3] = 1+2x+3x^2)
gx = [0,1,0,0,3]     #dividing polynomial #polynomial to be divided (eg. [0,2] = 2x)
#creates quotient list based on fx

q=[]
for ii in range(len(fx)):
    q.append(0)

r = fx
  
degree = len(r)-len(gx) #exponent of LT(fx)/LT(gx)
 
while degree>0:
#for jj in range(1):
    
    # Where the next r = r - LT(fx)/LT(gx)*gx r2 = LT(fx)/LT(gx)*gx r2
    #establishes r2
    r2 = []   
    for ii in range(len(r)): #degree of r2
        r2.append(0)
            
    for ii in range(-1,-len(gx),-1): #coefficients of r2   
        r2[ii] = coef(r,gx)*gx[ii]
    #        
    q[degree] = q[degree] + coef(r,gx) #places the proper coefficient into the appropriate degreed space in the list
    
    #creates the next r where r(next) = r(current)-r2
    for ii in range(-1,-len(r2)-1,-1):
        r[ii] = r[ii] -r2[ii]        
    del r[-1] #removes final 0 from list, 0x^n that will equal zero
    
    degree = len(r)-len(gx)

if degree == 0:  

    r2 = []
    for ii in range(degree+1):
        r2 = list(gx)
    for ii in range(0,len(r2)):
        r2[ii] = coef(r,gx)*r2[ii]
    q[degree] = q[degree] + coef(r,gx)
    for ii in range(-1,-len(r2)-1,-1):
        r[ii] = r[ii] - r2[ii]
    del r[-1]

 # Where the next r = r - LT(fx)/LT(gx)*gx r2 = LT(fx)/LT(gx)*gx r2
    #establishes r2
#r2 = []   
#for ii in range(degree+1): #degree of r2
#    r2.append(0)
#    
#for ii in range(-1,-len(gx),-1): #coefficients of r2   
#    r2[ii] = coef(r,gx)*gx[ii]
#    
#q[degree] = q[degree] + coef(r,gx) #places the proper coefficient into the appropriate degreed space in the list
#
##creates the next r where r(next) = r(current)-r2
#for ii in range(-1,-len(r2)-1,-1):
#    r[ii] = r[ii] -r2[ii]        
#del r[-1] #removes final 0 from list, 0x^n that will equal zero
#
#degree = len(r)-len(gx)
print(q,r)

