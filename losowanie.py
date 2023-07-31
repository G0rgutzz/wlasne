import random
nazwisko = []
numer = []
liczby = []
wylosowane = []
j = 0

k = int(input("Ilu uczniów jest w klasie: "))
for i in range(k):
    imie = (input("Podaj imię i nazwisko %s ucznia: " % (i+1)))
    nazwisko.append(imie)
    numer.append(i+1)
    i = i+1
while len(liczby) < len(numer):
    liczba = random.randint(1, k)
    if liczba != j+1 and liczba not in liczby:
        liczby.append(liczba)
        los = nazwisko[liczba-1]
        wylosowane.append(los)
        j = j+1
    else:
        liczba = random.randint(1, k)

print(nazwisko, "\n", numer, "\n", liczby, "\n", wylosowane)

exit()
