#Napisz program, który wyznaczy silnię.
taptap=int(input("podaj liczbę by wyliczyć bardzo silną liczbę: "))
number=1
for i in range(2,taptap+1):

    number=number*i
print("silnia z",taptap,"to",number)