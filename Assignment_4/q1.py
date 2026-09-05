import numpy as np

np.set_printoptions(formatter={'float':'{:0.4f}'.format})

def get_lu(mat):
    n=len(mat)
    u_m=np.copy(mat).astype(float)
    l_m=np.eye(n)
    for k in range(n-1):
        for i in range(k+1,n):
            fctr=u_m[i,k]/u_m[k,k]
            l_m[i,k]=fctr
            u_m[i,k:]=u_m[i,k:]-fctr*u_m[k,k:]
    return l_m,u_m

def solve_sys(l_m,u_m,vec):
    n=len(vec)
    d_v=np.zeros(n)
    for i in range(n):
        d_v[i]=vec[i]-np.dot(l_m[i,:i],d_v[:i])
    x_v=np.zeros(n)
    j=n-1
    while j>=0:
        x_v[j]=(d_v[j]-np.dot(u_m[j,j+1:],x_v[j+1:]))/u_m[j,j]
        j-=1
    return x_v

a_mat=np.array([[7.0,2.0,-3.0],[2.0,5.0,-3.0],[1.0,-1.0,-6.0]])
b_vec=np.array([12.0,18.0,-6.0])

l_res,u_res=get_lu(a_mat)
print("(a)LU Matrices")
print("L=\n",l_res)
print("U=\n",u_res)

ans_x=solve_sys(l_res,u_res,b_vec)
print("\n(b)System Solution")
print("X=\n",ans_x)

sze=a_mat.shape[0]
inv_mat=np.zeros((sze,sze))
id_mat=np.eye(sze)
for c in range(sze):
    inv_mat[:,c]=solve_sys(l_res,u_res,id_mat[:,c])
print("\n(c)Inverse Matrix")
print("A_inv=\n",inv_mat)

nrm_a=np.max(np.sum(np.abs(a_mat),axis=1))
nrm_inv=np.max(np.sum(np.abs(inv_mat),axis=1))
cond_no=nrm_a*nrm_inv
print("\n(d)Condition Number")
print("Cond(A)=",round(cond_no,4))