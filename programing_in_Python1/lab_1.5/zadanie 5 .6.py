"""Napisz program, który będzie interpretacją gry w ”Za dużo, za mało”. Program losuje liczbę z
zakresu 1...100, a gracz (użytkownik) ma za zadanie odgadnąć, co to za liczba poprzez
podawanie kolejnych wartości. Użytkownik ma 3 szanse. Jeżeli podana wartość jest:
• większa – wyświetlany jest komunikat „Podałeś za dużą wartość”,
• mniejsza – wyświetlany jest komunikat „Podałeś za małą wartość”,
• identyczna z wylosowaną – wyświetlany jest komunikat „Gratulacje” i gra się
kończy.
• Jeśli po 3 próbach użytkownik nie podał poprawnej wartości program ma
przerwać działanie i wyświetlić komunikat – „Haha przegrałeś!” """
import random
check=0
random_number=random.randint(1,100)
while check<=2:
    print("wylosowana liczba to:",random_number)
    taptap=int(input("podaj liczbę"))
    if taptap==random_number:
        print("Gratulacje zgadłeś!!!")
        check=4
        break
    elif taptap<random_number:
        print("Podałeś za małą wartość")
        check+=1
    else:
        print("„Podałeś za dużą wartość")
        check+=1
if check==3:
    print("Przegrałeś")