from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)

#print simplify(sin(x)**2 + cos(x)**2)

#print simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))

#print simplify(gamma(x)/gamma(x - 2))

print simplify((x + 1)**2)
print expand((x + 1)**2)
