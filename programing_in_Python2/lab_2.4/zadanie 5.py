"""5.Zdefiniować klasę Hotel. Każdy hotel ma określoną liczbę numerowanych pokoi
rozmieszczonych na poszczególnych piętrach. Liczba pięter i liczba pokoi na każdym
piętrze jest ustawiana w momencie tworzenia obiektu. Pokój jest identyfikowany przez
obiekt klasy NumerPokoju (o polach: pietro i pokoj). Określony pokój jest wyjęty jeśli
jest z nim powiązany obiekt klasy Osoba(zaproponować definicję stosownej klasy).
Jedna osoba może wynajmować wiele pokoi.Należy z definiować metody:
czy jest jakiś wolny pokój,
ile jest wolnych pokoi,
wynajmij dowolny z wolnych pokoi podanej (jako parametr) osobie (obiekt typu Osoba)-
wynikiem powinien być numer przydzielonego pokoju,
czy można wynająć 2-3 sąsiednie pokoje(wynikiem powinien być numer pierwszego pokoju
lub null jeśli to niemożliwe), czy osoba o podanym nazwisku wynajmuje jakiś pokój, z
wolnij pokój bądź wszystkie pokoje wynajmowane przez osobę o podanym nazwisku."""
class RoomNumber:
    def __init__(self, floor, room):
        self.floor = floor
        self.room = room
        self.person = None

    def __str__(self):
        return f"Piętro: {self.floor}, Pokój: {self.room}"


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Hotel:
    def __init__(self, num_floors, num_rooms_per_floor):
        self.num_floors = num_floors
        self.num_rooms_per_floor = num_rooms_per_floor
        self.rooms = self.createRooms()

    def createRooms(self):
        rooms = []
        for floor in range(1, self.num_floors + 1):
            for room in range(1, self.num_rooms_per_floor + 1):
                rooms.append(RoomNumber(floor, room))
        return rooms

    def isAnyRoomAvailable(self):
        return len(self.rooms) > 0

    def getNumAvailableRooms(self):
        return len(self.rooms)

    def rentAnyAvailableRoom(self, person):
        if self.isAnyRoomAvailable():
            room = self.rooms.pop(0)
            room.person = person
            return room
        else:
            return None

    def canRentAdjacentRooms(self):
        if len(self.rooms) >= 2:
            room1 = self.rooms[0]
            room2 = self.rooms[1]
            return room1, room2
        else:
            return None

    def isPersonRentingRoom(self, last_name):
        for room in self.rooms:
            if room.person and room.person.last_name == last_name:
                return True
        return False

    def getAvailableRooms(self):
        available = []
        for room in self.rooms:
            if not room.person:
                available.append(room)
        return available

    def getRoomsRentedByPerson(self, last_name):
        rooms = []
        for room in self.rooms:
            if room.person and room.person.last_name == last_name:
                rooms.append(room)
        return rooms


hotel = Hotel(5, 10)

print(hotel.isAnyRoomAvailable())  # True
print(hotel.getNumAvailableRooms())  # 50

person1 = Person("Jacek", "Sasin")
room = hotel.rentAnyAvailableRoom(person1)
print(room)  # Piętro: 1, Pokój: 1

print(hotel.canRentAdjacentRooms())  # (Piętro: 1, Pokój: 2, Piętro: 1, Pokój: 3)

print(hotel.isPersonRentingRoom("Sasin"))  # True

available_rooms = hotel.getAvailableRooms()
for available_room in available_rooms:
    print(available_room)

