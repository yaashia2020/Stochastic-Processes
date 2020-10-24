import numpy as np 
import random
import math
import matplotlib.pyplot as plt 
import scipy.stats as sci
poisson_experiment=np.empty([1000,1])
p=0
for i in range (0,1000):
    value= random.random()
    p=math.exp(-120)
    F=p
    m=0
    while 1:
        if value < F:
            poisson_experiment[i]= m
            i += 1
            break
        else:
            p = 120*p/(m+1)
            F += p
            m += 1


y = np.arange(sci.poisson.ppf(0.001, 120), sci.poisson.ppf(0.999, 120))
plt.hist(poisson_experiment, 20, density=True, facecolor='green', edgecolor='black', alpha=0.75)
plt.plot(y, sci.poisson.pmf(y, 120), linewidth=2, color='red')
plt.title("Histogram for number of arrivals per hour")
plt.xlabel("Number of car arrivals per hour")
plt.ylabel("Probability")

plt.show()