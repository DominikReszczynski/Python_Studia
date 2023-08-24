"""Zadanie1. Napisz program Czy liczba a jest podzielna przez b?
Program ma pobrać od użytkownika dwie liczby całkowite a, b.
Jako wynik pracy program ma wydrukować informację mówiącą o tym,
czy liczba a jest podzielna przez liczbę b
(jeden z tekstów A JEST PODZIELNE PRZEZ B lub A NIE JEST PODZIELNE PRZEZ B)."""

a = int(input("podaj pierwszą liczbę: "))#wczytuje 2 cyfry z łapki
b = int(input("podaj drugą liczbę: "))
if b==0:
    print("nie dzielimy przez zero")

elif a%b==0 and b!=0:
    print("A JEST PODZIELNE PRZEZ B") #jeżeli dzielenie nie ma reszty da się podzielić
else:
    print("A NIE JEST PODZIELNE PRZEZ B")
