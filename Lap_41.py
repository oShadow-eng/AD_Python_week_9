"""
Day 41 Activity: Probability Basics
Tasks:
1) Simulate coin flips or dice rolls
2) Estimate event probabilities empirically
3) Compare to theoretical probabilities
"""

import numpy as np

#Task 1: Simulate coin flips or dice rolls
# Example: Simulate 1000 coin flips (1 for heads, 0 for tails)
num_trials = 1000
# Simulate coin flips
coin_flips = np.random.choice([0, 1], size=num_trials)

# Simulate dice rolls
dice_rolls = np.random.randint(1, 7, size=num_trials)

#Task 2: Estimate event probabilities empirically
# Example: Estimate probability of getting heads (1) in coin flips
prob_heads = np.mean(coin_flips)
# Example: Estimate probability of rolling a 6 in dice rolls
prob_six = np.mean(dice_rolls == 6)

print(f"Probability of getting heads (1) in coin flips: {prob_heads}")
print(f"Probability of rolling a 6 in dice rolls: {prob_six}")

#Task 3: Compare to theoretical probabilities
theoretical_prob_heads = 0.5
theoretical_prob_six = 1/6
print(f"Theoretical probability of getting heads (1) in coin flips: {theoretical_prob_heads}")
print(f"Theoretical probability of rolling a 6 in dice rolls: {theoretical_prob_six}")

# TODO: Choose coin or dice simulation
# TODO: Estimate probabilities using many trials
# TODO: Print results
