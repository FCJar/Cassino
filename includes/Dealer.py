from .deck import Deck

class Dealer:
    #builder
    def __init__(self):
        self.deck = Deck()
        self.hand = []

    #create a new deck
    def create_deck(self):
        self.deck.reset_deck()
        self.deck.create_deck()

    #shufle the atual deck
    def shuffle_deck(self):
        self.deck.shuffle()

    #take a card of the deck
    def deal_card(self):
        return self.deck.deal_card()

    #take a card from the deck
    def deal_hand(self, num_cards):
        return [self.deal_card() for _ in range(num_cards)]

    #add a card to dealer hand
    def add_card_to_hand(self, card):
        self.hand.append(card)

    #erase the entire card hand
    def clear_hand(self):
        self.hand = []

    #return the dealer point score
    def get_score(self):
        score = 0
        aces = 0
        for card in self.hand:
            if card.get_rank() == 'Ace':
                aces += 1
            score += card.get_value()
            while score > 21 and aces > 0:
                score -= 10
                aces -= 1
        return score

    #return the cards in player hand 
    def __str__(self):
        return f"Dealer's hand: {', '.join(str(card) for card in self.hand)}"
