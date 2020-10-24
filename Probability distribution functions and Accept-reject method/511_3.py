import numpy as np 
import random 
from sklearn.utils import resample
batch_of_chips=np.ones([125,1])
k=0
j=0
x=0
f=0
P=0
number=30
for i in range (0,6):
    value = random.randint(1,125)
    batch_of_chips[value]=0  
 
for m in range (0,1000):
    X = resample(batch_of_chips,n_samples = 5,replace=True)
    if(0 in X):
        k+=1
#print (k)

Probability= k/1000
print (Probability)   

