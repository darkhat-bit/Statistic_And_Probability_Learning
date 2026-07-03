import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Unfair Die Simulation
faces = [1, 2, 3, 4, 5, 6]
probs = [1/6, 0, 1/6, 1/6, 1/6, 1/3]

print("Sum of probabilities:", sum(probs)) 

results = np.random.choice(faces, size=10000, p=probs)

print("First 20 rolls:", results[:20])
print()

series = pd.Series(results)
observed_counts = series.value_counts().sort_index()
observed_probs = observed_counts / len(series)

print("Observed probabilities:")
print(observed_probs)
print()

theoretical_probs = pd.Series(probs, index=faces)
print("Theoretical probabilities:")
print(theoretical_probs)


plt.figure(figsize=(8,5))
plt.hist(results, bins=np.arange(1,8)-0.5, density=True, 
          edgecolor='black', rwidth=0.8, color='skyblue', label='Experimental')
plt.plot(faces, probs, 'ro-', linewidth=2, label='Theoretical')  # theoretical ko line se overlay karo
plt.xticks([1,2,3,4,5,6])
plt.xlabel("Die Face")
plt.ylabel("Probability")
plt.title("Unfair Die: Experimental vs Theoretical Distribution")
plt.legend()
plt.show()