#%%
""" Find Divisors
Write a program that does the following:
• Write a def function that takes an integer n as input, and returns a list containing all the proper divisors of n.
• Using this function, print out all proper divisors of some number.

"""

def FindDivisor(num):
    divList = []
    for ii in range(num):
        if num%ii == 0:
            divList.append(ii)
    return divList
    
