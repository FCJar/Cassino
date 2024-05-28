from abc import ABC,abstractmethod
class Game(ABC):
    @abstractmethod
    def show_game_score(self):
        pass
    def bet(self,i):
        pass
    def end_game(self):
        pass
    