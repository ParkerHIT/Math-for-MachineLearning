#Simulating central limit theorem

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randint


#Create a list named means with 1000 sample means from samples of 30 rolled dice by using list comprehension.
means1 = [randint(1, 7, 30).mean() for i in range(1000)]


#Adapt code to visualize only 100 samples in the means list; the distribution changed
means2 = [randint(1, 7, 30).mean() for i in range(100)]

# Plot the histograms
plt.hist(means1, label='1000 Samples', alpha=0.5)
plt.hist(means2, label='100 Samples', alpha=0.5)

# Add a legend
plt.legend()

# Display the plot
plt.show()