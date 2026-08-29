import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp((x-1)**2)-1

def df(x):
    return 2*(x-1)*np.exp((x-1)**2)

def ddf(x):
    return 2*np.exp((x-1)**2)*(1+2*(x-1)**2)

def u_vec(x):
    val=np.zeros_like(x)
    mask=np.abs(x-1)>1e-12
    val[mask]=f(x[mask])/df(x[mask])
    val[~mask]=0.0
    return val

def u(x):
    if abs(x-1.0)<1e-12: return 0.0
    return (1-np.exp(-(x-1)**2))/(2*(x-1))

def du_vec(x):
    val=np.zeros_like(x)
    mask=np.abs(x-1)>1e-12
    val[mask]=1-(f(x[mask])*ddf(x[mask]))/(df(x[mask])**2)
    val[~mask]=0.5
    return val

x_vals=np.linspace(0,2,400)


plt.figure()
plt.plot(x_vals,f(x_vals),label="f(x)",color='C0')
plt.axhline(0,color='black',linewidth=0.8,linestyle='--')
plt.title("f(x)")
plt.legend()
plt.grid(True)
plt.savefig("f_plot.png")
plt.close()

plt.figure()
plt.plot(x_vals,df(x_vals),label="f'(x)",color='C1')
plt.axhline(0,color='black',linewidth=0.8,linestyle='--')
plt.title("f'(x)")
plt.legend()
plt.grid(True)
plt.savefig("df_plot.png")
plt.close()

plt.figure()
plt.plot(x_vals,ddf(x_vals),label="f''(x)",color='C2')
plt.axhline(0,color='black',linewidth=0.8,linestyle='--')
plt.title("f''(x)")
plt.legend()
plt.grid(True)
plt.savefig("ddf_plot.png")
plt.close()
print("saved individual plots.\n")


plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(x_vals,f(x_vals),label="f(x)")
plt.plot(x_vals,df(x_vals),label="f'(x)")
plt.plot(x_vals,ddf(x_vals),label="f''(x)")
plt.axhline(0,color='black',linewidth=0.8,linestyle='--')
plt.title("Part(a):f(x) and derivatives")
plt.legend()
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(x_vals,u_vec(x_vals),label="u(x)")
plt.plot(x_vals,du_vec(x_vals),label="u'(x)")
plt.axhline(0,color='black',linewidth=0.8,linestyle='--')
plt.title("Part(b):u(x) and u'(x)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("q1_plots.png")
print("saved q1_plots.\n")

def secant_method(func,x_prev,x_curr,tol=1e-6,max_iter=100):
    for i in range(1,max_iter+1):
        f_curr=func(x_curr)
        f_prev=func(x_prev)
        if abs(f_curr-f_prev)<1e-14:
            return x_curr,i,False
        x_new=x_curr-f_curr*((x_curr-x_prev)/(f_curr-f_prev))
        if abs(x_new-x_curr)<tol:
            return x_new,i,True
        x_prev=x_curr
        x_curr=x_new
    return x_curr,max_iter,False

print("-Results-")
root_std,iter_std,conv_std=secant_method(f,-0.5,0.0)
print(f"Standard Secant: root={root_std:.6f}, iterations={iter_std}, converged={conv_std}")

root_mod,iter_mod,conv_mod=secant_method(u,-0.5,0.0)
if conv_mod:
    print(f"Modified Secant: root={root_mod:.6f}, iterations={iter_mod}")
else:
    print(f"Modified Secant: DID NOT CONVERGE (ran {iter_mod} iterations, drifted to x={root_mod:.3e})")

plt.show()