import numpy as np

a = np.array([[4, 5], [6, 7]])
b = np.array([[8, 9], [10, 11]])

operations = {
    "Addition": a + b,
    "Subtraction": a - b,
    "Division": a / b,
    "Multiplication": a * b
}

print("Matrix 1:\n", a)
print("Matrix 2:\n", b)

for name, result in operations.items():
    print(f"\n{name}:\n{result}")

print("\nTotal Sum:", a.sum())
print("Column-wise Sum:", a.sum(axis=0))
print("Row-wise Sum:", a.sum(axis=1))
print("Transpose:\n", a.T)