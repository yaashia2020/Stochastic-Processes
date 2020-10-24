import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import math

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

N_r = 512
x = np.linspace(-N_r,N_r,100)
y = np.linspace(-N_r,N_r,100)
X, Y = np.meshgrid(x, y)
Z = 418.9829*2 - (X*np.sin(np.sqrt(abs(X))) + Y*np.sin(np.sqrt(abs(Y))))

plt.figure(num=None,dpi=80)
plt.contourf(X,Y,Z)
plt.title('Contour plot of Schwefel function with dimension=2')
plt.colorbar()
plt.show()
plt.close()

cplot = plt.figure(num=None,dpi=95)
ax = cplot.add_subplot(111,projection='3d')
surf = ax.plot_surface(X,Y,Z,cmap=cm.coolwarm)
cbar = cplot.colorbar(surf, shrink=0.5, aspect=5)
plt.title('3D plot of Schwefel function with dimension=2')
plt.show()
plt.close()


def sch_fun(x1,x2): 
    return (418.9829*2 - x1*np.sin(np.sqrt(np.abs(x1))) - x2*np.sin(np.sqrt(np.abs(x2)))) 
# simulated annealing to find the minimum 
N = 50
x1 = 0 #we begin our simulation at origin 
x2 = 0 
x1_list = [] 
x2_list = [] 
T = 100 
value_list = [] 
value_list.append(sch_fun(x1,x2)) 
for i in range (1,N): 
    x1_prop = x1 + np.random.normal(0,50) # creating a new propsal solution 
    x2_prop = x2 + np.random.normal(0,50) 
    alpha = np.exp((sch_fun(x1_prop,x2_prop) - sch_fun(x1,x2))/T) #the threshold value 
    if (sch_fun(x1_prop,x2_prop) < sch_fun(x1,x2)): # cheking the coondition 
        x1 = x1_prop #updating new value
        x2 = x2_prop 
    else: 
        if (np.random.rand() < alpha): #now checking with the alpha, where we sometimes accpet bad values 
            x1 = x1_prop 
            x2 = x2_prop 
    #T = 100/(np.log(i+1)) #logarithmic cooling function 
    #T = 100/((i+1)**2) #polynomial cooling function 
    T = 100/np.exp(i) #exponenential cooling function 
    x1_list.append(x1) 
    x2_list.append(x2) 
    value_list.append(sch_fun(x1,x2)) 
plt.hist(value_list) 
plt.show() 
plt.plot(x1_list, x2_list, 'C3', zorder=1, lw=3) 
plt.scatter(x1_list, x2_list, s=1, zorder=2) 
plt.contour(X,Y,Z) 
plt.title('final path') 
plt.tight_layout() 
plt.show()