#%%%
""" Amicable Numbers
Write a program that does the following:
 Find all amicable numbers up to some upper bound N.
 Print out all amicable numbers found in your program.
"""
import time
tic = time.time()

def FindDivisor(num):
    divList = []
    for ii in range(1,num):
        if num%ii == 0:
            divList.append(ii)
    return divList

N = 2000
amicablePairs = []
nonAmicablePairs = []
for ii in range(1,N+1):   
    x = sum(FindDivisor(ii))   
    if ii == sum(FindDivisor(x)):
        pair = [ii,x]
        amicablePairs.append(pair)
    else:
        pair = [ii,x]
        nonAmicablePairs.append(pair)
        
print("The set of Amicable pairs is:\n",amicablePairs)
toc = time.time()
print("\nThe program took {:.4f} seconds to complete!!!".format(toc-tic)) 
    
    