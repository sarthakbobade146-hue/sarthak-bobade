import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

def plot_pie(labels, sizes):
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Pie Chart")
    plt.axis('equal')
    plt.show()

labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [15, 30, 45, 10]

plot_pie(labels, sizes)