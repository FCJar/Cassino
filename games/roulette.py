import pygame
from .game import Game
import includes.colors as colors
import random
import sys
import os
from includes.Player import Player


current_path = os.path.dirname(__file__)
background_path = os.path.join(current_path, '..', 'assets', 'images', 'roulete.jpg')
background1_path = os.path.join(current_path, '..', 'assets', 'images', 'roulete1.jpg')

background=pygame.image.load(background_path)
background1=pygame.image.load(background1_path)

class Roulette(Game):
    #builder
    def __init__(self, screen, screen_width, screen_height):
        super().__init__(screen, screen_width, screen_height)
        self.bet = None
        self.my_number = None
        self.color=None
        self.roulette_numbers = list(range(37))  # 0-36
        self.start=False
        self.errorMsg=False
        self.Pl=Player('Jose',15000)
        self.Pl.readData()
    
    #processing game input events
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                elif event.key == pygame.K_TAB:
                    if self.start==True:
                        self.start=False
                        self.errorMsg=False
                    else: 
                        self.start=True
                        self.errorMsg=False

                elif event.key == pygame.K_1:
                        self.bet=5
            
                elif event.key == pygame.K_2:
                        self.bet=25
                
                elif event.key == pygame.K_3:
                        self.bet=125
                
                elif event.key == pygame.K_b:
                    self.color="Black"
                    self.my_number=None

                elif event.key == pygame.K_r:
                    self.color="Red"
                    self.my_number=None
                
                elif event.key == pygame.K_UP:
                    if(self.my_number == None):
                        self.my_number=0
                        self.color=None

                    elif(self.my_number<37 and self.start==True):
                        self.my_number+=1
                        self.color=None

                elif event.key == pygame.K_DOWN:
                    if(self.my_number == None):
                        self.my_number=0
                        self.color=None

                    elif(self.my_number>0 and self.start==True):
                        self.my_number-=1
                        self.color=None

                    else:
                        self.my_number=None

                elif event.key == pygame.K_RETURN:
                    if(self.start == True and ((self.my_number!= None) or (self.color!=None))):
                        self.spin_roulette()
                
                else:
                    print("invalid entry")

    #spin the virtual roulette wheel and generate the game result
    def spin_roulette(self):
        if((self.bet==None or self.Pl.get_chips==None)):
            print=("Error msg")
        elif(self.bet<self.Pl.get_chips()):
            result=random.choice(self.roulette_numbers)
            if(self.color=="Black"):
                if((result==2) or (result==4) or (result==6) or (result==8) or (result==10) or (result==11) or (result==13) or (result==15)):
                    self.Pl.win(self.bet*2)
                elif((result==17) or (result==20) or (result==22) or (result==24) or (result==26) or (result==28) or (result==29) or (result==33) or (result==35)):
                    self.Pl.win(self.bet*2)
                else:
                    self.Pl.lose(self.bet)

            elif(self.color=="Red"):
                if((result==1) or (result==3) or (result==5) or (result==7) or (result==9) or (result==12) or (result==14) or (result==16)):
                    self.Pl.win(self.bet*2)
                elif((result==18) or (result==19) or (result==21) or (result==23) or (result==25) or (result==27) or (result==30) or (result==32) or (result==34)):
                    self.Pl.win(self.bet*2)
                else:
                    self.Pl.lose(self.bet)

            elif((self.my_number>=0 and self.my_number<=36)):
                if(self.my_number==result):
                    self.Pl.win(self.bet*8)
                else:
                    self.Pl.lose(self.bet)
            
        else:
            self.errorMsg=True
            
    #updating game status
    def update(self):
        pass

    #draw the game interface
    def draw(self):

        self.screen.fill(colors.WHITE_COLOR)

        if(self.start==False or self.errorMsg==True):
            self.screen.blit(background,(0,0))
            font=pygame.font.Font(None, 60)
            msg1 = font.render("::Welcome to lucky roulete::",True,colors.BOARD_COLOR)
            self.screen.blit(msg1,(self.screen_width//2 - msg1.get_width()//2,self.screen_height//2 - msg1.get_height()-240))

            font=pygame.font.Font(None,40)
            msg2 = font.render("::How to play::",True,colors.BOARD_COLOR)
            self.screen.blit(msg2,(self.screen_width//2 - msg2.get_width()//2,self.screen_height//2 - msg2.get_height()+180))
            
            font=pygame.font.Font(None,24)
            msg3= font.render("Press a number betwen 1 to 3 for chose the chips   ::   For (Start/Pause) the game press tab",True,colors.BOARD_COLOR)
            self.screen.blit(msg3,(self.screen_width//2 - msg3.get_width()//2,self.screen_height//2 - msg3.get_height()+200))
            
            font=pygame.font.Font(None,24)
            msg4 = font.render("Press the (backspace) button for spin   ::   For start the game press tab",True,colors.BOARD_COLOR)
            self.screen.blit(msg4,(self.screen_width//2 - msg4.get_width()//2,self.screen_height//2 - msg4.get_height()+220))

            font=pygame.font.Font(None,24)
            msg5 = font.render("Press the up and down arrows to chose a number(36 to 1)   ::   Press B or R for bet by colors(2 to 1)",True,colors.BOARD_COLOR)
            self.screen.blit(msg5,(self.screen_width//2 - msg5.get_width()//2,self.screen_height//2 - msg5.get_height()+240))
            
            if self.errorMsg==True:
                font=pygame.font.Font(None,40)
                erro_msg=font.render("You are bankrupt! Add more cash::",True,colors.RED_COLOR)
                self.screen.blit(erro_msg,(self.screen_width//2 - erro_msg.get_width()//2,self.screen_height//2 - erro_msg.get_height()+140))
            
        elif(self.errorMsg==False and self.start==True):
            self.screen.blit(background1,(0,0))
            font=pygame.font.Font(None, 40)
            auxtext=("Name:: " + self.Pl.get_name() + "       Chips:: " + str(self.Pl.get_chips()))
            new_msg1 = font.render(auxtext,True,colors.BLACK_COLOR)
            self.screen.blit(new_msg1,(self.screen_width//2 - new_msg1.get_width()//2,self.screen_height//2 - new_msg1.get_height()-240))
            
            if(self.my_number!=None):
                font=pygame.font.Font(None,24)
                auxtext1=("Number::    "+str(self.my_number))
                new_msg1 = font.render(auxtext1,True,colors.BLACK_COLOR)
                self.screen.blit(new_msg1,(self.screen_width//2 - new_msg1.get_width()//2,self.screen_height//2 - new_msg1.get_height()-220))
            
            if(self.color!=None):
                font=pygame.font.Font(None,24)
                auxtext2=("Color::    "+(self.color))
                new_msg2 = None
                if(self.color=="Black"):
                    new_msg2 = font.render(auxtext2,True,colors.BLACK_COLOR)
                else:
                    new_msg2 = font.render(auxtext2,True,colors.RED_COLOR)
                self.screen.blit(new_msg2,(self.screen_width//2 - new_msg2.get_width()//2,self.screen_height//2 - new_msg2.get_height()-220))
            
            if(self.bet!=None):
                font=pygame.font.Font(None,24)
                auxtext3 = ("Bet::    "+str(self.bet))
                new_msg3 = font.render(auxtext3,True,colors.BLACK_COLOR)
                self.screen.blit(new_msg3,(self.screen_width//2 - new_msg3.get_width()//2,self.screen_height//2 - new_msg3.get_height()-200))
