from constants import CardValue, CardSuit
import random

class Card:
    def __init__(self, card_value: CardValue, card_suit: CardSuit):
        self.card_value = card_value
        self.suit = card_suit

    def __eq__(self, other) -> bool:
        return self.card_value == other.card_value and self.suit == other.suit

    def __gt__(self, other) -> bool:
        return self.card_value.value > other.card_value.card_value

    def __repr__(self):
        return f"{self.card_value.name} of {self.suit.name}"

class Deck:
    def __init__(self):
        self.cards: list[Card] = []
        for suit in CardSuit:
            for rank in CardValue:
                self.cards.append(Card(rank, suit))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal_hand(self) -> list[Card]:
        hand = self.cards[:5]
        self.cards = self.cards[5:]
        return hand