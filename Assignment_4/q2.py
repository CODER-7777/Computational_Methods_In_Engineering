import numpy as np

np.set_printoptions(formatter={'float':'{:0.4f}'.format})

def get_cholesky(m):
    n=len(m)
    low=np.zeros((n,n))
    for r in range(n):
        for c in range(r+1):
            tmp=np.dot(low[r,:c],low[c,:c])
            if r==c:
                low[r,c]=np.sqrt(m[r,r]-tmp)
            else:
                low[r,c]=(m[r,c]-tmp)/low[c,c]
    return low

mat_a=np.array([[8.0,20.0,15.0],[20.0,80.0,50.0],[15.0,50.0,60.0]])
mat_l=get_cholesky(mat_a)
print("L_matrix=\n",mat_l)