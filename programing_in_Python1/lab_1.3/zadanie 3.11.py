#Napisz program, który symuluje działanie „Mini LOTTO”.
import random
how_many=int(input("ile chcesz wytypować liczb (3-5)? "))
if how_many<3 or how_many>5:
    print("nie takie było polecenie, sprubuj jeszcze raz!")
else:
    tab_user_number=[]
    tab_random_number=[]
    for i in range(how_many):
        taptap_number=int(input("podaj liczbę od 1 do 42: "))
        if taptap_number<1 or taptap_number>42:
            print("nie poprawna cyfra :( sprubuj jeszcze raz od nowa")
            break
        else:
            tab_user_number.append(taptap_number)
            if len(tab_user_number)==how_many:
                print(tab_user_number)
            for i in range(5):
                random_number=random.randint(1,42)
                tab_random_number.append(random_number)
            print(tab_random_number)
            how_many_hits=0
            for i in tab_user_number:
                if i in tab_random_number:
                    print("udało ci się trafić!")
                    how_many_hits+=1
                else:
                    print("nie udało ci się trafić :(")
            print("udało ci się trafić", how_many_hits)
