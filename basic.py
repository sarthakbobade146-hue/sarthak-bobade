import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

operations = {
    "Addition": a + b,
    "Subtraction": a - b,
    "Multiplication": a * b,
    "Division": a / b
}

for name, result in operations.items():
    print(f"{name}: {result}")