import matplotlib.pyplot as plt
from random import *
# Transformations
def trans_1(x, y):
    x1 = 0.5 * x
    y1 = 0.5 * y
    return x1, y1
def trans_2(x, y):
    x1 = 0.5 * x + 0.5
    y1 = 0.5 * y + 0.5
    return x1, y1
def trans_3(x, y):
    x1 = 0.5 * x + 1
    y1 = 0.5 * y
    return x1, y1

def transpicker(x1, y1):
    rand = randint(0,2)
    transformations = [trans_1, trans_2, trans_3]
    transfunc = transformations[rand]
    x, y = transfunc(x1, y1)
    return x, y

# Draw Function

def draw_start(n):
    x = [0]
    y = [0]
    x1, y1 = 0, 0
    for i in range(n):
        x1, y1 = transpicker(x1, y1)
        x.append(x1)
        y.append(y1)
    return x, y

n = int(input('Number of Triangles: '))
x, y = draw_start(n)
plt.plot(x, y, 'o', markersize = 5)
plt.title('Sierpinski Trianagle with {0} points'.format(n))
plt.show()
