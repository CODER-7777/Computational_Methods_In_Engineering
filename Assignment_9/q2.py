import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0,1.1,0.1)
y_explicit=np.zeros(len(t))
y_implicit=np.zeros(len(t))
y_analytical=np.exp(-10*t)

y_explicit[0]=1.0
y_implicit[0]=1.0
h=0.1

for i in range(len(t)-1):
    y_explicit[i+1]=y_explicit[i]*(1-10*h)
    y_implicit[i+1]=y_implicit[i]/(1+10*h)

plt.figure(figsize=(10,6))
plt.plot(t,y_analytical,label='Analytical Solution',marker='o',linestyle='-')
plt.plot(t,y_explicit,label='Explicit Euler',marker='s',linestyle='--')
plt.plot(t,y_implicit,label='Implicit Euler',marker='^',linestyle='-.')

plt.title('Comparison of Analytical, Explicit, and Implicit Euler Methods')
plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.savefig("Q2_plot")
plt.show()
