"""Zadanie7.Napisz program potrafiący rozwiązywać równanie kwadratowe:
y = ax2 + bx + c """
import math
print("Witaj w programie do rozwiązywania równania kwadratowego :)")

a=float(input("podaj a: "))
b=float(input("podaj b: "))
c=float(input("podaj c: "))
delta=pow(b,2)-4*a*c

print(delta)
if delta>0:
    x1=((-1)*math.sqrt(delta)-b)/2*a
    x2=(math.sqrt(delta)-b)/2*a
    print("miejsca zerowe x1:",round(x1,1),"natomist x2:",round(x2,1))
elif delta==0:
    x0=(-1)*b/2*a
    print("miejsce zerowe to:",x0)
else:
    print("brak miejsc zerowych!")
