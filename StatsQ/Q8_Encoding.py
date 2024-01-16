


import pandas as pd
from sklearn import preprocessing

laptop = pd.DataFrame()
laptop['Company'] = ['A','B','C','D','E','A','A','C','D']

# Create the encoder and print our encoded new_vals
encoder = preprocessing.LabelEncoder()
new_vals = encoder.fit_transform(laptop['Company'])
print(new_vals)

laptops2 = laptop.copy()

# One-hot encode Company for laptops2
laptops2 = pd.get_dummies(data=laptops2, columns=['Company'])
print(laptops2.head())