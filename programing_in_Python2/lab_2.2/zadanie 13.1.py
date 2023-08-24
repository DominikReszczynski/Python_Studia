"""1.
Napisz klasę samochód w której zdefiniujesz 5 obiektów dotyczących
samochodów np. marka,
model, przebieg. Dodaj 5 metod, które będą wywoływane na obiektach z przekazywanymi
parametrami np. jedzprosto();Jeden samochód powinien mieć kolor "czerwony", rodzaj
"kabriolet", wartość 60000 i nazwę "Ferrari".Zaproponuj pozostałe samochody."""
class car:
    species="samochód"
    def __init__(self,brand,model,mileage,color,wheels):
        self.brand=brand
        self.model=model
        self.mileage=mileage
        self.color=color
        self.wheels=wheels
    def radio(self,song):
        return"W {} leci {}".format(self.brand,song)
    def comfort(self,comforted):
        return"Czy w {} jest wygodnie?".format(self.brand,comforted)
    def frog(self,frogii):
        return"czy {} prowadzi żaba? {}".format(self.model,frogii)
    def drive (self):
        return"{} {} jeździ prosto".format(self.brand,self.model)
toyota=car("toyota","yaris",100000,"red",17)
mustang=car('mustang','nieznam',5000,'czerwono-czrny',17)
print(toyota.wheels)
print(toyota.radio("man who sold the world"))
print(toyota.frog("tak"))
print(toyota.drive())
