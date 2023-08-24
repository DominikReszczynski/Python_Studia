'''Korzystając ze słowników stwórz menu restauracji. Dodaj do niej 10 pozycji razem z cenami.
Za pomocą pętli for wypisz: wartości, klucze, klucze i wartości. W menu restauracji usuń
element o najniższej cenie oraz o największej. Dodaj możliwość dodania nowej pozycji do
słownika np. pizza hawajska z ceną 19.99 zł.'''
menu={'kotlet':(19.99),"zupa":(8.99),"warzywa na prze":(14.99),"koktail":(6.88)}
print(menu)
mini=0
maxi=0
name_dish_mini=""
name_dish_maxi=""
for name in menu:
    print ("\nnazwa to     %s" % name,"     cena to      %s" % menu[name])
    print(name, menu[name])
    if menu[name]>=maxi:
        maxi=menu[name]
        name_dish_maxi=name
    elif menu[name]<=maxi:
        mini=menu[name]
        name_dish_mini=name
print('\nmax',maxi, name_dish_maxi)
print('mini',mini,name_dish_mini)
del menu[name_dish_mini]
print("\nusuneliśmy własnie z listy:",name_dish_mini,"(najmniejsza cena) teraz menu wygląda tak",menu)
del menu[name_dish_maxi]
print("usuneliśmy własnie z listy:",name_dish_maxi,"(najwyższa cena) teraz menu wygląda tak",menu)

test="tak"
while test=="tak":
    test=input('\nChcesz coś dodać do menu? (tak/nie): ')
    if test=="tak":
        new_meal=input("podaj nazwę posiłku: ")
        price_of_new_meal=float(input("podaj cenę nowego posiłku: "))
        menu[new_meal]=price_of_new_meal
        print("\n menu teraz tak wygląda",menu)
    elif test=="nie":
        print("szkoda może następnym razem ;)")
        test='nie'
        break
    else:
        print("nie rozumiem co mówisz!")