import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('assignment6(Sheet1).csv')
y=df['Annual flow (ac-ft/year)'].values
T=len(y)
t=np.arange(1,T+1)
k_max=T//2
ak=np.zeros(k_max)
bk=np.zeros(k_max)
power=np.zeros(k_max)
a0=np.sum(y)/T
print(f"a0={a0:.2f}")
for k in range(1,k_max+1):
    angle=2*np.pi*k*t/T
    ak[k-1]=(2/T)*np.sum(y*np.cos(angle))
    bk[k-1]=(2/T)*np.sum(y*np.sin(angle))
    power[k-1]=ak[k-1]**2+bk[k-1]**2
top_indices=np.argsort(power)[::-1][:3]
for i,idx in enumerate(top_indices):
    k_val=idx+1
    freq=k_val/T
    print(f"Rank {i+1}: k={k_val}, Frequency={freq:.4f}, Power={power[idx]:.2e}")
freq_array=np.arange(1,k_max+1)/T
plt.figure(figsize=(10,5))
plt.plot(freq_array,power,marker='o',linestyle='-',color='b')
plt.title('Power vs Frequency')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.grid(True)
plt.savefig('q2_plot.png')