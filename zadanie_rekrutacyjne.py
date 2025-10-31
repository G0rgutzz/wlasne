import datetime
"""Wyznacz medianę wydatków do pierwszej niedzieli (włącznie) każdego miesiąca
    Należy użyć tylko funkcji/modułów ze standardowej biblioteki (np. math).
    Po przesłaniu poprawnego wyniku:
        przesłany plik jest finalnym rozwiązaniem
        uruchomione zostaną testy automatyczne (na różnych danych) badające zużycie 
        pamięci i procesora dla funkcji solution
    Zadanie może zostać wykonane w języku Python lub JavaScript.
    Wynik to jedna liczba dla danych spełniających kryteria lub null.
"""
expenses = {
    "2023-01": {
        "01": {
            "food": [ 22.11, 43, 11.72, 2.2, 36.29, 2.5, 19 ],
            "fuel": [ 210.22 ]
        },
        "09": {
            "food": [ 11.9 ],
            "fuel": [ 190.22 ]
        }
    },
    "2023-03": {
        "07": {
            "food": [ 20, 11.9, 30.20, 11.9 ]
        },
        "04": {
            "food": [ 10.20, 11.50, 2.5 ],
            "fuel": []
        }
    },
    "2023-04": {}
}

def create_date (firstkey, secondkey):
    year = int(firstkey[:4])  # tworzę datę na podstawie otrzymanych kluczy ze słownika
    month = int(firstkey[-2:])
    day = int(secondkey)
    date1 = datetime.date(year, month, day)
    return date1

def first_sunday(year, month):
    firstday = datetime.date(int(year), int(month), 1)  # pierwszy dzień miesiąca
    daystosunday = (6 - firstday.weekday()) % 7 # Ilość dni do najbliższej niedzieli
    first_sunday_date = firstday + datetime.timedelta(days=daystosunday)  # pierwsza niedziela miesiąca
    return first_sunday_date


def calculate_median(values):
    n = len(values)  # Obliczanie mediany
    if n == 0:
        return None
    elif n % 2 == 1:
        median = values[n // 2]  # Mediana dla nieparzystej liczby wartości
    else:
        median = (values[(n // 2) - 1] + values[n // 2]) / 2  # Mediana dla parzystej liczby wartości
    return median


def solution(expenses):
    result = 0
    keyslist = list(expenses.keys())  # tworzę listę roku i miesiąca
    keyslist1 = []
    for i in range(0, len(keyslist)):
        keyslist1 += list(expenses[keyslist[i]].keys())  # tablica dla dni miesiąca pobierana z kluczy słownika

    prices = []

    for j in range(0, len(keyslist)):
        sunday = first_sunday(keyslist[j][:4], keyslist[j][-2:])
        for i in range(0, len(keyslist1)):
            if create_date(keyslist[j], keyslist1[i]) <= sunday:
                try:
                    prices += list(expenses[keyslist[j]][keyslist1[i]]["food"])
                    try:
                        prices += list(expenses[keyslist[j]][keyslist1[i]]["fuel"])
                    except KeyError:
                        prices = prices
                except KeyError:
                    prices = prices
        prices = sorted(prices)
    result = calculate_median(prices)

    return result

print(solution(expenses))
