#Napisz program wypisujący nieparzyste liczby z zakresu 100 do 200, ale niepodzielne przez 2 i 3.
for i in range (100,201):
    if i%2!=0 and i%3!=0:
        print(i)