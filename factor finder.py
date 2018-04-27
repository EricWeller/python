from sympy import Symbol
from sympy import factor
x = Symbol('x')
y = Symbol('y')
expres = x

while True:
    expres = input('Input a expression example (x**2)-x-2:  ')

    break
try:
    print(factor(expres))
except ValueError:
    print('Are you sure thats an expression?')
