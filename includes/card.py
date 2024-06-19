class Card:
    #builder
    def __init__(self, code):
        self.code = code
        self.rank = self.get_rank()
        self.suit = self.get_suit()

    #get the card rank
    def get_rank(self):
        rank_code = int(self.code[:2])
        if rank_code == 1:
            return 'Ace'
        elif 2 <= rank_code <= 10:
            return str(rank_code)
        elif rank_code == 11:
            return 'Jack'
        elif rank_code == 12:
            return 'Queen'
        elif rank_code == 13:
            return 'King'
        else:
            raise ValueError("Invalid rank code")

    #get the card suit
    def get_suit(self):
        suit_code = int(self.code[2])
        if suit_code == 1:
            return 'Hearts'
        elif suit_code == 2:
            return 'Diamonds'
        elif suit_code == 3:
            return 'Clubs'
        elif suit_code == 4:
            return 'Spades'
        else:
            raise ValueError("Invalid suit code")

    #get the card value
    def get_value(self):
        if self.rank in ['Jack', 'Queen', 'King']:
            return 10
        elif self.rank == 'Ace':
            return 11  # Valor do Ás pode variar, ajuste conforme necessário
        else:
            return int(self.rank)

    #return the cards value
    def __str__(self):
        return f"{self.rank} of {self.suit} ({self.code})"
