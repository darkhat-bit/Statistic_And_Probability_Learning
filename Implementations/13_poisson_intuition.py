import numpy as np

lambda_val = 9.3    
k = 3              

def get_combos(n_val, k_val):
    import math
    return math.factorial(n_val) / (math.factorial(k_val) * math.factorial(n_val - k_val))

n_min = 60
p_min = lambda_val / n_min
prob_minutes = get_combos(n_min, k) * (p_min**k) * ((1 - p_min)**(n_min - k))

n_sec = 3600
p_sec = lambda_val / n_sec
prob_seconds = get_combos(n_sec, k) * (p_sec**k) * ((1 - p_sec)**(n_sec - k))

print("Granularity Accuracy Comparison:")
print(f"Minutes Level Model (n=60) Probability:   {prob_minutes:.6f}")
print(f"Seconds Level Model (n=3600) Probability: {prob_seconds:.6f}")