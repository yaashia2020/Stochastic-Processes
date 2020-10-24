import random 
import numpy as np 
import matplotlib.pyplot as plt 
i=0
prev=0
x=0
y=0
count=0
no_of_heads=np.empty([200,1])
for i in range(0,200):
    value=random.random()
    if value<0.8:
        j=1
    else:
        j=0
    if prev==1 and j==1:
        x+=1
    if prev==0 and j==1:
        x=1
    if x>y:
        y=x
    if j==1:
        count+=1
        no_of_heads[i]=1
    else:
        no_of_heads[i]=0
    prev=j
    print(value)
    print(j) 
print("no.of heads {}" .format(count))
print("longest run of heads {}" .format(y))
bins=np.arange(2+1)-0.5
plt.title("no. of heads for 200 flips of a coin")
plt.hist(no_of_heads, bins, facecolor="blue", edgecolor="black", alpha=0.75)
plt.ylabel("frequency")
plt.xlabel("heads=1,tails=0")
plt.show()
