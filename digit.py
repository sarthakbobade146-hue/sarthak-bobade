import math

n = int(input("Enter a number: "))

if n >= 0 and n <= 9:
    print("Square =", n**2)

elif n >= 10 and n <= 99:
    print("Square root =", math.sqrt(n))

elif n >= 100 and n <= 999:
    print("Cube root =", n**(1/3))

else:
    print("Number not in range")