import numpy as np 
import random
from scipy.stats import multivariate_normal
m1 = float(input("mean of X1: "))
m2 = float(input("mean of X2: "))
m3 = float(input("mean of X3: "))
m4 = float(input("mean of X4: "))
p = float(input("weight of one population: "))

 
print("Enter the entries for covariance matrix 1 in a single line (separated by space): ") 
entries1 = list(map(float, input().split())) 
cov1 = np.array(entries1).reshape(2, 2) 
print(cov1) 
print("Enter the entries for covariance matrix 2 in a single line (separated by space): ")
entries2 = list(map(float, input().split())) 
cov2 = np.array(entries2).reshape(2, 2) 
print(cov2) 
v1 = np.sqrt(cov1[0][0])
v2 = np.sqrt(cov1[1][1])
v3 = np.sqrt(cov2[0][0])
v4 = np.sqrt(cov2[1][1])
#Box Muller Method
Z= np.empty([2,1])


u1= random.random()
u2= random.random()
u3= random.random()
u4= random.random()
X1=np.sqrt(-2*np.log(u1))*np.cos(2*np.pi*u2)
X2=np.sqrt(-2*np.log(u1))*np.sin(2*np.pi*u2)
X3=np.sqrt(-2*np.log(u3))*np.cos(2*np.pi*u4)
X4=np.sqrt(-2*np.log(u3))*np.sin(2*np.pi*u4)
#since uncorrelated no need of cholesky decomposition 
X=np.array([[X1],[X2]])
Y=np.array([[X3],[X4]])
X[0] = v1*X[0]+m1
X[1] = v2*X[1]+m2
Y[0] = v3*Y[0]+m3
Y[1] = v4*Y[1]+m4
u5= random.random()

if u5<p:
    Z[i]=X
else:
    Z[i]=Y
print (Z)

