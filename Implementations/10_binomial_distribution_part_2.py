import numpy as np

# Basketball experiment lets have 6 trials and 
# have success rate of 30% and failure rate of 70%
n = 6
p = 0.3
q = 0.7
x_values = np.array([0,1,2,3,4,5,6])

# Pure math combination logic (nCr)
def combination_logic(x, y):
    x_fact = 1
    y_fact = 1
    x_y_fact = 1

    for i in range(x):
        x_fact *= (i + 1)

    if y == 0:
        y_fact = 1
    else:
        for i in range(y):
            y_fact *= (i + 1)
            
    diff = x - y
    if diff == 0:
        x_y_fact = 1
    else:
        for i in range(diff):
            x_y_fact *= (i + 1)
            
    ans = x_fact / (y_fact * x_y_fact)
    return ans

# Har scenario (0 se 6 baskets) ki probability array
prob_array = np.zeros(7)
for i in range(7):
    p_var = p**i
    q_var = q**(n-i)
    # Binomial Formula
    prob_array[i] = combination_logic(n, i) * p_var * q_var

print("Probability of all 7 cases:")
print(prob_array)

total_sum = np.sum(prob_array)
print("Sum of all the probability:", np.round(total_sum, 4))