#Problem: You're working with a website and want to test for a difference in conversion rate.
#Before you begin the experiment, you must decide how many samples you'll need per variant using 5% significance and 95% power.

#Power analysis involves four moving parts:

#Sample size
#Effect size
#Minimum effect
#Power


#1. Standardize the effect of a conversion rate increase from 20% to 25% success using the proportion_effectsize() function.
# Standardize the effect size
from statsmodels.stats.proportion import proportion_effectsize
std_effect = proportion_effectsize(.20, .25)

# Assign and print the needed sample size
from statsmodels.stats.power import  zt_ind_solve_power
sample_size = zt_ind_solve_power(effect_size=std_effect, nobs1=None, alpha=.05, power=.95)
print(sample_size)

