#Napisz program, który wyświetli n kolejnych potęg naturalnych liczby 2.
taptap=int(input("do której potęgi? "))
number=0
for i in range(taptap):
    number=2**i
    print("dla",i,"to",number)