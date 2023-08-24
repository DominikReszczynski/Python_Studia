"""zadanie6.Napisz   program,   który   spośród   czterech   podanych
przez   użytkownika   liczb   wybierze największą z  nich  i  wypisze  ją na
ekranie.  Spróbuj  przewidzieć wszystkie  trudne  kombinacje liczb a,b,c i d.
Czy może być problem w którymś z przypadków? """
number=1
tab=[]
for i in range(4):
    a=float(input("podaj liczbę :"))
    number+=1
    tab.append(a)
print("największa liczba to ",max(tab))
