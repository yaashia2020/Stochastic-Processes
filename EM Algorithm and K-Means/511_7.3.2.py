import numpy as np 
import random 
from scipy.stats import multivariate_normal 
m1 = float(input("mean of X1: "))
m2 = float(input("mean of X2: "))
m3 = float(input("mean of X3: "))
m4 = float(input("mean of X4: "))

mean1=np.array([m1,m2])
mean2=np.array([m3,m4])
print("Enter the entries for covariance matrix 1 in a single line (separated by space): ") 
entries1 = list(map(float, input().split())) 
cov1 = np.array(entries1).reshape(2, 2) 
print(cov1) 
print("Enter the entries for covariance matrix 2 in a single line (separated by space): ")
entries2 = list(map(float, input().split())) 
cov2 = np.array(entries2).reshape(2, 2) 
print(cov2)


r1 = np.random.multivariate_normal(mean1, cov1,300) 
r2 = np.random.multivariate_normal(mean2, cov2,300) 
X = np.vstack((r1,r2)) 

np.random.shuffle(X)
X=X[0:599:2]

#the EM algo
#initialize

w1=0.5
w2=0.5
means1=np.array([0.13,4.04])
means2=np.array([-2,-.05])
var1=np.array([[1,0],[0,1]])
var2=np.array([[1,0],[0,1]])


for u in range(0, 5):
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    sum6=0
    gamma1=np.empty([300,1])
    gamma2=np.empty([300,1])
    for i in range (0,300):
        normal1=w1*multivariate_normal.pdf(X[i,:],mean=means1,cov=var1)
        normal2=w2*multivariate_normal.pdf(X[i,:],mean=means2,cov=var2)
        gamma1[i]=normal1/(normal1+normal2)
        gamma2[i]=normal2/(normal1+normal2)
    for k in  range(0,300):
        sum1=sum1+ (X[k,:]*gamma1[k])  
        sum2=sum2+ gamma1[k]
        sum3=sum3+gamma2[k]
        sum4=sum4+(X[k,:]*gamma2[k])
    means1=sum1/sum2
    means2=sum4/sum3
    for j in range(0,300):
        sum5= gamma1[j]*(X[i:,]-means1)*((X[i:,]-means1).T)
        sum6= gamma2[j]*(X[i:,]-means2)*((X[i:,]-means2).T)
    var1=sum5/sum2
    var2=sum6/sum3
    w1=sum2/300
    w2=sum3/300
    print(means1,means2,var1,var2,w1,w2)




