"""Napisz program wczytujący z klawiatury n liczb całkowitych. Program ma znaleźć największą
spośród podanych liczb oraz wydrukować na ekranie informację mówiącą o tym, ile razy
największa liczba wystąpiła w podanym ciągu liczb."""
import random
print("\n-----------------------------------------------------------------------")
tab_random=[]
loop=random.randint(10,35)
print(loop,"będzie w naszej tablicy")
for i in range(loop):
    random_number=random.randint(0,100)
    tab_random.append(random_number)
print(tab_random,'\n')
max_tab_random=max(tab_random)
print('największa liczba to:',max_tab_random,'\n')
how_many=tab_random.count(max_tab_random)
print('największa liczba:',max_tab_random,'\nwystępuje dokładnie:',how_many)
print("----------------------------------------------------------------------")