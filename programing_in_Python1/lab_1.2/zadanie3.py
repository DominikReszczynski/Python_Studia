"""zadanie3.Napisz program, który porówna ze sobą 3 liczby i wskaże,
która jest większa i czy liczby są identyczne. Zastanów się nad opcją
zagnieżdżania ifów."""
a=0

tab=[]
for i in range(3):
    a = int(input("Podaj liczbę: "))
    tab.append(a)
print("największa liczba to: ",max(tab))

if tab[0]==tab[2] and tab[1]==tab[2]:
    print("cyfry są takie same!!!")
