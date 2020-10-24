import numpy as np
import matplotlib.pyplot as plt
import math
import random
P = np.zeros([20,1])
for i in range(5):
    P[i][0] = 0.06
P[5][0] = 0.15
P[6][0] = 0.13
P[7][0] = 0.14
P[8][0] = P[5][0]
P[9][0] = P[6][0]

Q = np.full((20,1),0.05)

a = 0
r = 0

c = int(input("Enter the value of c for the accept-reject sampling method: "))

z_total = np.zeros([10000,1])

for i in range(10000):
    j = 0
    random_number = random.random()
    while random_number > j:
        z = math.floor((random.random())*20)
        j = P[z]/(c*Q[z])
        random_number = random.random()
        if random_number > j:
            r += 1
    a += 1
    z_total[i][0] = z
    
binwidth = 1
bins = np.arange(min(z_total),max(z_total)+1+binwidth,binwidth)
    
x = np.zeros([10,1])
for i in range(len(x)):
    x[i] = i

y = np.zeros([10,1])
for i in range(len(y)):
    y[i] = P[i]
    
plt.hist(z_total, bins, density=True, facecolor='green', edgecolor='black', alpha=0.75)
plt.plot(x, y, linewidth=2, color='red')
plt.title("Accept-Reject results")
plt.xlabel("simulated value")
plt.ylabel("Frequency")

plt.show()   
mean_theo = 0.06*(1+2+3+4+5) + 0.15*(6+9) + 0.13*(7+10) + 0.14*8
mean_prac = np.mean(z_total) + 1

var_theo = 0
for i in range(10):
    var_theo += P[i]*((mean_theo - (i+1))**2)
var_prac = np.var(z_total)

efficiency_theo = 1/c
efficiency_prac = a/(a+r)

print("Theoretical Expectation: ", mean_theo)
print("Estimated Sample mean: ", mean_prac)
print("Theoretical Variance: ", var_theo[0])
print("Estimated Sample Variance: ", var_prac)
print("Theoretical Efficiency: ", efficiency_theo)
print("Estimated Efficiency: ", efficiency_prac)