import scipy.stats as stats
import math
 
# Given values
sample_mean = 240
sample_std_dev = 25
sample_size = 10
confidence_level = 0.95
 
# DF
df = sample_size - 1
 
# Significance level (α)
alpha = (1 - confidence_level) / 2
 
# t-value from the t-distribution table
t_value = stats.t.ppf(1 - alpha, df)
 
margin_of_error = t_value * (sample_std_dev / math.sqrt(sample_size))
 
lower_limit = sample_mean - margin_of_error
upper_limit = sample_mean + margin_of_error
 
print(f"Confidence Interval: ({lower_limit}, {upper_limit})")