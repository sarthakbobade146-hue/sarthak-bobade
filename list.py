lst = [10, 20, 30, 40]
key = int(input("Enter number to search: "))

if key in lst:
    print("Found at position", lst.index(key))
else:
    print("Not found")