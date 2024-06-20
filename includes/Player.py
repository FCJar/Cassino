import os

current_path=os.path.dirname(__file__)
path=os.path.join(current_path,'..','assets','last_save','score.txt')

class Player:
    #builder
    def __init__(self, name, chips):
        self.__name = name
        self.__chips = chips
        self.hand = []

    #place the bet
    def bet(self, amount):
        if amount > self.chips:
            raise ValueError("Not enough chips to place the bet.")
        self.__chips -= amount
        return amount

    #won the chips
    def win(self, amount):
        self.__chips += amount

    #lose the chips
    def lose(self, amount):
        self.__chips -= amount
        if self.__chips < 0:
            self.__chips = 0

    #add a card to hand
    def add_card(self, card):
        self.hand.append(card)

    #clean the hand of cards
    def clear_hand(self):
        self.hand = []
    
    #calculate the player score
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
        
    #get chips
    def get_chips(self):
        return(self.__chips)
    
    #read the save txt
    def readData(self):
        save = open(path,'r')
        self.__chips = int(save.readline())
        self.__name = str(save.readline())

    #save the actual state
    def saveData(self):
        myarchive=str(self.__chips)+('\n')+str(self.__name)
        save = open(path,'w')
        save.write(str(myarchive))
        save.close()

    #get name
    def get_name(self):
        return(self.__name)
    
    #return the cards in player hand 
    def __str__(self):
        return f"{self.__name} has {self.__chips} chips and hand: {', '.join(str(card) for card in self.hand)}"
