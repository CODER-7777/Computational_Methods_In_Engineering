import numpy as np

def Q(t):
    return 8+5*(np.cos(0.4*t))**2
def c(t):
    return 5*np.exp(-0.5*t)+3*np.exp(0.15*t)
def f(t):
    return Q(t)*c(t)

a=2
b=8
tol=0.1
R=np.zeros((10,10))
h=b-a
R[0,0]=(h/2)*(f(a)+f(b))

for i in range(1,10):
    h=(b-a)/(2**i)
    sum_new=0
    for k in range(1,2**i,2):
        sum_new+=f(a+k*h)
    
    R[i,0]=0.5*R[i-1,0]+h*sum_new
    
    for j in range(1,i+1):
        R[i,j]=R[i,j-1]+(R[i,j-1]-R[i-1,j-1])/(4**j-1)
        
    ea=abs((R[i,i]-R[i,i-1])/R[i,i])*100
    
    if ea<tol:
        print(f"Final={R[i,i]}")
        break