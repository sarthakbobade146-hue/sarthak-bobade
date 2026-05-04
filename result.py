marks = []

for i in range(5):
    m = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

if all(m >= 40 for m in marks):
    total = sum(marks)
    percentage = total / 5

    print("Percentage =", percentage)

    if percentage >= 75:
        print("Distinction")
    elif percentage >= 60:
        print("First Division")
    elif percentage >= 50:
        print("Second Division")
    else:
        print("Third Division")
else:
    print("Fail")