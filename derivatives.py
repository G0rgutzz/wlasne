from math import *


def f(x):
    return sin(x)*cos(x)  # dowolna funkcja


def derivative(function, value):  # pochodna tej funkcji
    h = 0.000000000001  # krok h - musi być mały
    top = function(value+h) - function(value)  # poprawić, za słabo napisane
    bottom = h
    slope = top/bottom
    # Returns the slope to the third decimal
    return float("%.3f" % slope)
    # nie działa w mojej wersji, konieczne printowanie jak poniżej, żeby zobaczyć wyniki
    # zapewne zwraca wyniki do użycia przez inne moduły


print(f(pi/3))
print(derivative(f, pi/3))

