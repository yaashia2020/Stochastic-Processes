import numpy as np 
import random
import matplotlib.pyplot as plt 
from scipy.stats import levy_stable
a=-np.pi/2
b=np.pi/2
RV=np.empty([100,1])
alpha=float(input("alpha:"))
if alpha<=0 or alpha>2 or np.isscalar(alpha)==False:
    raise Exception('ALPHA must be a scalar within (0,2]')
beta=float(input("beta:"))
if abs(beta)>1 or np.isscalar(beta)==False:
    raise Exception('BETA must be a scalar within [−1,1]')
gamma=float(input("gamma:"))
if gamma<0 or np.isscalar(gamma)==False:
    raise Exception('GAMMA must be a non−negative scalar')
delta=float(input("delta:"))
if np.isscalar(delta)==False:
    raise Exception('C must be a scalar')

# define the sampling function
def generate_samples(alpha,beta,gamma,delta):
    V= random.uniform(a,b)
    W=random.expovariate(1)
    if alpha!=1:
        S= (1+(beta*np.tan((np.pi*alpha)/2))**2)**(1/2*alpha)
        B= np.arctan((beta*np.tan((np.pi*alpha)/2)))/alpha
        X= S*(np.sin(alpha*(V+B))/np.cos(V)**(1/alpha))*(np.cos(V-alpha*(V+B))/W)**((1-alpha)/alpha)
        X = gamma*X + delta
    if alpha == 1:
        X= (1/b)*((b+beta*V)*np.tan(V)-beta*np.log(W*np.cos(V)/(b+beta*V)))
        X = gamma*X + (2/np.pi)*beta*gamma*np.log(gamma) + delta
    return X

for i in range(0,100):
    RV[i]= generate_samples(alpha,beta,gamma,delta)

t = np.arange(-10,10,0.01)
plt.hist(RV, 15, density=False, facecolor='green', edgecolor='black', alpha=0.75)
plt.plot(t, 50*levy_stable.pdf(t,alpha,beta),linewidth=2, color='red')
#plt.title('Histogram with alpha = '+str(alpha)+' and beta = '+str(beta))
plt.xlabel('values')
plt.ylabel('Probability')

plt.show()







