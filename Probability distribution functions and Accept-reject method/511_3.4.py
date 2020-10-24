import numpy as np 
import matplotlib.pyplot as plt 
import random
from sklearn.utils import resample
a=np.empty([1,60])
p=np.empty([1,60])
f=0
x=0
for j in range (0, 60):
    a[0][j]=j+1
    p[0][j]=0.21/(j+1)
N=np.zeros([100,1])
val = np.empty([1000,1])
for i in range (0,1000):
    val[i]=random.choices(a[0],weights=p[0])


               

plt.hist(val, 20, facecolor='green', edgecolor='black', alpha=0.75)

plt.title("Histogram for sequence")
plt.xlabel("number")
plt.ylabel("Probability")
plt.show()