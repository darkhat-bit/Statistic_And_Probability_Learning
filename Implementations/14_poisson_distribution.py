import numpy as np
import matplotlib.pyplot as plt
import math

lambda_val = 9.0
max_cars = 25

k_values = np.arange(0, max_cars+1)

poisson_probabilities = np.zeros(len(k_values))

for k in k_values:
    numerator = (lambda_val**k) * np.exp(-lambda_val)
    denominator = math.factorial(k)
    poisson_probabilities[k] = numerator / denominator

print("Poisson Distribution Table Data:")
print(f"Exactly 2 cars passing probability: {poisson_probabilities[2]:.4f}\n")

print(f"Total Probabilities Sum: {np.sum(poisson_probabilities):.4f}")

plt.figure(figsize=(10, 5))
plt.bar(k_values, poisson_probabilities, color='blue', edgecolor='black', width=0.6, label=f"Poisson (lambda={lambda_val})")

plt.title("Poisson Process - Traffic Density Model")
plt.xlabel("Number of Cars Passing in an Hour (K)")
plt.ylabel("Probability")
plt.xticks(k_values)
plt.grid(axis='y', linestyle=':', alpha=0.5)
plt.legend()
plt.show()