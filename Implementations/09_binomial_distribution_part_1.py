import numpy as np
import matplotlib.pyplot as plt

n = 5 # chances
p = 0.5 # probability of having heads or tails
x_values = np.array([0,1,2,3,4,5])
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



plt.figure(figsize=(8,5))
plt.bar(x_values, prob_array, color='skyblue', edgecolor='black', width=0.6, label="Discrete Binomial")

plt.title("Binomial Probability Distribution (5 Coin Flips)")
plt.xlabel("Number of Heads (Random Variable X)")
plt.ylabel("Probability")
plt.xticks(x_values) 
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.show()