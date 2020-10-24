import numpy as np 
import matplotlib.pyplot as plt 
import random 
from scipy.stats import chisquare
from scipy.stats import chi2
M = 10
seq = np.array([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
i=0
uniform_sampling=np.empty([10,1])
for i in range (0,10):
    value= random.choices(seq)
    uniform_sampling[i]=value
print(uniform_sampling)
sampling_ideal= 10*np.array([1/10,1/10,1/10,1/10,1/10,1/10,1/10,1/10,1/10,1/10])
chi_sq_test=chisquare(uniform_sampling,sampling_ideal)
print('Chi square test statistic is: ', str(chi_sq_test.statistic))
print('Chi square test p-value is: ', str(chi_sq_test.pvalue))
plt.title("uniform distribution")    
plt.ylabel("frequency")
plt.hist(uniform_sampling, 10, facecolor="red", edgecolor="black", alpha=0.75)
print('The 95 percentile of chi square dist with 9 dof, is:',str(chi2.ppf(0.95,df=9)))
plt.show()