import numpy as np


obj = np.array([45, 50, 50, 52, 47, 500])

total_element = int(len(obj))
sum_squared_deviation = 0
obj_mean = np.mean(obj)
for i in range(total_element):
    sum_squared_deviation  += (obj[i] - obj_mean)**2

obj_variance = sum_squared_deviation / total_element

print("Manually Calculated:", obj_variance)
print("Using numpy:", np.var(obj, ddof=0))