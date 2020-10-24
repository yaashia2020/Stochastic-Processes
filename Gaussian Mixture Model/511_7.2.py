import numpy as np 
import matplotlib.pyplot as  plt 
import random
m1=0
m2=3
v1=1.5
v2=2
p=0.2
X= np.empty([2000,1])
Y= np.empty([2000,1])
Z= np.empty([2000,1])
for i  in range(0,2000):
    X[i]= random.gauss(m1,v1)
    Y[i]= random.gauss(m2,v2)
    u3=random.random()
    if u3<p:
        Z[i]=X[i]
    else :
        Z[i]=Y[i]
print(Z)
plt.title("GMM")
count, bins, ignored = plt.hist(Z, 30, density=True,facecolor="green", edgecolor="yellow", alpha=0.75)
plt.plot(bins, p*(1/(v1 * np.sqrt(2 * np.pi)) *
                np.exp( - (bins - m1)**2 / (2 * v1**2) )) + (1-p)*(1/(v2 * np.sqrt(2 * np.pi)) *
                np.exp( - (bins - m2)**2 / (2 * v2**2)) ),
         linewidth=2, color='r')

plt.show()
