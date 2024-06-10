from .deck import Deck

class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.hand = []

    def create_deck(self):
        self.deck.reset_deck()
        self.deck.create_deck()

    def shuffle_deck(self):
        self.deck.shuffle()

    def deal_card(self):
        return self.deck.deal_card()

    def deal_hand(self, num_cards):
        return [self.deal_card() for _ in range(num_cards)]

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def get_score(self):
        score = 0
        for card in self.hand:
            score += card.get_value()
        return score

    def __str__(self):
        return f"Dealer's hand: {', '.join(str(card) for card in self.hand)}"
