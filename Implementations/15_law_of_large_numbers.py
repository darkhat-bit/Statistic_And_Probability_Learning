import numpy as np
import matplotlib.pyplot as plt

total_flips = 10000
expected_value = 0.5

raw_flips = np.random.randint(0, 2, size=total_flips)

running_heads_sums = np.cumsum(raw_flips)
trials_indices = np.arange(1, total_flips + 1)
sample_means = running_heads_sums / trials_indices

print("Simulation ke beech ke kuch sample means:")
print(f"10 flips ke baad average:     {sample_means[9]:.4f}")
print(f"100 flips ke baad average:    {sample_means[99]:.4f}")
print(f"10,000 flips ke baad average:  {sample_means[-1]:.4f}\n")

plt.figure(figsize=(10, 5))
plt.plot(trials_indices, sample_means, color='teal', label="Sample Mean (X_bar)")
plt.axhline(y=expected_value, color='red', linestyle='--', label=f"True Expected Value ({expected_value})")

plt.title("Law of Large Numbers - Convergence Simulation")
plt.xlabel("Number of Trials (n)")
plt.ylabel("Sample Mean Value")
plt.xscale('log')  
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()