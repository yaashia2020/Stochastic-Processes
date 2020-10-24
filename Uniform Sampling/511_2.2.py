import numpy as np
import random
import matplotlib.pyplot as plt
i=0
std_uniform=np.empty([10,1])
x_incremented=np.empty([10,1])
for i in range (0,10):
    value=random.random()
    print (value)
    std_uniform[i]=value
    x_incremented[i-1]=value
std_uniform=std_uniform.T
x_incremented=x_incremented.T
A = np.cov(x_incremented,std_uniform)
print(std_uniform)
print(x_incremented)
print(A)