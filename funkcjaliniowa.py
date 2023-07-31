import pylab
a=float(input("Podaj współczynnik a: "))
b=float(input("Podaj współczynnik b: "))
x=range(-10,11)
y=[]
for i in x:
    y.append(a*i+b)
pylab.plot(x, y)
pylab.title('Wykres f(x) = a*x - b')
pylab.grid(True)
pylab.show()
