import math
def sum (first, second):
    sumarize=first + second
    return sumarize
def dif (first, second):
    diffrent=first - second
    return diffrent
def multi (first, second):
    multiply=first * second
    return multiply
def div (first, second):
    try:
        division1=first / second
        return division1
    except ZeroDivisionError:
        return "niedzielimy przez zero"
def root (first, second):
    rootExtraction1 = 0
    rootExtraction2 = 0
    if first>0:
        rootExtraction1= first**(1/2)
    if first<0:
        rootExtraction1="liczba ujemna"
    if second>0:
        rootExtraction2= second**(1/2)
    elif second<0:
        rootExtraction2= "liczba ujemna"
    return rootExtraction1,rootExtraction2
numberOne=int(input("podaj pierwszą liczbę: "))
numberTwo=int(input("podaj drugą liczbę: "))
rootRes1,rootRes2= root(numberOne,numberTwo)

print("wynik dodawania to: ", sum(numberOne,numberTwo))
print("wynik odejmowania to: ", dif(numberOne,numberTwo))
print("wynik mnożenia to: ", multi(numberOne,numberTwo))
print("wynik dzielenia to: ", div(numberOne,numberTwo))
print("wynik pierwistkowanie 1 to: ", rootRes1, "wynik drugiego to: ", rootRes2)
