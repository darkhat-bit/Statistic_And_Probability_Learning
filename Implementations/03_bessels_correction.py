import numpy as np
import pandas as pd

obj = np.array([45, 50, 50, 52, 47, 500])

# using n-1 not n in denominator for sample variance
print("Sample Variance using numpy(ddof=1 manually set):", np.var(obj, ddof=1))
print("Sample Variance using pandas(ddof=1 auto set):", pd.Series(obj).var())