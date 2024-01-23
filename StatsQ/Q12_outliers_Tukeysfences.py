# Import necessary libraries
import numpy as np
import pandas as pd
from scipy.stats import zscore

# Generate or load your dataset
data = pd.DataFrame({'col1': [1, 2, 3, 4, 5, 6, 6.2, 8, 1000]})  # Example dataset

# Method 1: Z-score
z_scores = np.abs(zscore(data))
print(z_scores)
outliers_z = data[(z_scores > 3).any(axis=1)]

# Method 2: Interquartile Range (IQR)
q1 = data.quantile(0.25)
q3 = data.quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers_iqr = data[((data < lower_bound) | (data > upper_bound)).any(axis=1)]

# Method 3: Tukey's Fences
k = 1.5  # You can change the value of k as needed
lower_bound_tukey = q1 - k * iqr
upper_bound_tukey = q3 + k * iqr
outliers_tukey = data[((data < lower_bound_tukey) | (data > upper_bound_tukey)).any(axis=1)]

# Print the outliers for each method
print("Outliers using Z-score method:\n", outliers_z)
print("Outliers using IQR method:\n", outliers_iqr)
print("Outliers using Tukey's Fences method:\n", outliers_tukey)