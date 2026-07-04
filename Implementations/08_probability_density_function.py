"""

OBJECTIVE: Probability Density Function (PDF) Integration & Normalization
AI/ML LINK: Used in Continuous action spaces in Reinforcement Learning 
            and token logit scaling in LLMs.

CORE THEORY CONCEPT:
1. Continuous Space Paradox: P(X = exact_value) is always 0 because a geometric 
   line has a width of 0. We always measure intervals (ranges).
2. Normalization Axiom: Total area under a valid PDF must equal 1.0. If the area 
   deviates, we divide the function outputs by the total area to normalize.

"""
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define continuous range for simulation (e.g., using np.linspace)
X = np.linspace(0, 5, num=1000)

# Step 2: Define your raw mathematical probability density curve
raw_pdf = X * np.exp(-X)

# Step 3: Calculate the total area under the curve to verify validation
total_area = np.trapezoid(raw_pdf, X) 
print("Total Area Before Normalizing:", total_area)

# Step 4: [CRITICAL STEP] If total_area != 1.0, divide raw values by total_area to normalize
normalize_pdf = raw_pdf / total_area
new_area = np.trapezoid(normalize_pdf, X)
print("Total Area After Normalization:", new_area)

# Step 5: The exact probability of a single point will always be 0. We will calculate the area of a range (e.g., 1.9 to 2.1).
exact_point_prob = 0.0

# Range(interval)
lower_bound = 1.9
upper_bound = 2.1

# data filter between 1.9 to 2.1
interval_mask = (X >= lower_bound) & (X <= upper_bound)
X_interval = X[interval_mask]
pdf_interval = normalize_pdf[interval_mask]

# area between the taken interval
interval_prob = np.trapezoid(pdf_interval, X_interval)
print(f"Rain 1.9 se 2.1 inches ke beech hone ki probability: {interval_prob:.4f}")


# Ploting on graph(Matplotlib)
plt.figure(figsize=(10,5))
plt.plot(X, normalize_pdf, label="Probability Density Function (PDF)", color='blue')
plt.fill_between(X_interval, pdf_interval, color="orange", alpha=0.5, label="Interval (1.9 to 2.1)")

plt.title("Continuous Random Variable - Rain PDF Simulation")
plt.xlabel("Rain (Inches)")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.show()