#zadanie 1. Napisz program, który pobierze od użytkownika dwie liczby
#i zwróci ich sumę, różnicę, iloczyn oraz iloraz (jeżeli można policzyć).

#można użyć eval("1+1")
first=int(input("podaj pierwszą liczbę: "))
second=int(input("podaj drugą liczbę: "))
sum=first+second
min=first-second
multi=first*second
div=first/second
if second==0:
    print("dzielenie przez zero")
else:
    div=first/second
    print("dzielenie to",div)
print("suma to",sum)
print("suma to",min)
print("suma to",multi)
