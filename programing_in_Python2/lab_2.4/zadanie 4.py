'''4.Napisz program reprezentujący obiektowo talię kart(52). Zdefiniuj metody
porównujące karty, sortujące, wyświetlające, dodawanie, usuwanie i przenoszenie ich.
Rozszerzając zadanie zaproponuj implementację wybranej gry karcianej '''
import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}, {self.suit}"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return self.rank < other.rank


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        ranks = ["AS", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jopek", "Królowa", "Król"]
        suits = ["Serce", "Diament", "Żołądź", "Wino"]

        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)

    def move_card(self, card, other_deck):
        if card in self.cards:
            self.cards.remove(card)
            other_deck.add_card(card)

    def sort(self):
        self.cards.sort()

    def display(self):
        for card in self.cards:
            print(card)
class WarGame:
    def __init__(self):
        self.deck = Deck()
        self.player1_cards = []
        self.player2_cards = []

    def start(self):
        print("-WOJNA-")

        self.deck.shuffle()
        self.deal_cards()

        while len(self.player1_cards) > 0 and len(self.player2_cards) > 0:
            player1_card = self.player1_cards.pop(0)
            player2_card = self.player2_cards.pop(0)

            print("Gracz 1 wyciąga:", player1_card)
            print("Gracz 2 wyciąga:", player2_card)

            if player1_card == player2_card:
                print("Wojna!")
                self.war(player1_card, player2_card)
            elif player1_card > player2_card:
                print("Gracz 1 wygrywa rundę!")
                self.player1_cards.append(player1_card)
                self.player1_cards.append(player2_card)
            else:
                print("Gracz 2 wygrywa rundę!")
                self.player2_cards.append(player2_card)
                self.player2_cards.append(player1_card)

            print("Gracz 1 posiada", len(self.player1_cards), "kart")
            print("Gracz 2 posiada", len(self.player2_cards), "kart")
            print("")

        if len(self.player1_cards) == 0:
            print("Gracz 2 wygrywa grę!")
        else:
            print("Gracz 1 wygrywa grę!")

    def deal_cards(self):
        for _ in range(len(self.deck.cards) // 2):
            self.player1_cards.append(self.deck.deal())
            self.player2_cards.append(self.deck.deal())

    def war(self, card1, card2):
        war_cards = [card1, card2]

        while True:
            if len(self.player1_cards) < 3 or len(self.player2_cards) < 3:
                # Nie można przeprowadzić pełnej wojny, jeden z graczy ma za mało kart
                if len(self.player1_cards) < 3 and len(self.player2_cards) < 3:
                    # Obydwaj gracze mają za mało kart
                    print("Remis!")
                elif len(self.player1_cards) < 3:
                    print("Gracz 2 wygrywa grę!")
                else:
                    print("Gracz 1 wygrywa grę!")
                break

            print("Karty wojenne:")
            for _ in range(3):
                war_cards.append(self.player1_cards.pop(0))
                war_cards.append(self.player2_cards.pop(0))
            print(war_cards)

            player1_card = self.player1_cards.pop(0)
            player2_card = self.player2_cards.pop(0)

            print("Gracz 1 wyciąga:", player1_card)
            print("Gracz 2 wyciąga:", player2_card)

            war_cards.extend([player1_card, player2_card])

            if player1_card == player2_card:
                print("Kolejna wojna!")
            elif player1_card > player2_card:
                print("Gracz 1 wygrywa rundę wojenną!")
                self.player1_cards.extend(war_cards)
            else:
                print("Gracz 2 wygrywa rundę wojenną!")
                self.player2_cards.extend(war_cards)

            print("Gracz 1 posiada", len(self.player1_cards), "kart")
            print("Gracz 2 posiada", len(self.player2_cards), "kart")
            print("")
            break


deck = Deck()
# Dodawanie karty do talii
new_card = Card("AS", "Wino")
deck.add_card(new_card)
print("\nTalia po dodaniu nowej karty:")
deck.display()

# Usuwanie karty z talii
deck.remove_card(new_card)
print("\nTalia po usunięciu karty:")
deck.display()

# Tworzenie drugiej talii i przeniesienie jednej karty
deck2 = Deck()
deck.move_card(card, deck2)
print("\nTalia 1 po przeniesieniu karty:")
deck.display()
print("\nTalia 2 po przeniesieniu karty:")
deck2.display()

# Sortowanie talii
deck2.sort()
print("\nPosortowana talia 2:")
deck2.display()

#Gra w wojnę
game = WarGame()
game.start()