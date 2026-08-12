import numpy as np
import matplotlib.pyplot as plt
T=1.0

t1=np.linspace(1e-5,(T/2)-1e-5,500)
t2=np.linspace((T/2)+1e-5,T-1e-5,500)

k1=np.abs((2*np.pi*t1/T)*(np.cos(2*np.pi*t1/T)/np.sin(2*np.pi*t1/T)))
k2=np.abs((2*np.pi*t2/T)*(np.cos(2*np.pi*t2/T)/np.sin(2*np.pi*t2/T)))

plt.figure(figsize=(8,5))
plt.plot(t1,k1,color='blue',linewidth=2)
plt.plot(t2,k2,color='blue',linewidth=2)

plt.axvline(x=T/2,color='red',linestyle='--',label='Asymptote at t=T/2')
plt.axvline(x=T,color='red',linestyle='--',label='Asymptote at t=T')

plt.title('Condition Number of $y(t)= \sin(2\pi t/T)$')
plt.xlabel('Time $t$')
plt.ylabel('Condition Number $\kappa(t)$')


plt.ylim(0,20)
plt.xlim(0*T,1.05*T)
# plt.xticks([0,T/4,T/2,3*T/4,T],['0','T/4','T/2','3T/4','T'])
plt.grid(True)
plt.legend()
plt.savefig('condition_number_plot.png',dpi=300,bbox_inches='tight') # I used this to just to save the image
plt.show()
    
