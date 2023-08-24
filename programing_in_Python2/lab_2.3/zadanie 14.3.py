import math
"""Napisz program, w którym utworzysz klasę podstawową Figura
oraz klasy potomne:kwadrat, prostokąt, trójkąt, koło, romb, trapez.
Zaproponuj odpowiednie metody,pola i dziedziczenie. Program powinien
obliczać obwód i pole stworzonego obiektu na podstawie wprowadzonych
przez użytkownika danych."""
sideA=0
sideB=0
sideC=0
high=0
radius=0
while sideA<=0 and sideB<=0 and high<=0 and sideC<=0 and radius<=0:
    sideA=float(input("podaj długość boku A: "))
    sideB=float(input("podaj długość boku B: "))
    sideC = float(input("podaj długość boku C: "))
    high=float(input("podaj długość wysokości: "))
    radius=float(input("podaj długość promień:"))
    print("")
    if sideA<=0 and sideB<=0 and high<=0  and sideC<=0 and radius<=0:
        print("Nie poprawne dane!\n")
class Figure:
    def __init__(self,sideA,sideB,sideC,high, radius):
        self.sideA=sideA
        self.sideB=sideB
        self.high=high
        self.radius=radius
        self.sideC=sideC
class square(Figure):
    def __init__(self, sideA,sideB,sideC,high,radius):
        super().__init__(sideA,sideB,sideC,high,radius)

    def area(self):
        print("KWADRAT:")
        print("Pole kwadratu wynosi:", pow(self.sideA,2))
    def perimeter(self):
        print("Obwód kwadratu wynosi:", self.sideA*4)
class rectangle(Figure):
    def __init__(self, sideA,sideB,sideC,high,radius):
        super().__init__(sideA,sideB,sideC,high,radius)
    if sideA!=sideB:
        def area(self):
            print("\nPROSTOKĄT:")
            print("Pole prostokąta wynosi:", sideA*sideB)
        def perimeter(self):
            print("Obwód prostokąta wynosi:", sideA*2+sideB*2)
    else:
        print("\nPROSTOKĄT:")
        print("Podane dane tworzą kwadrat a nie prostokąt!\n")
class tringle(Figure):
    def __init__(self, sideA,sideB,sideC,high,radius):
        super().__init__(sideA,sideB,sideC,high,radius)

    def area(self):
        sides = [sideA, sideC, sideB]
        sides = sorted(sides)
        print("\nTRÓJKĄT:")
        print("Pole trójkąta wynosi:", (sides[-1]*high)/2)
    def perimeter(self):
        sides = [sideA, sideC, sideB]
        sides = sorted(sides)
        print("Obwód trójkąta wynosi:", sum(sides))
class circle(Figure):
    def __init__(self, sideA,sideB,sideC,high,radius):
        super().__init__(sideA,sideB,sideC,high,radius)

    def area(self):
        print("\nKOŁO:")
        print("Pole kola wynosi:", round(math.pi*pow(radius,2),2))
    def perimeter(self):
        print("Obwód kola wynosi:", round(2*math.pi*radius,2))
squares=square(sideA,0,0,0,0)
squares.area()
squares.perimeter()
rectangles=rectangle(sideA,sideB,0,0,0)
if sideA!=sideB:
    rectangles.area()
    rectangles.perimeter()
tringles=tringle(sideA,sideB,sideC,high,0)
tringles.area()
tringles.perimeter()
circles=circle(0,0,0,0,radius)
circles.area()
circles.perimeter()