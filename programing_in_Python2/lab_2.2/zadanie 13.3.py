"""Napisz klasę smartfon w której zdefiniujesz kilka obiektów dotyczących
smartfonów i dodaj ciekawe metody. Spróbuj eksperymentować z metodami oraz"""
class smartphone:

    def __init__(self,producent, model, system):
        self.producent=producent
        self.model=model
        self.system=system

    def ring(self):
        return"dzwoni jeszcze jak"
    def crysis(self):
        return "can run crisis?"
s10=smartphone("samsung","galaxy s10","android")
Pro14Max=smartphone("Apple","14 pro max","ios")
print(Pro14Max.producent)
