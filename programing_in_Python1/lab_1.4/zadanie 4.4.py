'''Napisz program przy użyciu pętli while wczytujący z klawiatury wartości, a następnie
wyświetlający średnią tych wartości, niech program kończy wprowadzanie, kiedy natrafi na
cyfrę 0. Czy możliwe by było przerwanie jeśli ktoś wpisze wybrany znak albo string o treści
NULL?'''
check=1
tab_number=[]
medicore=0


while check==1:
    check_2 = 0
    summ=0
    numberos = ""
    taptap=input("podaj liczbę a policzymy razem średnią (NULL by przerwać) \n")

    if taptap=="NULL":
        print("zakończyłeś działanie programu \n")
        print()
        check+=1
        break

    for i in taptap: #pętla odpowiada za rozdzielenie tekstu i sprawdzenie czy są to liczby dzięki systemowi ascii a
        # potem je skleja razem jeśli jest to assci check_2 odpowiada za zliczenie długości liczby by potem porównać ją z len(taptap)
        #by w środku ciągu nie znalazła się zaraz żadna litera
        if ord(i)>=48 and ord(i)<=57:
            numberos+=i
            check_2+=1
    if check_2==len(taptap):
        tab_number.append(int(numberos))
        print('nasze liczby teraz to: ',tab_number)

        medicore+=1
        summ=sum(tab_number)
        summ=summ/medicore
        print("średnia to ", summ)

