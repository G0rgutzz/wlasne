import numpy as np
import matplotlib.pyplot as plt

def euler_method(x0, y0, h, N):
    x_values = [x0 + i * h for i in range(N+1)]
    y_values = [y0]

    for i in range(N):
        x_n = x_values[i]
        y_n = y_values[i]
        y_next = y_n + h * ((np.sqrt(x_n**2))/x_n**2 - y_n/x_n)
        y_values.append(y_next)

    return x_values, y_values

# Ustawienia początkowe
x0 = 0.1  # początkowa wartość x
y0 = 1.0  # warunek początkowy y(x0)
h = 0.05  # krok czasowy
N = 5  # liczba iteracji

# Rozwiązanie równania różniczkowego
x_values, y_values = euler_method(x0, y0, h, N)

# Wykres
plt.plot(x_values, y_values, label='Metoda Eulera')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Rozwiązanie numeryczne równania różniczkowego')
plt.legend()
plt.show()