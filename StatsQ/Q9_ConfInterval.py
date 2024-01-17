
#In this exercise, we'll practice implementing a confidence interval by hand,
#using no packages other than those imported.

#We have gone ahead and assigned the appropriate z-score for a 95% confidence interval and sample mean
#to the z_score and sample_mean variables to simplify things a bit.

from scipy.stats import sem, t
data = [1, 2, 3, 4, 5]
confidence = 0.95
z_score = 2.7764451051977987
sample_mean = 3.0


# Compute the standard error and margin of error
std_err = sem(data)
margin_error = std_err * z_score

# Compute and print the lower threshold
lower = sample_mean - margin_error
print(lower)

# Compute and print the upper threshold
upper = sample_mean + margin_error
print(upper)