"""Napisz program, który podaje 50 razy wynik rzutu monetą - losowo 0 lub 1. Zapamiętuj liczbę
wylosowanych zer i jedynek i na koniec wyświetl podsumowanie. Zmodyfikuj program żeby
zamiast 0 lub 1 po wylosowaniu wyświetlało się "orzeł" lub "reszka"""
import random
tab_0=[]
tab_1=[]
for i in range(50):
    number=random.randint(0,1)
    if number==0:
        eagle="orzeł"
        tab_0.append(eagle)
    else:
        tails="reszka"
        tab_1.append(tails)
print(tab_0)
print(tab_1)
print("wylosowało się", len(tab_0),"orłów oreaz", len(tab_1),"reszek :)")