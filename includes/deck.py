import random
from .card import Card

class Deck:
    #builder
    def __init__(self):
        self.cards = self.create_deck()
        self.shuffle()

    #clean the deck
    def reset_deck(self):
        self.cards = []
    
    #create a new deck
    def create_deck(self):
        deck = []
        for rank in range(1, 14):  # 1-13 para Ás a Rei
            for suit in range(1, 5):  # 1-4 para os quatro naipes
                code = f"{rank:02d}{suit}"
                deck.append(Card(code))
        return deck
    
    #shuffle the card in the deck
    def shuffle(self):
        random.shuffle(self.cards)

    #take a card of the deck
    def deal_card(self):
        if not self.cards:
            self.cards = self.create_deck()
            self.shuffle()
        return self.cards.pop()

    #return the cards in the deck
    def __str__(self):
        return f"Deck has {len(self.cards)} cards"
