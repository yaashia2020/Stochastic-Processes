import numpy as np 
import math
import random
current_time=0
total_break_time=0
n_jobs=1
ts=0
ta=0
tdiff=0
l=0 
lam=np.empty([100,1])
#function to define lambda

def lamda():
    t = current_time % 10
    if t in range (0,6):
        l= 3*t+4
    if t in range (5, 11):
        l= -3*t + 34
    return l
for i in range (0,100):
    current_time=i
    lam[i]=lamda()
print(lam)
#function to generate time between two poisson intervals 
def t_arrival(temp):
   return random.expovariate(temp)

