from includes.Player import Player

class User(Player):
    def __init__(self,name,login,password):
        self.name=name
        self.login=login
        self.password=password
        self.score=0
        #super().__init__()

    def ad_score(self, i):
        self.score=(i*0.90)
        return(i*0.10)
    
    def bet(self, i):
        aux=0
        if(self.score>=i):
            aux=i
            self.score-=i
        else:
            aux=-1
        return aux

    def remove_score(self, i):
        self.score-=i
        return self.score
    