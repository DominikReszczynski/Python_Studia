"""Zadanie4. Napisz  program,  który  wypisze  czy  podana  liczba  jest
 ujemna  czy  dodatnia  oraz  czy  jest podzielna przez 2 z resztą.
 Zaproponuj odpowiednie warunki."""
a=int(input("podaj liczbę: "))
if a<0:
    print("liczba ujemna")
elif a>0:
    print("liczba dodatnia")
else:
    print("liczba jest równa zero")

if a%2==0:
    print("liczba jest podzielna przez 2")
else:
    print("liczba jest podzielna przez 2 ale z resztą")
