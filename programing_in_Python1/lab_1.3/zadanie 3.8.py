#Napisz program, który wypisze największą liczbę niepodzielną przez 2,3,5,7 ale mniejszą od 1000.
number=0
for i in range(11,1000):
    if i%2!=0 and  i%3!=0 and i%5!=0 and i%2!=7:
        number=i
print(number)
