#%%

""" Newtons Method

itterative method 

starting point Z_o -> initial iterative (initital guess)
z_o ->z_1 -> z_2 ->...

Z_1 = Z_o - f(Z_o)/f'(Z_o)
Z_2 = Z_1 - f(Z_1)/f'(Z_1)
Z_n = Z_(n-1) - f(Z_(n-1))/f'(Z_(n-1))
|Z_(n+1) - Z_n | < Tolerance or stop after N times
"""
import math
import time
import numpy as np
tic = time.time()

r_n = lambda n: 1/100*(n**4+(math.e-2-math.sqrt(2))*n**3 +(2*math.sqrt(2) - math.e*math.sqrt(2)-3-2*math.e)*n**2 +(2*math.sqrt(2)*math.e + 3*math.sqrt(2) - 3*math.e)*n+ 3*math.e*math.sqrt(2))
t_n = lambda n: 1/100*(4*n**3+3*(math.e-2-math.sqrt(2))*n**2 + 2*(2*math.sqrt(2) - math.e*math.sqrt(2)-3-2*math.e)*n + (2*math.sqrt(2)*math.e + 3*math.sqrt(2) - 3*math.e))

TOL = 10**(-4)
tol = 2
inZ = 11
goal = 0
zList = np.zeros([0,2]) 

z = inZ
N = 1000
itter = 0
while tol > TOL and itter < N:
    newZ = z - r_n(z)/t_n(z)
    tol = abs(z-newZ)
    zList = np.vstack([zList,np.array([newZ,tol])])
    z = newZ
    itter += 1
    
print("List of itterations starting at {} until convergence within {} tolerance".format(inZ,TOL))
print(zList) 
if itter == 1000:
    print("Finished early")

"""-2.718,1.414, -1,3, """


    
#%%
"""
starting point Z_o -> initial iterative (initital guess)
z_o ->z_1 -> z_2 ->...

Z_1 = Z_o - f(Z_o)/f'(Z_o)
Z_2 = Z_1 - f(Z_1)/f'(Z_1)
Z_n = Z_(n-1) - f(Z_(n-1))/f'(Z_(n-1))
|Z_(n+1) - Z_n | < Tolerance or stop after N times
"""
import math
import time
import numpy as np
tic = time.time()

r_n = lambda n: math.tan(n)-n- 2
t_n = lambda n: 1/(math.cos(n)**2) - 1

TOL = 10**(-4)
tol = 2
inZ = math.pi/2
goal = 0
zList = np.zeros([0,2]) 

z = inZ
N = 1000
itter = 0
while tol > TOL and itter < N:
    newZ = z - r_n(z)/t_n(z)
    tol = abs(z-newZ)
    zList = np.vstack([zList,np.array([newZ,tol])])
    z = newZ
    itter += 1
    
print("List of itterations starting at {} until convergence within {} tolerance".format(inZ,TOL))
print(zList) 
if itter == 1000:
    print("Finished early")
""" pi/2, -pi/2"""