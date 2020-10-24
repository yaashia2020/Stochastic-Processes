import numpy as np
import random
import matplotlib.pyplot as plt
i=0
k=0
f=0
for k in range (0,4):
    if k==0 :
        f=100
    if k==1:
        f=500
    if k==2:
        f==5000
    if k==3:
        f=10000
    uniform_distribution=np.empty([f,1])
    for i in range(0,f):
        value=random.uniform(-3,2)
        print (value)
        uniform_distribution[i]=value
    sample_mean=np.mean(uniform_distribution)
    variance=np.var(uniform_distribution)
    print("sample mean is {}" .format(sample_mean))
    print("sample variance is {}" .format(variance))
    bins=np.arange(-3,2,0.5)
    plt.title("uniform distribution")
    plt.ylabel("frequency")
    plt.hist(uniform_distribution,bins, facecolor="red", edgecolor="black", alpha=0.75)
    plt.show()