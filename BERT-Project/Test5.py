import matplotlib.pyplot as plt

numbers = [1,-2,-1.6,0,6]

def bar_chart(numbers, labels, pos):
    plt.bar(pos, numbers, color='blue')
    plt.xticks(ticks=pos, labels=labels)
    plt.show()


labels = ['Electric', 'Solar', 'Diesel', 'Unleaded', "Watever"]
pos = list(range(5))
bar_chart(numbers, labels, pos)