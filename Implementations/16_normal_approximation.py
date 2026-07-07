import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

n = 400
p = 0.5

mu = n * p
sigma = np.sqrt(n * p * (1 - p)) 

print(f"Calculated Parameters -> Mean (mu): {mu} | Standard Deviation (sigma): {sigma}\n")

x_range = np.arange(150, 250)

binomial_probs = binom.pmf(x_range, n, p)

normal_curve = norm.pdf(x_range, mu, sigma)

area_prob = norm.cdf(210, mu, sigma) - norm.cdf(190, mu, sigma)
print(f"Probability of getting between 190 and 210 heads: {area_prob * 100:.2f}%")

plt.figure(figsize=(10, 5))

plt.bar(x_range, binomial_probs, color='orange', alpha=0.6, label="Binomial Distribution Bars")
plt.plot(x_range, normal_curve, color='blue', linewidth=2, label="Approximated Normal Curve (Bell shape)")

plt.title("Normal Approximation to Binomial (n=400 Flips Exercise)")
plt.xlabel("Number of Successes (Heads)")
plt.ylabel("Probability Density")
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()