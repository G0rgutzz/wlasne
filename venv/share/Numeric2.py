import numpy as np
import matplotlib.pyplot as plt

def runge_kutta(h, x_range, initial_conditions):
    x_values = np.arange(x_range[0], x_range[1] + h, h)
    y_values = []
    v_values = []

    y, v = initial_conditions

    for x in x_values:
        y_values.append(y)
        v_values.append(v)

        k1y = h * v
        k1v = h * (-v*(x**2+1)-(x**2)-y*x)
        print(f"k1v {k1v}, k1y {k1y}")

        k2y = h * (v + 0.5 * k1v)
        k2v = h * (-(v + 0.5 * k1y)*((x+0.5*h)**2+1)-(x+0.5*h)**2-(y+0.5*k1y)*(x+0.5*h))
        print(f"k2v {k2v}, k2y {k2y}")
        k3y = h * (v + 0.5 * k2v)
        k3v = h * (-(v + 0.5 * k2y)*((x+0.5*h)**2+1)-(x+0.5*h)**2-(y+0.5*k2y)*(x+0.5*h))
        print(f"k3v {k3v}, k3y {k3y}")
        k4y = h * (v + k3v)
        k4v = h * (-(v + k3y)*((x+h)**2+1)-(x+h)**2-(y+k3y)*(x+h))
        print(f"k4v {k4v}, k1y {k4y}")
        y = y + (1/6) * (k1y + 2*k2y + 2*k3y + k4y)
        v = v + (1/6) * (k1v + 2*k2v + 2*k3v + k4v)

    return x_values, y_values, v_values

# Warunki początkowe
initial_conditions = [2, 1]  # y(3)=2, y'(3)=1

# Rozwiązanie numeryczne
h = (8 - 3) / 5  # Pięć kroków w przedziale (3, 8)
x_range = (3, 8)
x_values, y_values, v_values = runge_kutta(h, x_range, initial_conditions)

# Wykresy
plt.plot(x_values, y_values, label='y(x)')
plt.plot(x_values, v_values, label="y'(x)")
plt.xlabel('x')
plt.legend()
plt.show()
