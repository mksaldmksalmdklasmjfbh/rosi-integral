def create_funcs(func):
    math_prefix = 'from math import *\n\n\ndef f_math(x):\n    return '
    sympy_prefix = 'from sympy import *\n\n\ndef f_sympy(x):\n    return '

    with open('function_math.py', 'w') as f:
        f.write(math_prefix)
        f.write(func)
        f.write('\n')

    with open('function_sympy.py', 'w') as f:
        f.write(sympy_prefix)
        f.write(func)
        f.write('\n')

    from function_math import f_math
    from function_sympy import f_sympy

    return f_math, f_sympy
