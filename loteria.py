import random
nazwisko=[]
numer=[]
i=0
k=0

k=int(input("Ilu uczniów jest w klasie: "))
for i in range (k):
    imie=(input("Podaj imię i nazwisko %s ucznia: "%(i+1)))
    nazwisko.append(imie)
    numer.append(i+1)
    i=i+1
liczba=random.randint(1,k)

print(nazwisko,"\n",numer,"\n",nazwisko[liczba-1])

exit()
