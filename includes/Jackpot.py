from games.game import Game
class Jackpot(Game):
    #builder
    def __init__(self):
        self.total_score=0
        self.current_bet=0
    
    #show the game 
    def show_game_score(self):
        return (self.total_score)
    
    #make a bet
    def bet(self,i):
        pass
    
    #end the actual game
    def end_game(self):
        pass
    
    #start the game
    def play(self):
        pass