#Napisz program, który wypisze na ekran liczby od zadanej wartości do zera i podzielne przez 6 oraz 9.
taptap=int(input("podaj liczbę: "))
for i in range (0,taptap+1):
    taptap=taptap-1
    if taptap%9==0 and taptap%6==0:
        print(taptap)