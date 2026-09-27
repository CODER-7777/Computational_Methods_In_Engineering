import numpy as np
import matplotlib.pyplot as plt
T=np.array([0,8,16,24,32,40],dtype=float)
O=np.array([14.621,11.843,9.870,8.418,7.305,6.413],dtype=float)
n=len(T)
def newton_divided_difference(x,y):
    n=len(y)
    coef=np.zeros([n,n])
    coef[:,0]=y
    for j in range(1,n):
        for i in range(n-j):
            coef[i,j]=(coef[i+1,j-1]-coef[i,j-1])/(x[i+j]-x[i])
    return coef[0,:]
newton_coeffs=newton_divided_difference(T,O)
def evaluate_newton(x_data,coeffs,x_val):
    result=coeffs[0]
    product_term=1.0
    for i in range(1,len(coeffs)):
        product_term*=(x_val-x_data[i-1])
        result+=coeffs[i]*product_term
    return result
A=np.zeros((15,15))
b=np.zeros(15)
A[0,2]=1
b[0]=O[0]
A[1,0:3]=[T[1]**2,T[1],1]
b[1]=O[1]
A[2,3:6]=[T[1]**2,T[1],1]
b[2]=O[1]
A[3,3:6]=[T[2]**2,T[2],1]
b[3]=O[2]
A[4,6:9]=[T[2]**2,T[2],1]
b[4]=O[2]
A[5,6:9]=[T[3]**2,T[3],1]
b[5]=O[3]
A[6,9:12]=[T[3]**2,T[3],1]
b[6]=O[3]
A[7,9:12]=[T[4]**2,T[4],1]
b[7]=O[4]
A[8,12:15]=[T[4]**2,T[4],1]
b[8]=O[4]
A[9,12:15]=[T[5]**2,T[5],1]
b[9]=O[5]
A[10,0:2]=[2*T[1],1]
A[10,3:5]=[-2*T[1],-1]
A[11,3:5]=[2*T[2],1]
A[11,6:8]=[-2*T[2],-1]
A[12,6:8]=[2*T[3],1]
A[12,9:11]=[-2*T[3],-1]
A[13,9:11]=[2*T[4],1]
A[13,12:14]=[-2*T[4],-1]
A[14,0]=1
def gauss_elimination(mat,vec):
    M=np.hstack([mat,vec.reshape(-1,1)])
    num_eqs=len(vec)
    for i in range(num_eqs):
        max_row=np.argmax(abs(M[i:,i]))+i
        M[[i,max_row]]=M[[max_row,i]]
        for j in range(i+1,num_eqs):
            factor=M[j,i]/M[i,i]
            M[j,i:]=M[j,i:]-factor*M[i,i:]
    x=np.zeros(num_eqs)
    for i in range(num_eqs-1,-1,-1):
        x[i]=(M[i,-1]-np.dot(M[i,i+1:num_eqs],x[i+1:]))/M[i,i]
    return x
spline_coeffs=gauss_elimination(A,b)
def evaluate_splines(coeffs,x_vals,T_knots):
    y_vals=np.zeros_like(x_vals)
    for i,x in enumerate(x_vals):
        for j in range(5):
            if T_knots[j]<=x<=T_knots[j+1]:
                a,b,c=coeffs[j*3],coeffs[j*3+1],coeffs[j*3+2]
                y_vals[i]=a*(x**2)+b*x+c
                break
    return y_vals
x_plot=np.linspace(0,40,500)
y_newton=[evaluate_newton(T,newton_coeffs,x) for x in x_plot]
y_spline=evaluate_splines(spline_coeffs,x_plot,T)
plt.figure(figsize=(10,6))
plt.scatter(T,O,color='black',zorder=5,s=50)
plt.plot(x_plot,y_newton,'b--')
plt.plot(x_plot,y_spline,'r-')
plt.xlim(0,40)
plt.savefig("q1_plot.png")
plt.show()