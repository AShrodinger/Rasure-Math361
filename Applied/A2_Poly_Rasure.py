
"""Differintiate Polynomial"""

def dDx(px):
    dDx = []
    for ii in range(len(px)):
        dDx.append(px[ii]*ii)
    del dDx[0]
    return dDx

def integrate(px,a,b):
    iPx = [0]
    Pxa = []
    Pxb = []
    defPx = 0
    for ii in range(len(px)):
        iPx.append(px[ii]/(ii+1))
    for ii in range(len(iPx)):
        Pxa.append(iPx[ii]*a**ii)
        Pxb.append(iPx[ii]*b**ii)
        defPx = defPx + Pxb[ii] - Pxa[ii]
    
    return defPx

def evaluate(px,x):
    for ii in range(len(px)):
        px[ii] = px[ii]
    
    return sum(px)
    
p_x = [-9,2,0,-8,4] 
a = 2
b = 0




print("The function evaluated at {} is: {}.".format(a,evaluate(p_x,a)))
print("The derivative of the function evaluated at {} is: {}.".format(a,evaluate(dDx(p_x),a)))
print("the intergral of the function from {} to {} is: {}".format(b,a,integrate(p_x,b,a)))
