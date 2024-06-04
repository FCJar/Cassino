import random
from .card import Card

class Deck:
    def __init__(self):
        self.cards = self.create_deck()
        self.shuffle()

    def create_deck(self):
        deck = []
        for rank in range(1, 14):  # 1-13 para Ás a Rei
            for suit in range(1, 5):  # 1-4 para os quatro naipes
                code = f"{rank:02d}{suit}"
                deck.append(Card(code))
        return deck

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if not self.cards:
            self.cards = self.create_deck()
            self.shuffle()
        return self.cards.pop()

    def __str__(self):
        return f"Deck has {len(self.cards)} cards"
