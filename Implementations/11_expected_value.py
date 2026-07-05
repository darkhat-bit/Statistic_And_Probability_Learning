import numpy as np

n = 6
total_outcomes = 2**n

baskets = np.arange(0, 7)

probabilities = np.array([1/64, 6/64, 15/64, 20/64, 15/64, 6/64, 1/64])

print(f"Probabilities Validation Sum: {np.sum(probabilities):.4f}\n")

weighted_products = baskets * probabilities
expected_value = np.sum(weighted_products)

print("Step-by-step Weighted Multiplications:")
for k, prob, prod in zip(baskets, probabilities, weighted_products):
    print(f"Heads: {k} | Prob: {prob:.4f} | Weighted Option: {prod:.4f}")

print(f"\nFinal Expected Value E(X) [Population Mean]: {expected_value:.4f}")