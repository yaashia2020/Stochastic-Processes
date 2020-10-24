import random
import numpy
user_spec= int(input("user-specified number of heads: "))
no_of_heads=0
count=0
while no_of_heads < user_spec:
    value=random.randrange(0,2)
    if value==1:
        no_of_heads+=1
    count+=1
    print(value)
print(count)
