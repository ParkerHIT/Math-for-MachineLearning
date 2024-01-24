#The L1 loss function, also known as the Least Absolute Deviations (LAD) loss function,
#is used in Lasso regression to minimize the error,
#which is the sum of the absolute differences between the actual and predicted values.

import numpy as np

# Example of observed and predicted values
y_observed = np.array([3, 5, 7, 9])
y_predicted = np.array([2, 5, 8, 10])

# Calculate the L1 loss
l1_loss = np.sum(np.abs(y_observed - y_predicted))
print("L1 Loss:", l1_loss)