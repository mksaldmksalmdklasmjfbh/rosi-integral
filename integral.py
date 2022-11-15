import matplotlib.pyplot as plt
from numpy import linspace, vectorize
from sympy import Symbol, integrate

from crutch import create_funcs


f_math, f_sympy = create_funcs(input('Введите функцию для интегрирования: '))
left = int(input('Введите левую границу: '))
right = int(input('Введите правую границу: '))
freq = int(input('Введите частоту дискретизации, Гц: '))

f = vectorize(f_math)

try:
    x = Symbol('x')
    integral = integrate(f_sympy(x), (x, left, right))

    x = linspace(left, right, freq)
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    plt.plot(x, f(x))
    plt.grid(True)
    plt.fill_between(x, f(x))
    plt.title(f'{str(integral)} = {float(integral)}')
    plt.show()
except (TypeError, ValueError, ZeroDivisionError):
    print('Интеграл не может быть найден на данном отрезке, либо в данном числовом пространстве.\n'
          'Попробуйте скорректировать ввод.')
