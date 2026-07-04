import numpy as np

n = 5 # chances
p = 0.5 # probability of having heads or tails

# math combination logic function
def combination_logic(x, y):
    x_fact = 1
    y_fact = 1
    x_y_fact = 1

    for i in range(x):
        x_fact *= i+1
    
    if y == 0 or y == 1:
        y_fact = 1
    else:
        for i in range(y):
            y_fact *= i+1
    if x-y == 0 or x-y == 1:
        x_y_fact = 1
    else:
        for i in range(x-y):
            x_y_fact *= i+1
    ans = x_fact/(y_fact*x_y_fact)
    return ans

# total outcomes we have 2 choice(H & T) and 5 chances
total_outcomes = 32

# possible values that how many time heads are there
prob_array = np.zeros(6)
for i in range(6):
    prob_array[i] = combination_logic(n, i) * (1/total_outcomes)

print("Har case ki probability (0 se 5 heads):")
print(prob_array)

total_sum = np.sum(prob_array)
print(f"Saari probabilities ka total sum: {total_sum}")


