# Import the required libraries
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Generate random dataset with approximate normal distribution
norm_data = np.random.normal(loc=0, scale=1, size=500)

# Create Q-Q plot with 45-degree line (reference line)
sm.qqplot(norm_data, line='45')
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Sample Quantiles")
plt.show()

