import numpy as np 
import random
import matplotlib.pyplot as plot 

r= 4.5*3.5*2.5*1.5*0.5
pdfX = lambda x: (1/(r*np.sqrt(np.pi)))*(np.power(x,4.5))*(np.exp(-x))
pdfY = lambda y: (1/5.5)*(np.exp(-(1/5.5)*np.array(y)))


t = np.arange(0,17,0.01)
ratio = np.divide(pdfX(t),pdfY(t))
c = np.max(ratio)
X=np.empty([1000,1])
C=np.empty([1000,1])
for i in range (0,1000):
    k=0
    while 1:
        k += 1
        value = random.random()
        A=random.expovariate(1/5.5)
        if value<=(1/(r*np.sqrt(np.pi)))*(float(A)**4.5)(np.exp(-float(A)))/(c*(1/5.5)*(np.exp(-(1/5.5)*float(A)))):
            X[i]=A
            C[i]=k
            break

rate = 1000/np.sum(C)

print('Rate of acceptance: ', rate)

plot.hist(X, 20, density=True, facecolor='green', edgecolor='black', alpha=0.75)
plot.plot(t, pdfX(t),linewidth=2, color='red')
plot.title('Histogram for X')
plot.xlabel('values')
plot.ylabel('Probability')
plot.grid(True)
plot.show()