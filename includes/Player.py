from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def ad_score(self,i):
        pass

    def bet(self,i):
        pass

    def remove_score(self,i):
        pass