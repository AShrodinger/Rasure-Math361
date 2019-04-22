
def Coef(r,gx):
    coRet =[]
    for ii in range(len(r)-len(gx)+1):
        coRet.append(0)
    coRet[-1] = r[-1]/gx[-1]    
    return coRet

def PolyMult(outer,inner):
    nx = []
    for ii in range(len(inner)+len(outer)-1):
        nx.append(0)
    for ii in range(1,len(inner)+1):
        nx[-ii] = outer[-1]*inner[-ii]
    return nx
 
def PolySub(fx,gx):
    nx = []
    for ii in range(len(fx)):
        nx.append(0)
    for ii in range(len(gx)):
        nx[ii] = fx[ii]-gx[ii]
    return nx

f_x = [5,-11,-7,4] #polynomial to be divided (eg. [1,2,3] = 1+2x+3x^2)
g_x = [5,4]     #dividing polynomial #polynomial to be divided (eg. [0,2] = 2x)
#creates quotient list based on fx
q=[]
r = list(f_x)
for ii in range(len(f_x)):
    q.append(0)
degree = len(r)-len(g_x)
while degree > -1:
    r2 = PolyMult(Coef(list(r),list(g_x)),list(g_x))
    q[degree] = q[degree] + Coef(list(r),list(g_x))[-1]
    r = PolySub(r,r2)
    
    del r[-1]
    degree = len(r)-len(g_x)

print("Through polynomial division:")   
for ii in range(len(f_x)):
    if ii == 0:      
        print("({})".format(f_x[ii]), end="")    
    elif f_x[ii] != 0:
        print("+({})x^{}".format(f_x[ii],ii), end="")
print()
print("divided by")
for ii in range(len(g_x)):
    if ii == 0:      
        print("({})".format(g_x[ii]), end="")    
    elif g_x[ii] != 0:
        print("+({})x^{}".format(g_x[ii],ii), end="")
print()
print("is")
for ii in range(len(q)):
    if ii == 0:      
        print("[({:.4})".format(q[ii]), end="")    
    elif q[ii] != 0:
        print("+({:.4f})x^{}".format(q[ii],ii), end="")
print("]",end ="")
for ii in range(len(r)):
    if ii == 0:
        print("+[({:.4f})".format(r[ii]), end="")    
    elif r[ii] != 0:
        print("+({:.4f})x^{}".format(r[ii],ii), end="")
print("]")        
         