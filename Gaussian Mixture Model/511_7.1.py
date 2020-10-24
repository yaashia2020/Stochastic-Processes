import numpy as np 
import random 
import math
from scipy.linalg import cholesky
m1=1
m2=2
m3=3
v1=np.sqrt(3)
v2=np.sqrt(5)
v3=np.sqrt(4)

cov=np.array([[3, -1, 1],[-1, 5, 3], [1, 3, 4]])

u1= random.random()
u2= random.random()
u3= random.random()
u4= random.random()
X1=np.sqrt(-2*np.log(u1))*np.cos(2*np.pi*u2)
X2=np.sqrt(-2*np.log(u1))*np.sin(2*np.pi*u2)
X3=np.sqrt(-2*np.log(u3))*np.cos(2*np.pi*u4)

X =np.array([[X1],[X2],[X3]])
L = cholesky(cov, lower=True)
X=L.dot(X)
X[0] = v1*X[0]+m1
X[1] = v2*X[1]+m2
X[2] = v3*X[2]+m3
print (X)