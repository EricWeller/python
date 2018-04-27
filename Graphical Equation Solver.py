from sympy.plotting import plot
from sympy import Symbol, sympify, solve


def plot_expression(expr):

    y = Symbol('y')
    solutions = solve(expr, y)
    expr_y = solutions[0]
    plot(expr_y)

if __name__=='__main__':

    expr = input('Enter Expression in terms of x and y: ')
    try:
        expr = sympify(expr)
    except SympifyError:
        print('Invalid Input')
    else:
        plot_expression(expr)
