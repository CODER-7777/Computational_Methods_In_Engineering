import numpy as np
def gauss_elimination_pivoting(A,b):
    n=len(b)
    Ab=np.zeros((n,n+1))
    Ab[:,:n]=A
    Ab[:,n]=b
    for k in range(n):
        max_row=k+np.argmax(np.abs(Ab[k:,k]))
        if max_row!=k:
            Ab[[k,max_row]]=Ab[[max_row,k]]
        for i in range(k+1,n):
            factor=Ab[i,k]/Ab[k,k]
            Ab[i,k:]=Ab[i,k:]-factor*Ab[k,k:]
    x=np.zeros(n)
    for i in range(n-1,-1,-1):
        x[i]=(Ab[i,n]-np.sum(Ab[i,i+1:n]*x[i+1:]))/Ab[i,i]
    return x

A=np.array([[2.0,-6.0,-1.0],[-3.0,-1.0,7.0],[-8.0,1.0,-2.0]])
b=np.array([-38.0,-34.0,-20.0])
roots=gauss_elimination_pivoting(A,b)
print("x1=",roots[0])
print("x2=",roots[1])
print("x3=",roots[2])