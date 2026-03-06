"""
Day 43 Activity: Probability Computation with SciPy
Tasks:
1) Compute CDF-based probability for a range
2) Use PPF for quantiles
3) Verify with Monte Carlo
"""

import numpy as np
from scipy import stats

#Task 1: Compute CDF-based probability for a range
# Define parameters for a normal distribution
mu, sigma = 0, 1  # mean and standard deviation
# Define the range for which we want to compute the probability
a, b = -1, 1
# Compute the CDF values at a and b
cdf_a = stats.norm.cdf(a, loc=mu, scale=sigma)
cdf_b = stats.norm.cdf(b, loc=mu, scale=sigma)

# Compute the probability P(a <= X <= b)
probability = cdf_b - cdf_a
print(f"P({a} <= X <= {b}) = {probability}")
#Task 2: Use PPF for quantiles
# Define a quantile
quantile = 0.95
# Compute the value corresponding to the quantile
quantile_value = stats.norm.ppf(quantile, loc=mu, scale=sigma)
print(f"The value at the {quantile*100}th percentile is: {quantile*100}% = {quantile_value}")

#Task 3: Verify with Monte Carlo
# Define parameters for a normal distribution
mu, sigma = 0, 1  # mean and standard deviation
# Define the range for which we want to compute the probability
a, b = -1, 1
# Compute the CDF values at a and b
cdf_a = stats.norm.cdf(a, loc=mu, scale=sigma)
cdf_b = stats.norm.cdf(b, loc=mu, scale=sigma)
# Generate a large number of random samples from the normal distribution
samples = np.random.normal(loc=mu, scale=sigma, size=1000000)
# Compute the proportion of samples that fall within the range [a, b]
monte_carlo_prob = np.mean((samples >= a) & (samples <= b))
print(f"Monte Carlo estimate of P({a} <= X <= {b}) = {monte_carlo_prob}")


# TODO: Define distribution
# TODO: Compute P(a<=X<=b)
# TODO: Compare with Monte Carlo
