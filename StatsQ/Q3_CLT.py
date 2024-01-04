#Central Limit Theorem
#Generate a sample of 10 die rolls using the randint() function; assign it to a variable.

from numpy.random import randint

#Create a sample of 10 die rolls
small = randint(1,7,10)
print(small)

# Calculate and print the mean of the sample
small_mean = small.mean()
print(small_mean)

# Create a sample of 1000 die rolls
large = randint(1, 7, 10000)
print(large)

# Calculate and print the mean of the large sample
large_mean = large.mean()
print(large_mean)

#Why does CLT matter?

#Central limit theorem matters because it promises our sampling mean distribution will be normal,
#therefore we can perform hypothesis tests. More concretely, we can assess the likelihood that
#a given mean came from a particular distribution and then, based on this,
#reject or fail to reject our hypothesis. This empowers all of the A/B testing you see in practice.