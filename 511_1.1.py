i=0
j=0
k=0
x=0
count=0
prev=0
y=0
f=0
import matplotlib.pyplot as plt
import numpy as np
import random
for k in range(1,5):
 if k==1:
     f=20
 if k==2:
     f=100
 if k==3:
     f=200
 if k==4:
     f=1000
 no_of_heads=np.empty([f,1])
 for j in range(0,f):
        count=0
        y=0
        x=0
        for i in range(1,51):
            value= random.randrange(0,2)
            if prev==0 and value==0:
                x+=1
            if prev==1 and value==0:
                x=1
            if x>y:
                y=x
            if value==0:
                count+=1
            prev=value
            print(value)
        no_of_heads[j]=count    
        print("no.of heads {}" .format(count))
        print("longest run of heads {}" .format(y))
 bins=np.arange(51+1)-0.5
 plt.title("Number of heads for 50 coin flips")
 plt.hist(no_of_heads, bins, facecolor="blue", edgecolor="black", alpha=0.75)
 plt.ylabel("frequency")
 plt.xlabel("no. of heads")
 plt.xlim([10, 40])
 plt.show()