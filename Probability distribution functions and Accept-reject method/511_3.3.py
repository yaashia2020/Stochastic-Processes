import numpy as np 
import random
import matplotlib.pyplot as plt 

f=100
random_variable=np.empty([f,1])
for j in range (0,f):
        x=0
        a=0
        i=0
        while 1:
            a+=1
            value=random.random()
            x=x+value
            if x>4:
                random_variable[i]=a
                x=0
                a=0
                i+=1
            if i==f:
                break
Expectation=np.mean(random_variable)
print (Expectation)
binwidth=1
bins = np.arange(min(random_variable)-0.5,max(random_variable)+0.5+binwidth,binwidth)
plt.hist(random_variable, bins, facecolor='yellow', edgecolor='black', alpha=0.75)
plt.xlabel("random variable")
plt.ylabel("frequency")
plt.show()