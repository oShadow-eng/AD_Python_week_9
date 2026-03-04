"""
Day 42 Activity: Distributions
Tasks:
1) Generate uniform and normal samples
2) Plot histograms and KDEs
3) Compare mean and std
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Task 1: Generate uniform and normal samples
uniform_samples = np.random.uniform(low=0, high=1, size=1000)
normal_samples = np.random.normal(loc=0, scale=1, size=1000)

#Task 2: Plot histograms and KDEs
#KDEs plot
#KDE plot for normal samples
sns.displot(normal_samples, kind="kde")
plt.show()
#KDE plot for uniform samples   
sns.displot(uniform_samples, kind="kde")
plt.show()

#Histogram plot uniform 
plt.hist(uniform_samples, bins=30, edgecolor="black", color="green")
plt.title("Histogram of Uniform Samples")
plt.xlabel("Value")
plt.ylabel("Count")
plt.show()
#Histogram plot normal  
plt.hist(normal_samples, bins=30, edgecolor="black", color="blue")
plt.title("Histogram of Normal Samples")
plt.xlabel("Value")
plt.ylabel("Count")
plt.show()



#Task 3: Compare mean and std
print(f"Mean of uniform samples: {uniform_samples.mean()}")
print(f"Mean of normal samples: {normal_samples.mean()}")
print(f"Standard Deviation of uniform samples: {uniform_samples.std()}")
print(f"Standard Deviation of normal samples: {normal_samples.std()}")

# TODO: Generate samples
# TODO: Plot distributions
