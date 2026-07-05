import numpy as np
from scipy.special import comb

n = 1000
p = 0.4
q = 1 - p

manual_sum = 0
for k in range(n+1):
    prob_k = comb(n, k) * (p**k) * (q**(n-k))
    manual_sum += k * prob_k

print(f"System A (Manual Summation Process) Output: {manual_sum:.4f}")

shortcut_expected_value = n * p

print(f"System B (Algebraic Equation Shortcut) Output: {shortcut_expected_value:.4f}")