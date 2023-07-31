import numpy as np
import random
import pylab
n = int(input("Ile ruchów? "))
x1 = y1 = 0
x2 = y2 = 1
lx1 = [0]
ly1 = [0]
lx2 = [1]
ly2 = [1]
for i in range(0, n):
    rad = float(random.randint(0, 360))*np.pi/180  # losowanie kąta
    x1 = round(x1+np.cos(rad), 3)
    lx1.append(x1)
    y1 = round(y1+np.sin(rad), 3)  # zapisywanie przesunięcia
    ly1.append(y1)
for j in range(0, n):
    rad = float(random.randint(0, 360))*np.pi/180  # losowanie kąta
    x2 = round(x2+np.cos(rad), 3)
    lx2.append(x2)
    y2 = round(y2+np.sin(rad), 3)  # zapisywanie przesunięcia
    ly2.append(y2)
s1 = round(np.fabs(np.sqrt((x1-0)**2+(y1-0)**2)), 3)
s2 = round(np.fabs(np.sqrt((x2-1)**2+(y2-1)**2)), 3)
# print("Końcowa wartość przesunięcia wynosi: ", s)
xl1 = [0, x1]
yl1 = [0, y1]
xl2 = [1, x2]
yl2 = [1, y2]
pylab.plot(lx1, ly1, "o:", color="green", linewidth=2, alpha=0.5)
pylab.plot(xl1, yl1, color="red")
pylab.plot(lx2, ly2, "o:", color="blue", linewidth=1.5, alpha=0.7)
pylab.plot(xl2, yl2, color="black")
pylab.legend(["1. cząstka", "Przemieszczenie: "+str(s1), "2. cząstka", "Przemieszczenie: "+str(s2)], loc="upper left")
pylab.xlabel("x")
pylab.ylabel("y")
pylab.title('Ruchy Browna')
pylab.grid(True)
pylab.show()
