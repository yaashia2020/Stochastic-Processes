import numpy as np 
import random
import math
from sklearn.utils import resample

N=15
data = np.array([79,54,74,62,85,55,88,85,51,85,54,84,78,47,83])
mean_data = np.mean(data)
std_dev = np.std(data)
z_alpha = 1.96
statCI1 = mean_data + z_alpha*(std_dev/float (math.sqrt(N)))
statCI2 = mean_data - z_alpha*(std_dev/float (math.sqrt(N)))

print(statCI1)
print(statCI2)

#bootstrap interval
X_means=np.empty([1000,1])
for i in range(0,1000):
    X=resample(data,n_samples=len(data),replace=True) 
    X_means[i]=np.mean(X)
X_means=np.sort(X_means)
print(X_means[250])
print(X_means[975])

whole_data = np.array([79,54,74,62,85,55,88,85,51,85,54,84,78,47,
83,52,62,84,52,79,51,47,78,69,74,83,55,76,78,
79,73,77,66,80,74,52,48,80,59,90,80,58,84,58,
73,83,64,53,82,59,75,90,54,80,54,83,71,64,77,
81,59,84,48,82,60,92,78,78,65,73,82,56,79,71,62,
76,60,78,76,83,75,82,70,65,73,88,76,80,48,86,
60,90,50,78,63,72,84,75,51,82,62,88,49,83,81,
47,84,52,86,81,75,59,89,79,59,81,50,85,59,87,
53,69,77,56,88,81,45,82,55,90,45,83,56,89,46,
82,51,86,53,79,81,60,82,77,76,59,80,49,96,53,
77,77,65,81,71,70,81,93,53,89,45,86,58,78,66,
76,63,88,52,93,49,57,77,68,81,81,73,50,85,74,
55,77,83,83,51,78,84,46,83,55,81,57,76,84,77,
81,87,77,51,78,60,82,91,53,78,46,77,84,49,83,
71,80,49,75,64,76,53,94,55,76,50,82,54,75,78,
79,78,78,70,79,70,54,86,50,90,54,54,77,79,64,
75,47,86,63,85,82,57,82,67,74,54,83,73,73,88,
80,71,83,56,79,78,84,58,83,43,60,75,81,46,90,46,74])

whole_data_mean=np.mean(whole_data)
whole_data_std_dev=np.std(whole_data)
stat_whole_data_1=whole_data_mean + z_alpha*(whole_data_std_dev/float (math.sqrt(N)))
stat_whole_data_2=whole_data_mean - z_alpha*(whole_data_std_dev/float (math.sqrt(N)))


print(stat_whole_data_1)
print(stat_whole_data_2)

whole_means=np.empty([1000,1])
for i in range(0,1000):
    whole=resample(whole_data,n_samples=len(whole_data),replace=True) 
    whole_means[i]=np.mean(whole)
whole_means=np.sort(whole_means)
print(whole_means[250])
print(whole_means[975])



