import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.utils import resample
i=0
k=0
uniform_distribution=np.empty([5000,1])
uniform_distribution_mean=np.empty([10000,1])
variance=np.empty([10000,1])
for i in range(0,5000):
        value=random.uniform(-3,2)
        uniform_distribution[i]=value
for k in range (0,10000): 
    X = resample(uniform_distribution,n_samples = 5000,replace=True)
    uniform_distribution_mean[k]=np.mean(X)
    variance[k]=np.var(X)
per_1 = np.percentile(uniform_distribution_mean, 2.5,interpolation='nearest')
per_2 = np.percentile(uniform_distribution_mean, 97.5,interpolation='nearest')
per_3 = np.percentile(variance,2.5,interpolation='nearest')
per_4 = np.percentile(variance,97.5,interpolation='nearest')
print('The 2.5% percentile for mean is: ',str(per_1))
print('The 97.5% percentile for mean is: ',str(per_2))
print('The 2.5% percentile for variance is: ',str(per_3))
print('The 97.5% percentile for variance is: ',str(per_4))
plt.figure()
plt.subplot(211)

plt.ylabel("frequency")
plt.xlabel("mean")
plt.hist(uniform_distribution_mean,20, facecolor="purple", edgecolor="black", alpha=0.75)
plt.subplot(212)

plt.ylabel("frequency")
plt.xlabel("variance")
plt.hist(variance,20, facecolor="green", edgecolor="black", alpha=0.75)
plt.show()
