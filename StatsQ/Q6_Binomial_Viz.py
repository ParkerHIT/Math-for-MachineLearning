#Binomial Distribution
#The binomial distribution is used to model the number of successful outcomes in trials
#where there is some consistent probability of success.

#For this exercise, consider a game where you are trying to make a ball in a basket.
#You are given 10 shots and you know that you have an 80% chance of making a given shot.
#To simplify things, assume each shot is an independent event.

import matplotlib.pyplot as plt
# Generate binomial data
from scipy.stats import binom
data = binom.rvs(n=10, p=0.8, size=1000)

# Plot the distribution
plt.hist(data)
plt.show()

# Assign and print probability of 8 or less successes
prob1 = binom.cdf(k=8, n=10, p=0.8)
print(prob1)

# Assign and print probability of all 10 successes
prob2 = binom.pmf(k=10, n=10, p=0.8)
print(prob2)