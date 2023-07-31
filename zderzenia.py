import numpy as np
import random
import pylab
import pygame
import pygame.locals
'''dobudować cały interfejs, żeby prędkość ustalać na poziomie aplikacji, bez wpisywania'''
# ----------------------------------------------------------------------
k = int(input("Podaj ilość cząstek: "))
n = int(input("Ile ruchów? "))
v = float(input("Prędkość początkowa: "))
bazax = []
bazay = []
for i in range(k):
    bazax.append(1920*(i+1)/k)  # poprawić, albo zmienić na związanie z wysokością aplikacji
    bazay.append(1080*(i+1)/k)


class Plansza(object):  # plansza do gry
    def __init__(self, width, height):
        # konstruktor planszy do gry, przygotowuje okienko :param width: :param height:
        self.surface = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption("Symulacja zderzeń")

    def draw(self, *args):  # Rysuje okno gry :param args: lista obiektów do narysowania
        background = (230, 255, 255)
        self.surface.fill(background)
        for drawable in args:
            drawable.draw_on(self.surface)
        # dopiero w tym miejscu następuje faktyczne rysowanie
        # w oknie gry, wcześniej tylko ustalaliśmy co i jak ma zostać narysowane
        pygame.display.update()


class Drawable(object):  # klasa bazowa dla rysowanych obiektów
    def __init__(self, width, height, x, y, color=(0, 255, 0)):
        self.width = width
        self.height = height
        self.color = color
        self.surface = pygame.Surface([width, height], pygame.SRCALPHA, 32).convert_alpha()
        self.rect = self.surface.get_rect(x=x, y=y)  # do zmiany, musi być inna wielkość cząstek

    def draw_on(self, surface):
        surface.blit(self.surface, self.rect)


class Zderzenia(object):  # cała symulacja zderzeń, zbiera wszystko do kupy
    def __init__(self, width, height):
        pygame.init()
        self.board = Plansza(width, height)
        self.czastka = Czastka(1, 1, bazax[i], bazay[i])


class Czastka(Drawable):  # opis cząstek
    def __init__(self, width, height, x, y, color=(255, 0, 0), x_speed=v, y_speed=v):
        super(Czastka, self).__init__(width, height, x, y, color)
        pygame.draw.ellipse(self.surface, self.color, [0, 0, self.width, self.height])
        self.x_speed = x_speed
        self.y_speed = y_speed
        for j in range(k):
            self.startx.append(bazax[j])  # powinno działać jako tablica z wartościami startowymi dla cząstek
            self.starty.append(bazay[j])  # sprawdzić i dopracować

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1  # odbicia cząstek

    def move(self, board, *args):  # przesuwa o wektor prędkości
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.x < 0 or self.rect.x > board.surface.get_width()-self.surface.get_width():
            self.bounce_x()
        if self.rect.y < 0 or self.rect.y > board.surface.get_height()-self.surface.get_height():
            self.bounce_y()


Zderzenia(1920,1080)
'''
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
pylab.show()'''
