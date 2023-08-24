"""3.Napisz program, który tworzy klasę Obywatel o polach: imię,
nazwisko, ulica,nr_domu, kod_pocztowy, miejscowość. Napisz konstruktor oraz
metodę, która wczytuje dane, oraz funkcję wyświetlającą w postaci wizytowki
i drukującą ją do plik"""
import os
class citizen:
    def __init__(self, firstName, secondName, street, streetNumber, city, cityCode):
        self.firstName=firstName
        self.secondName=secondName
        self.street=street
        self.streetNumber=streetNumber
        self.city=city
        self.cityCode=cityCode
    def profileCard(self):
        print("---- Wizytówka ----")
        print(f"{self.firstName}", f"{self.secondName}")
        print(f"ul.{self.street}", f"{self.streetNumber}")
        print(f"{self.cityCode}", f"{self.city}")
        print("-------------------")
    def info(self):
        print(f"\nImię: {self.firstName}")
        print(f"Nazwisko: {self.secondName}")
        print(f"Ulica: {self.street}")
        print(f"Nr domu: {self.streetNumber}")
        print(f"Kod pocztowy: {self.cityCode}")
        print(f"Miejscowość: {self.city}")
    def user(self):
        self.firstName = input("Podaj imię: ")
        self.secondName = input("Podaj nazwisko: ")
        self.street = input("Podaj ulicę: ")
        self.streetNumber = input("Podaj numer domu: ")
        self.cityCode = input("Podaj kod pocztowy: ")
        self.city = input("Podaj miejscowość: ")
    def printToFile(self,fileName):
        #tworzenie pliku z danymi; niestety po prubie wywołania metody wizytowka do pliku przekazywana wartość była none dla tego zastosowałem przeniesienie jej kodu do tej funkcji i przypisaniu do zmiennej
        profilCard = "---- Wizytówka ----\n"
        profilCard += f"{self.firstName} {self.secondName}\n"
        profilCard += f"ul.{self.street} {self.streetNumber}\n"
        profilCard += f"{self.cityCode} {self.city}\n"
        profilCard += "-------------------\n"
        #fileName="Dominik"#self.firstName+self.secondName
        with open(fileName,"w") as file:
            file.write(profilCard)
workFolder=os.getcwd()
print(workFolder)
obywatel1 = citizen("Jan", "Kowalski", "Wiejska", "10", "Warszawa", "00-123")
obywatel2=citizen("","","","","","")
obywatel2.user()
obywatel2.profileCard()
obywatel2.printToFile("wizytówka.txt")
#obywatel1.info()