import numpy as np 
import math
import random
import matplotlib.pyplot as plt 
import time
from scipy.stats import norm

start_box = time.time()
V1=4
M1=1
M2=2
V2=9
s=0
i=0
X = np.empty([1000000,1])
Y = np.empty([1000000,1])
while (i<1000000):
    value1=random.uniform(-1,1)
    value2=random.uniform(-1,1)
    s=value1**2+value2**2
    if (s<1):
        X[i] = np.sqrt(-2*np.log(s)/s)*value1
        Y[i] = np.sqrt(-2*np.log(s)/s)*value2
        X[i] = np.sqrt(V1)*X[i] + M1
        Y[i] = np.sqrt(V2)*Y[i] + M2
        i=i+1


end_box = time.time()
print(end_box - start_box)
x = X.T
y = Y.T
covxy = np.cov(x,y)
print(covxy)
print('mean of X', np.mean(X))
print('mean of Y', np.mean(Y))

print('Variance of X',np.var(X))
print('Variance of Y',np.var(Y))

