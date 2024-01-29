# Import necessary libraries
import numpy as np
import pandas as pd
from scipy.stats import zscore
import seaborn as sns
import matplotlib.pyplot as plt

# Generate or load your dataset
data = pd.DataFrame({'col1': [1, 2, 3, 4, 5, 6, 6.2, 8, 1000]})  # Example dataset

# Method 1: Z-score
z_scores = np.abs(zscore(data))
print(z_scores)
outliers_z = data[(z_scores > 3).any(axis=1)]
print(outliers_z)

# Method 2: Interquartile Range (IQR)
q1 = data.quantile(0.25)
q3 = data.quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers_iqr = data[((data < lower_bound) | (data > upper_bound)).any(axis=1)]
print(outliers_iqr)


# Create a notched box plot with customized line width
plt.boxplot(data, notch=True, widths=0.5)
plt.show()