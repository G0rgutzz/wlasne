import pylab
#x=x1= pylab.arange(-10, 10.5, 0.5)
x1= pylab.arange(-10, 0.5, 0.5)
x2= pylab.arange(0, 10.5, 0.5)
a=int(input("Podaj współczynnik a: "))
y1=[i/-3+a for i in x1]
y2=[i*i/3 for i in x2]

#pylab.plot(x[:len(y1)], y1, x[-len(y2):], y2)
pylab.plot(x1, y1, x2, y2)
pylab.title('Wykres f(x)')
pylab.grid(True)
pylab.show()