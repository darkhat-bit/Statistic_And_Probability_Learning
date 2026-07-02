import timeit
import numpy as np

def method_1_alternate_formula():
    obj = np.array([45, 50, 50, 52, 47, 500])
    total_element = int(len(obj))
    sum_x = 0
    sum_x_squared = 0
    for i in range(total_element):
        sum_x += obj[i]
        sum_x_squared  += (obj[i])**2

    mean_of_square = sum_x_squared / total_element
    square_of_mean = (sum_x/total_element)**2
    obj_variance = mean_of_square - square_of_mean

def method_2_deviation_formula():
    obj = np.array([45, 50, 50, 52, 47, 500])
    total_element = int(len(obj))
    sum_squared_deviation = 0
    obj_mean = np.mean(obj)
    for i in range(total_element):
        sum_squared_deviation  += (obj[i] - obj_mean)**2

    obj_variance = sum_squared_deviation / total_element

runs = 1

time_method_1 = timeit.timeit(method_1_alternate_formula, number=runs)
time_method_2 = timeit.timeit(method_2_deviation_formula, number=runs)

print(f"Method 1 (Alternate Formula) Time: {time_method_1:.6f} seconds")
print(f"Method 2 (Deviation Formula) Time: {time_method_2:.6f} seconds")
