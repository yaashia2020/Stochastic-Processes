import numpy as np 
import random
import matplotlib.pyplot as plt 
import math
Average=0
Estimate=0

#defining the limits
a = -2
b = 2
 
#defining the function 
def func(x):
    return math.exp(x+x**2)
 
N=1000
X= np.empty([N,1])
Estimate = np.empty([N,1])

for f in range(0,N):
    Average=0
    for i in range(0,len(X)):
        X[i]= random.uniform(a,b)       #random uniform
        Average = Average + func(X[i])  #averaging the function 
    Estimate[f]=(b-a)/(N-1)*Average     #monte carlo estimation
print(Estimate)
expectation=np.mean(Estimate)
print(expectation)

#plot the estimate and print the mean
plt.title("Monte Carlo Estimation")
plt.hist(Estimate, 25, facecolor="blue", edgecolor="black", alpha=0.75)
plt.ylabel("frequency")
plt.show()
