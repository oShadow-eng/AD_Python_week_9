"""
Day 44 Activity: Log, Exp, Softmax
Tasks:
1) Implement stable softmax
2) Apply to score vector
3) Show sum of probabilities
"""

import numpy as np

#Task 1: Implement stable softmax
def softmax_stable(scores):
    """Compute the softmax of a vector of scores in a numerically stable way."""
    # Shift scores by the maximum value to prevent overflow
    shifted_scores = scores - np.max(scores)
    exp_scores = np.exp(shifted_scores)
    probabilities = exp_scores / np.sum(exp_scores)
    return probabilities

#Task 2: Apply to score vector
# Example score vector
scores = np.array([1.0, 2.0, 3.0, 4.0, 5.0])

# Compute softmax probabilities
probabilities = softmax_stable(scores)

# Print probabilities
print("Softmax probabilities:", probabilities)

#Task 3: Show sum of probabilities
print("Sum of probabilities:", np.sum(probabilities))

# TODO: Implement softmax_stable
# TODO: Apply to scores
