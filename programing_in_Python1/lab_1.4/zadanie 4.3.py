"""Napisz program przy użyciu pętli while, w którym podajemy liczbę naturalną do momentu
podania liczby podzielnej przez 12. Algorytm kończy działanie napisem: „Podałeś liczbę
podzielną przez 12, wiec kończę działanie pętli". """
number=11
while number==11:
    taptap=int(input("podaj liczbę"))
    if taptap%12==0:
        print("twoja liczba jest podzielna przez 12")
        number+=1
        break