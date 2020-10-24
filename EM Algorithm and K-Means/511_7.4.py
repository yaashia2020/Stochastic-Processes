import numpy as np 
import random
import matplotlib.pyplot as plt
from scipy.stats import sem 
from sklearn.cluster import KMeans 
from scipy.stats import multivariate_normal
wait=[]
eruption=[]
with open("F:\\2nd sem\\EE 511/faithful.dat") as i: 
    wait = [float(line.split()[1]) for line in i] 
with open("F:\\2nd sem\\EE 511/faithful.dat") as i: 
    dura = [float(line.split()[2]) for line in i]

mean_wait = sum(wait)/272 
mean_eruption = sum(eruption)/272 

kmeans_plot = np.array(list(zip(wait, eruption))) 
plt.figure(figsize=(9, 9)) 
plt.xlabel('eruption') 
plt.ylabel('wait') 
plt.title('2D-SCATTER PLOT OF THE DATA') 
plt.scatter(wait,eruption,c='blue') 
plt.show()

kmeans = KMeans(n_clusters=2, random_state=0).fit(kmeans_plot) 
plt.scatter(kmeans_plot[:,0], kmeans_plot[:,1], c=kmeans.labels_.astype(float)) 
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1], marker='^', c='red') 
plt.title('Data Points with Labels by K-means Clustering') 
plt.xlabel('eruption') 
plt.ylabel('wait') 
plt.show()
#em algo
w1=0.5
w2=0.5
means1 = kmeans.cluster_centers_[0,:] 
means2 = kmeans.cluster_centers_[1,:]
var1=np.array([[1,0],[0,1]])
var2=np.array([[1,0],[0,1]])


for u in range(0, 5):
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    sum6=0
    gamma1=np.empty([300,1])
    gamma2=np.empty([300,1])
    for i in range (0,300):
        normal1=w1*multivariate_normal.pdf(X[i,:],mean=means1,cov=var1)
        normal2=w2*multivariate_normal.pdf(X[i,:],mean=means2,cov=var2)
        gamma1[i]=normal1/(normal1+normal2)
        gamma2[i]=normal2/(normal1+normal2)
    for k in  range(0,300):
        sum1=sum1+ (X[k,:]*gamma1[k])  
        sum2=sum2+ gamma1[k]
        sum3=sum3+gamma2[k]
        sum4=sum4+(X[k,:]*gamma2[k])
    means1=sum1/sum2
    means2=sum4/sum3
    for j in range(0,300):
        sum5= gamma1[j]*(X[i:,]-means1)*((X[i:,]-means1).T)
        sum6= gamma2[j]*(X[i:,]-means2)*((X[i:,]-means2).T)
    var1=sum5/sum2
    var2=sum6/sum3
    w1=sum2/300
    w2=sum3/300
    print(means1,means2,var1,var2,w1,w2)
r1 = np.random.multivariate_normal(means1, var1,300) 
r2 = np.random.multivariate_normal(means2, var2,300) 
X = np.vstack((r1,r2)) 
np.random.shuffle(X)
X=X[0:599:2] 
plt.figure(figsize=(8,8)) 
x, y = np.mgrid[0:5:.01, 30:100:.01]
pos = np.empty(x.shape + (2,)) 
pos[:, :, 0] = x 
pos[:, :, 1] = y 
rv1 = multivariate_normal(means1,var1) 
plt.contour(x, y, rv1.pdf(pos))
rv2 = multivariate_normal(measn2,var2) 
plt.contour(x, y, rv2.pdf(pos)) 
plt.scatter(X[:,0], X[:,1]) 
plt.scatter(means1[0],means1[1], marker='^', c='red') 
plt.scatter(means2[0],means2[1], marker='^', c='red') 
plt.xlabel('eruptions') 
plt.ylabel('wait') 
plt.title('CONTOUR OVERLAYED WITH SCATTER') 
plt.show() 