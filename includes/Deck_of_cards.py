import random
class Deck:
    def __init__(self):
        self.Cards=[]
        for x in range(51):
            self.Cards[x]=x

    def get_shuffle_cards(self):
        random.shuffle(self.Cards)
        return(self.Cards)
    