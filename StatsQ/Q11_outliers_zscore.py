import numpy as np
from scipy import stats

# Generate random data
np.random.seed(42)
data = np.random.normal(0, 1, 100)
print(data)
data[90:] += 5  # Introduce outliers
print(data)
# Calculate z-scores
z_scores = np.abs(stats.zscore(data))
threshold = 3
outliers = np.where(z_scores > threshold)

print("Outlier indices:", outliers)