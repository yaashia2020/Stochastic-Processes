import numpy as np
import matplotlib.pyplot as plt

def my_func(x,y):
    return np.cos(np.pi + 5*(x+y))

N = 1000
fX = np.random.rand(1,N)
fY = np.random.rand(1,N)
X = my_func(fX,fY)
print('Monte Carlo Mean: ', np.mean(X))
print('Monte Carlo Variance: ', 2*np.std(X)/np.sqrt(N))

# stratified sampling
K = 20
XSb = np.zeros((K,K))
SS = np.zeros_like(XSb)
Nij = N/np.power(K,2)

for i in range(0,K):
    for j in range(0,K):
        XS = my_func((i+np.random.rand(1,int(Nij)))/K,(j+np.random.rand(1,int(Nij)))/K)
        XSb[i][j] = np.mean(XS)
        SS[i][j] = np.var(XS)

SST = np.mean((SS/N)) 
SSM = np.mean((XSb))
print('Stratified Sampling Mean: ', str(SSM)) 
print('Stratified Sampling Variance: ', 2*np.sqrt(SST))

# importance sampling
N_is = 1000
U = np.random.rand(2,N_is)
X_is = -np.log(1+(1/np.exp(1)-1)*U)
T = np.power((1/np.exp(1)-1),2)*np.exp(np.sum(5*abs(X_is-5),axis=0) - np.sum(-X_is,axis=0))
print('Importance Sampling Mean: ', str(np.mean(T)))
print('Importance Sampling Variance: ', 2*np.std(T)/np.sqrt(N))