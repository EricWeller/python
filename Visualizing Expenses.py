import matplotlib.pyplot as plt
objects = []
costs = []
def create_bar_chart(data, labels):
    num_bars = len(data)
    positions = range(1, (num_bars+1))
    plt.barh(positions, data, align='center')
    plt.yticks(positions, labels)
    plt.ylabel('Catagory')
    plt.xlabel('Costs')
    plt.title('Expenses')
    plt.grid()
    plt.show()
while True:
    object = input('Catagory: ')
    objects.append(object)
    cost = input('Cost: ')
    costs.append(cost)
    b = input("Type in (y/n) to use again? ")
    if str(b) == 'n':
        break
create_bar_chart(costs, objects)
