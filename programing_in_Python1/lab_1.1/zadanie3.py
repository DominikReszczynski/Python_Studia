'''zadanie 3.Napisz skrypt, za pomocą zadeklarowanych zmiennych, który
# obliczy ile czasu i kilometrów ma rok świetlny.'''
light_second=300000 #300000km/s
sec=1
sec2=60
minut=60
ho=24
deys=365.25
km=(sec*sec2*minut*ho*deys)*light_second
time_l=deys*ho*minut*sec2*sec
print("ile czasu:",time_l)
print("ile kilometrów:",km)
