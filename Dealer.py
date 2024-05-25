from Player import Player

class Dealer(Player):

    def __init__(self,login,senha):
        self.banco=0
        self.login=login
        self.senha=senha
        self.ganhos=0
        self.perdas=0

    def ad_score(self,i):
        self.banco=i
        self.ganhos=i

    def bet(self,i):
        self.banco-=i
        self.perdas=i
        return(i)

    def remove_score(self,i):
        self.banco-=i
        self.perdas=i
        return(i)
    
    def profit(self):
        aux=0
        aux=(self.ganhos-self.perdas)
        return(aux)