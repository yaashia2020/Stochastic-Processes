import numpy as np 
import random
import matplotlib.pyplot as plt 
import scipy.stats as sci
a=[0,1]
Lambda=120
bernoulli_trial=np.empty([100,1])
for j in range (0,100):
    x=0
    for i in range (0,36000):
        value=np.random.choice(a,replace=True,p=[299/300, 1/300])
        if value==1:
            x+=1
    bernoulli_trial[j]=x

y = np.arange(sci.poisson.ppf(0.001, Lambda), sci.poisson.ppf(0.999, Lambda))
plt.hist(bernoulli_trial, 10,density=True, facecolor="blue", edgecolor="black", alpha=0.75)
plt.plot(y, sci.poisson.pmf(y, Lambda), linewidth=2, color='red')
plt.ylabel("frequency")
plt.xlabel("no. of cars per hour")

plt.show()