import numpy as np 
import math
import random
import matplotlib.pyplot as plt 
import time
from scipy.stats import norm

start_box = time.time()
X = np.empty([1000000,1])
Y = np.empty([1000000,1])

V1=4
M1=1
M2=2
V2=9
# creating samples from box muller method
for i in range (0,1000000):
    value1=random.random()
    value2=random.random()
    X[i]=np.sqrt(-2*np.log(value1))*np.cos(2*np.pi*value2)
    Y[i]=np.sqrt(-2*np.log(value1))*np.sin(2*np.pi*value2)
    X[i]=np.sqrt(V1)*X[i] + M1
    Y[i]=np.sqrt(V2)*Y[i] + M2
  

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
