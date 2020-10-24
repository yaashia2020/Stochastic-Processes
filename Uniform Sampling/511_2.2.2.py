import numpy as np
import random
import matplotlib.pyplot as plt
i=0
std_uniform=np.empty([10,1])
y=np.empty([10,1])
for i in range (0,10):
    value=random.random()
    print (value)
    std_uniform[i]=value
    if i>=3:
        y[i]=std_uniform[i]-2*std_uniform[i-1]+0.5*std_uniform[i-2]-std_uniform[i-3]
    else:
        y[i]=0
std_uniform=std_uniform.T
y=y.T
A = np.cov(y,std_uniform)
print(std_uniform)
print(y)
print(A)