import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q",
                  "K")
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        self.cards = [Card(suit, val) for suit in suits for val in values]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def _deal(self, num):
        try:
            dealt = self.cards[:num]
            self.cards = self.cards[num:]
            return dealt
        except ValueError:
            return "All Cards have been dealt"

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError('Only full decks can be shuffled')
        else:
            random.shuffle(self.cards)
            return self

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)
