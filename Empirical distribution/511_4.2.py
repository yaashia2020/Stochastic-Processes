import numpy as np 
import matplotlib.pyplot as plot 
import math
import random
from scipy.stats import chi2

#taking random uniform samples
N=1000
z1=np.empty([N,1])
z2=np.empty([N,1])
z3=np.empty([N,1])
z4=np.empty([N,1])
X=np.empty([N,1])
for i in range(0,N):
    z1[i]=random.gauss(0,1)
    z2[i]=random.gauss(0,1)
    z3[i]=random.gauss(0,1)
    z4[i]=random.gauss(0,1)
    X[i]= z1[i]**2+z2[i]**2+z3[i]**2+z4[i]**2

X=np.sort(X, axis=None)

#defining the chisquare dist
df=4
t=np.arange(0,15,10**(-1))
chi_sq=chi2.cdf(t,df)

#plot empirical as well as chisquare cdf
plot.step(X,np.arange(0,1,1/N), label='Empirical CDF')
plot.plot(t,chi_sq)
plot.ylim(0,1.05)
plot.show()

#the 25th,50th and 90th percentile
print('25th percentile: ',chi2.ppf(0.25,df))
print('50th percentile: ',chi2.ppf(0.5,df))
print('90th percentile: ',chi2.ppf(0.9,df))

#lower bound
a=0
max_lb = float('-inf')
for x in X:
    min_diff = float('inf')
    for j in range(len(t)):
        if min_diff > abs(x - t[j]):
            min_diff = abs(x - t[j])
            chi_sq_i = j
    if max_lb < abs(np.arange(0,1,1/N)[a] - chi_sq[chi_sq_i]):
        max_lb = abs(np.arange(0,1,1/N)[a] - chi_sq[chi_sq_i])

    a += 1
m=int(N/4)
n=int(N/2)
p=int(9*N/10)
print (max_lb)
print (X[m])
print (X[n])
print (X[p])









