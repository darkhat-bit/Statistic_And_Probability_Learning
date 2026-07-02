import numpy as np


obj = np.array([45, 50, 50, 52, 47, 500])

total_element = len(obj)
sum_squared_deviation = 0
obj_mean = np.mean(obj)

for i in range(total_element):
    sum_squared_deviation  += (obj[i] - obj_mean)**2

# Variance (population vs sample)
obj_variance = sum_squared_deviation / total_element
obj_sample_variance = sum_squared_deviation / (total_element-1)

# Standard Deviation = sqrt(variance)
standard_dev = (obj_variance)**0.5
sample_standard_dev = (obj_sample_variance)**0.5

print("Manually Calculated std for population:", round(standard_dev, 4))
print("Manually Calculated std for sample:", round(sample_standard_dev, 4))
print("Using numpy std for population:", round(np.std(obj, ddof=0), 4))
print("Using numpy std for sample:", round(np.std(obj, ddof=1), 4))