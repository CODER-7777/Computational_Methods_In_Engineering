import numpy as np

y=np.array([0,2,4,6,8,10,12,14])
H=np.array([0,1,1.5,3,3.5,3.2,2,0])
U=np.array([0,0.1,0.12,0.2,0.25,0.3,0.15,0])
h=2
HU=H*U

# part a
A_trap=(h/2)*(H[0]+2*np.sum(H[1:-1])+H[-1])
Q_trap=(h/2)*(HU[0]+2*np.sum(HU[1:-1])+HU[-1])
U_bar_trap=Q_trap/A_trap

print(f"Trapezoidal: A={A_trap}, Q={Q_trap}, U={U_bar_trap:.4f}")

# part b
A_13=(h/3)*(H[0]+4*(H[1]+H[3])+2*H[2]+H[4])
Q_13=(h/3)*(HU[0]+4*(HU[1]+HU[3])+2*HU[2]+HU[4])
A_38=(3*h/8)*(H[4]+3*(H[5]+H[6])+H[-1])
Q_38=(3*h/8)*(HU[4]+3*(HU[5]+HU[6])+HU[-1])

A_simp=A_13+A_38
Q_simp=Q_13+Q_38
U_bar_simp=Q_simp/A_simp

print(f"Simpson: A={A_simp}, Q={Q_simp}, U={U_bar_simp:.4f}")