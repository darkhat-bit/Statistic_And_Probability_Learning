import numpy as np
import matplotlib.pyplot as plt

obj = np.array([45, 50, 50, 52, 47, 500]);
# Mean Calculation
sum_total = 0
total_element = len(obj)
for i in range(total_element):
    sum_total += obj[i]

obj_mean = sum_total/total_element
print("Manual mean calculated:", obj_mean)
print("Using numpy:", np.mean(obj))
print()


# Median Calculation\
for j in range(total_element):
    for i in range(total_element-1):
        if obj[i] > obj[i+1]:
            temp = obj[i]
            obj[i] = obj[i+1]
            obj[i+1] = temp

if (total_element % 2 == 0):
    mid = int(total_element / 2)
    a = mid - 1
    b = mid
    obj_median = (obj[a] + obj[b])/2
else :
    mid = int(total_element/2)
    obj_median = obj[mid]

print("Manual median calculated:", obj_median)
print("Using numpy:", np.median(obj))
print()

# Mode Calculation
freq = np.zeros(6, dtype=int)
for i in range(total_element):
    x = obj[i]
    for j in range(total_element):
        if obj[j] == x:
            freq[i] += 1

if np.argmax(freq) > 1:
    print("Mode Calculated:", obj[np.argmax(freq)])


# Plotting histogram with mean and median lines
plt.figure(figsize=(8, 5))
plt.hist(obj, bins=6, color='skyblue', edgecolor='black')
plt.axvline(obj_mean, color='red', linestyle='--', linewidth=2, label=f'Mean = {obj_mean:.2f}')
plt.axvline(obj_median, color='green', linestyle='-', linewidth=2, label=f'Median = {obj_median:.2f}')
plt.title('Effect of Outlier on Mean vs Median')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()