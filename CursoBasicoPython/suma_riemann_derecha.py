import numpy as np
import matplotlib.pyplot as plt
from sympy import integrate
from sympy.abc import w


def riemann_right():
    def f(x): return ((((2*x)/7)-1)**3)+2
    z = ((((2*w)/7)-1)**3)+2
    a = 0
    b = 3
    N = int(input("Ingrese número de particiones: "))
    x = np.linspace(a, b, N+1)
    x_derecha = x[1:]
    dx = (b-a)/N
    x_derecha = np.linspace(dx, b, N)
    suma_riemann_derecha = np.sum(f(x_derecha) * dx)
    print("Suma por la derecha: " + str(suma_riemann_derecha))
    print("Porcentaje de error: " +
          str((suma_riemann_derecha - integrate(z, (w, a, b)))*100) + "%")


if __name__ == '__main__':
    riemann_right()
