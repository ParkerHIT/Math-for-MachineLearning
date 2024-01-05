#Generate sample data for a Bernoulli event and then examine the visualization produced.

import numpy as np
import matplotlib.pyplot as plt
# Generate bernoulli data
from scipy.stats import bernoulli
data1 = bernoulli.rvs(p=0.5, size=100)

#data2 = bernoulli.rvs(p=0.5, size=100)

# Plot the histograms
plt.hist(data1, label='100 Samples', alpha = 0.5)
#plt.hist(data2, label='1000 Samples')

# Add a legend
plt.legend()

# Display the plot
plt.show()