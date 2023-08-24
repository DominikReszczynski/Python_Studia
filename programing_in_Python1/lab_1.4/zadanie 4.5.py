#Napisz program przy użyciu pętli while , który skończy wczytywania liczb podawanych przez
# użytkownika, gdy ich suma przekroczy 100 albo średnia wyniesie 66.
srednia=0
medicore=0
sum_numbers=0

while sum_numbers<=100 and srednia<=66:
    liczba=int(input("podaj liczbę: "))
    sum_numbers+=liczba
    medicore+=1
    srednia=sum_numbers/medicore
    print('aktualna suma to:',sum_numbers,"aktualna średnia to:", srednia)
    if sum_numbers>100:
        print("suma przekroczyła 100 i wynosi,",sum_numbers)
    elif srednia>66:
        print("średnia przekroczyła 66 i wynosi,", srednia)