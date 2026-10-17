import numpy as np
import matplotlib.pyplot as plt

def f1(t,y1,y2):
    return y2

def f2(t,y1,y2,c):
    m=20.0
    k=20.0
    return -(k/m)*y1-(c/m)*y2

def rk4_system(c,h,t_end):
    t=np.arange(0,t_end+h,h)
    n=len(t)
    
    y1=np.zeros(n)
    y2=np.zeros(n)
    
    y1[0]=1.0
    y2[0]=0.0
    
    for i in range(n-1):
        k11=h*f1(t[i],y1[i],y2[i])
        k12=h*f2(t[i],y1[i],y2[i],c)
        
        k21=h*f1(t[i]+h/2,y1[i]+k11/2,y2[i]+k12/2)
        k22=h*f2(t[i]+h/2,y1[i]+k11/2,y2[i]+k12/2,c)
        
        k31=h*f1(t[i]+h/2,y1[i]+k21/2,y2[i]+k22/2)
        k32=h*f2(t[i]+h/2,y1[i]+k21/2,y2[i]+k22/2,c)
        
        k41=h*f1(t[i]+h,y1[i]+k31,y2[i]+k32)
        k42=h*f2(t[i]+h,y1[i]+k31,y2[i]+k32,c)
        
        y1[i+1]=y1[i]+(k11+2*k21+2*k31+k41)/6.0
        y2[i+1]=y2[i]+(k12+2*k22+2*k32+k42)/6.0
        
    return t,y1

c_values=[5,40,60]
t_end=15
h=1.0

plt.figure(figsize=(10,6))

for c in c_values:
    t_vals,x_vals=rk4_system(c,h,t_end)
    plt.plot(t_vals,x_vals,marker='o',label=f'c={c} Ns/m')

plt.title('Displacement of Damped Spring-Mass System (RK4)')
plt.xlabel('Time (s)')
plt.ylabel('Displacement x (m)')
plt.grid(True)
plt.legend()
plt.savefig('Q1_plot')
plt.show()
