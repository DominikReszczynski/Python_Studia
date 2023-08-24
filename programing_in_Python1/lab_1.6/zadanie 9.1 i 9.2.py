"""Utwórz 4 zestawy złożone z nazw drużyn sportowych min. 10 na każdy zestaw. Spraw
by część nazw się powtarzała np. LigaMistrzow= set(["Real Madrid", "PSG", "Bayern
Monachium”"]) Nazwy drużyn do zestawów powinny zostać wpisane losowo z puli 20
zespołów. """
#-Zadanie 1-#
import random
print("\n")
tab_of_teams=["wks",'skąd mam znać nazwy zespołów','Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop','Python', 'R', 'SQL', 'Git',"takjest",'może być',"a jak",'dokładnie','jeszcze jak','jak on żre koperek','Hihihihihi',"Iphone"]
print(len(tab_of_teams))
ligmistrzow=set()
euro= set()
pucharswiata=set()
last_grup=set()

while len(ligmistrzow)<=random.randint(10,19):
    ligmistrzow.add(tab_of_teams[random.randint(0,19)])
print("ligamistrzów:",ligmistrzow)

while len(euro)<=random.randint(10,19):
    euro.add(tab_of_teams[random.randint(0,19)])
print("euro:",euro)

while len(pucharswiata)<=random.randint(10,19):
    pucharswiata.add(tab_of_teams[random.randint(0,19)])
print("puchar świata:",pucharswiata)

while len(last_grup)<=random.randint(10,19):
    last_grup.add(tab_of_teams[random.randint(0,19)])
print("ostatnia grupa:",last_grup)

#-Zadanie 2-#
print("\n----------------------------------Zadanie 2----------------------------------------------------------------------------")
print("intersection tworzy część wspólną zbiorów:\n",ligmistrzow.intersection(euro))
print("\n diffrence zwraca różnicę pomiędzy zbiorami:\n",ligmistrzow.difference(euro))
print("\n union zwraca  zestaw będący połączeniem zbiorów A i B:\n",ligmistrzow.union(euro))
print("\n issuperset zwraca TRUE jeśli B jest podzbiorem A:\n",ligmistrzow.issuperset(euro))
print("\n issubset zwraca wartość TRUE jeśli A jest podzbiorem B:\n",ligmistrzow.issubset(euro))
