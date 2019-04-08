
import time
import numpy as np

tic = time.time()

def prime_check(pCan):
    isPrime = True
    
    for ii in range (2,pCan):
        if pCan % ii == 0:
            isPrime = False
   
    return isPrime
    
p = 1
P = 200
countList = np.zeros([0,2])
neg_one = np.zeros([0,2])

for jj in range (p,P+1):
    
    if prime_check(jj):
        quads = []
        
        appears = "False"
        for ii in range (0,jj):
            num = (ii**2)%jj
            quads.append(num)
            
            if (jj - 1) == num:
                appears = "True"
                
        quads = set(quads)
        count = len(quads)
        countList = np.vstack([countList,np.array([jj,count])])
        neg_one = np.vstack([neg_one,np.array([jj,appears])])

print("What follows is the list of Quadratic Residues for between {} and {}".format(p,P))
print(countList)
print("What follows is the list between {} and {} and if the prime minus one is a quadratic residue".format(p,P))
print(neg_one)

#for ii in range (0,len(countList)):
#    print(countList[ii,1])
toc = time.time()

print("\nThe program took {:.4f} seconds to complete!!!".format(toc-tic))    
    