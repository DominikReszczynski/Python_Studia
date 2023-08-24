"""Oblicz sumę sześcianów liczb naturalnych od 0 do 100. Rozwiń swój program, który policzy ile
liczb naturalnych (od 0) trzeba zsumować, by uzyskać liczbę większą niż 10^6"""
summ=0
limes=pow(10,6)
check=0
for i in range(2,101):
    print(i)
    i=pow(i,3)
    print("-",i)
    summ+=i
print("suma sześcianów liczb naturalnych od 0 do 100 to:",summ,"\n")
print("--------------tu się zaczyna 2 częśc zadania-------------------------- \n")
#-----------------------------------------------------------------------------------------------------------------------
summ=0

for i in range(int(limes/2)):
    if summ<limes:
        summ+=i
        print("summ teraz to:", summ)
        check+=1
        print("check teraz to:", check,"\n")
print("musim dodać do siebie:", check,"liczb by przekroczyć liczbę 10^6 i pierwszą liczbą która przekracza jest:", summ)