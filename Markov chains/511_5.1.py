import numpy as np 
import math
import random
current_time=0

n_jobs=0
ts=0
ta=0
tdiff=0
matrix= np.empty([100,1])
#function to define lambda
def lamda():
    t = current_time % 10
    l = None
    if t>=0 and t<=5:
        l= 3*t+4
    elif t<=10:
        l= -3*t + 34
    return l

#function to generate time between two poisson intervals 
def t_arrival(temp):
   return random.expovariate(temp)

#function to generate service time 
def t_serve():
   return random.expovariate(25)
    
#function to generate break time
def t_break():
   return random.uniform(0,0.3)

for i in range (0,100):   
    total_break_time=0
    current_time=0
    while (current_time < 100):
        
        if n_jobs>0:
            ts = t_serve()
            temp=lamda()
            ta1 = t_arrival(temp)
            #n_jobs=+1

            if ts<ta1:
                current_time=current_time+ts
                n_jobs = n_jobs-1



            if ts>ta1:
                n_jobs=+1
                temp=lamda()
                ta=t_arrival(temp)
                t_diff=ts-ta
                current_time=current_time+ta
                n_jobs = n_jobs+1
                
                if ta<=tdiff:
                    temp=lamda()
                    ta=t_arrival(temp)
                    n_jobs=+1
                    current_time=current_time+ta
                    tdiff=ts-current_time
                    
                
                    
                if ta>tdiff:
                    n_jobs= n_jobs-1
                    current_time=ts

        if (n_jobs==0):
            tb=t_break()
            
            current_time=current_time + tb
            total_break_time= total_break_time + tb
            temp=lamda()
            ta= t_arrival(temp)
            
            if ta<tb:
                n_jobs=+1
            
    print(total_break_time)
    matrix[i]=total_break_time
#print (matrix)     
f=np.mean(matrix)

print(n_jobs)
print (f)
    

