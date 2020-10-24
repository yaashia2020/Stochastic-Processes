import numpy as np 
import random
import matplotlib.pyplot as plt 
i=0
x=0
count=0
prev=0

run_of_heads=np.empty([100,1])
y=0 
for i in range(0,100):
   
    value= random.randrange(0,2)
    if prev==0 and value==0:
        x+=1
    if prev==1 and value==0:
        x=1
    if x>y:
        y=x
    if value==1:
        x=0
        run_of_heads[i]=y
        y=0
    if value==0:
        count+=1
        run_of_heads[i]=0
    if i==99 and value==0:
        run_of_heads[i]=y
    prev=value
    print(value)

print("no.of heads {}" .format(count))
print(run_of_heads)
bins=np.arange(10+1)-0.5
plt.title("run of heads for 100 flips of a coin")
plt.hist(run_of_heads, bins, facecolor="blue", edgecolor="black", alpha=0.75)
plt.ylabel("frequency")
plt.xlabel("head run")
plt.xlim([0.5,15])
plt.ylim([0,20])
plt.show()