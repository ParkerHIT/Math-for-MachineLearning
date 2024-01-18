import numpy as np
# Create a NumPy array (Replace this with your array)
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, -35, 100])

# Calculate the first and third quartiles
Q1 = np.percentile(data, 25)
print("Quartile1", Q1)
Q3 = np.percentile(data, 75)
print("Quartile3",Q3)

# Calculate the IQR
IQR = Q3 - Q1
print("IQR",IQR)

# Define the lower and upper bounds to identify outliers
lower_bound = Q1 - 1.5 * IQR
print("LowerBound",lower_bound)
upper_bound = Q3 + 1.5 * IQR
print("UpperBound", upper_bound)

# Find the outliers
outliers = data[(data < lower_bound) | (data > upper_bound)]
print("Outliers:", outliers)

