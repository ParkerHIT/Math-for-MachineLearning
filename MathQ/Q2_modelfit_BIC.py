#The Bayesian Information Criterion, often abbreviated BIC, is a metric that is used to
#compare the goodness of fit of different regression models.

#In practice, we fit several regression models to the same dataset and
#choose the model with the lowest BIC value as the model that best fits the data.

import statsmodels.api as sm

import pandas as pd
import numpy as np

# Set a seed for reproducibility
np.random.seed(0)

# Create a DataFrame with 100 rows and 4 columns
data = pd.DataFrame(np.random.rand(100, 4), columns=['Independent1', 'Independent2', 'Independent3', 'Target'])

# Print the first few rows of the DataFrame
print(data.head())

# Define the response variable y and predictor variables x
y = data['Target']
x = data[['Independent1', 'Independent2', 'Independent3']]

# Add a constant to the predictor variables
x = sm.add_constant(x)

# Fit the OLS regression model
model = sm.OLS(y, x).fit()

# View the BIC of the model
print(model.bic)