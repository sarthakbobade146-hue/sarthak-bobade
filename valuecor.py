import numpy as np

a = np.array([6, 7, 8])
b = np.array([2, 3, 4])

corr = np.corrcoef(a, b)[0, 1]
print("Correlation:", corr)