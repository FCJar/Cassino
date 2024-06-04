class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []

    def bet(self, amount):
        if amount > self.chips:
            raise ValueError("Not enough chips to place the bet.")
        self.chips -= amount
        return amount

    def win(self, amount):
        self.chips += amount

    def lose(self, amount):
        self.chips -= amount
        if self.chips < 0:
            self.chips = 0

    def add_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def __str__(self):
        return f"{self.name} has {self.chips} chips and hand: {', '.join(str(card) for card in self.hand)}"
