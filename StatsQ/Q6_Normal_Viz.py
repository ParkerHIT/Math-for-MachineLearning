#Normal distribution
#On to the most recognizable and useful distribution of the bunch:
#the normal or Gaussian distribution.
#the bell-curve shape and
#the normal distribution
#along with the central limit theorem
#enables us to perform hypothesis tests.


#Do the below results make sense in the context of the 68-95-99.7 rule?

#Generate the data for the distribution by using the rvs() function
#with size set to 1000; assign it to the data variable.
import matplotlib.pyplot as plt

# Generate normal data
from scipy.stats import norm
data = norm.rvs(size=1000)

# Plot distribution
#examine the shape of the distribution.
plt.hist(data)
plt.show()

#Given a standardized normal distribution,
#what is the probability of an observation greater than 2?
# Compute and print true probability for greater than 2
true_prob = 1 - norm.cdf(2)
print(true_prob) # 0.0228

# Compute and print sample probability for greater than 2
sample_prob = sum(obs > 2 for obs in data) / len(data)
print(sample_prob) # 0.018

