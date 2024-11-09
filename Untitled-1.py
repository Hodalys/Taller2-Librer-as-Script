import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def f(x):
    return x**3 - 3*x**2 + x - 1

# Crear un rango de valores para x
x = np.linspace(-2, 3, 400)
y = f(x)

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = x^3 - 3x^2 + x - 1', color='blue')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.title('Gráfica de y = x^3 - 3x^2 + x - 1')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()

from spicy.optimize import Newton
x0 = 100
x_r = newton(f, x0)
x_r