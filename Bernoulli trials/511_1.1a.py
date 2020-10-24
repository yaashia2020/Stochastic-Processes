i=0
x=0
count=0
prev=0
y=0
import matplotlib.pyplot as plt
import numpy as np
import random

no_of_heads=np.empty([50,1])
 
for i in range(0,50):
    value= random.randrange(0,2)
    if prev==0 and value==0:
        x+=1
    if prev==1 and value==0:
        x=1
    if x>y:
        y=x
    if value==0:
        count+=1
        no_of_heads[i]=0
    else:
        no_of_heads[i]=1
    prev=value
    print(value)
    
print("no.of heads {}" .format(count))
print("longest run of heads {}" .format(y))
bins=np.arange(2+1)-0.5
plt.title("no. of heads for 50 flips of a coin")
plt.hist(no_of_heads, bins, facecolor="blue", edgecolor="black", alpha=0.75)
plt.ylabel("frequency")
plt.xlabel("heads=0,tails=1")
plt.show()