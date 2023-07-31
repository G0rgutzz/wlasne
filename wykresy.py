import pylab
# funkcja postaci ai*x^i+a(i-1)*x^(i-1)+...+a1*x+a0
funkcja = []
y = []
k = 0
j = 0
n = 0
m = 0
b = int(input("podaj dolną granicę dziedziny: "))
c = int(input("podaj górną granicę dziedziny: "))
if b <= c:
    x = range(b, c+1)
else:
    x = range(c, b+1)
i = int(input("podaj ilość współczynników: "))
for j in range(i):
    a = float(input("Podaj %s. współczynnik: " % (j+1)))
    for k in x:
        funkcja.append(a*(pow(k, (i-j-1))))
    j = j+1
while n < len(x):
    suma = []
    suma1 = []
    for m in range(i):
        suma = funkcja[n+m*len(x)]
        suma1.append(suma)
        m = m+1
    suma2 = sum(suma1)
    y.append(suma2)
    n = n+1
# print(funkcja)
# print(y)
pylab.plot(x, y)
pylab.title('Wykres f(x)')
pylab.grid(True)
pylab.show()
