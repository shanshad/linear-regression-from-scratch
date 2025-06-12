#parameters.py

import numpy as np
def lrg(n,sumx,sumxsqr,sumy,sumxy):
    A=np.array([[n,sumx],[sumx,sumxsqr]])
    B=np.array([sumy,sumxy])
    a,b=np.linalg.solve(A,B)
    return a,b

