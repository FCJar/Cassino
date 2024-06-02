from Game import Game
class Jackpot(Game):
    def __init__(self):
        self.total_score=0
        self.current_bet=0

    def show_game_score(self):
        return (self.total_score)
    
    def bet(self,i):
        pass

    def end_game(self):
        pass
    
    def play(self):
        pass