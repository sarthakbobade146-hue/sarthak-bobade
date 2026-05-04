import numpy as np

a = np.array([[2, 3], [4, 5]])
b = np.array([[6, 7], [8, 9]])

operations = {
    "Addition": np.add(a, b),
    "Subtraction": np.subtract(a, b),
    "Division": np.divide(a, b),
    "Multiplication": np.multiply(a, b)
}

print("Matrix 1:\n", a)
print("Matrix 2:\n", b)

for name, result in operations.items():
    print(f"\n{name}:\n{result}")