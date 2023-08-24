"""Zadanie8.Napisz program, który poprosi o podanie trzech długości
boków trójkąta i sprawdzi czy jest on prostokątny."""
tab=[]
tringle=0
for i in range(3):
    a=float(input("podaj bok trójkąta: "))
    tab.append(a)
tab.sort()
print(tab)
tringle=pow(tab[0],2)+pow(tab[1],2)
if tringle==pow(tab[2],2):
    print("trójkąt jest prostokątny")
else:
    print("trójkąt nie jest prostokątny")
