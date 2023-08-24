#Napisz program, który symuluje działanie „LOTTO”
import random
number=0
number_tab=[]
for i in range(1,7):
    number=random.randint(1,49)
    number_tab.append(number)
print(number_tab)