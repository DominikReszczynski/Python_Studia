#zadanie 4.Napisz skrypt, za pomocą zadeklarowanych zmiennych, który
# obliczy ile sekund ma godzina, ile sekund ma doba, ile sekund ma rok,
# ile sekund ma twoje życie.
#dla 10.12.2022
import time
import datetime
sec = 60
minute = 60
hour = 24
rok = 365.25
time_date = time.localtime()


a=datetime.date(2001,9,20) #20 września 2001
b=datetime.date(time_date[0],time_date[1],time_date[2]) #data teraz
print("ile sekund trwa moje życie:",(b-a).days*hour*minute*sec)
print("ile sekund ma godzina :",minute*sec)
print("ile sekund ma doba :",hour*minute*sec)
print("ile sekund ma rok ",rok*hour*minute*sec)

