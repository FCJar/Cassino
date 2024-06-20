import pygame
from .game import Game
import includes.colors as colors
import random
import sys
import os
from includes.Player import Player
from assets.text_helpers import draw_text_with_background, draw_text_with_shadow


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
        self.color = None
        self.roulette_numbers = list(range(36))  # 0-34
        self.start = False
        self.errorMsg = False
        self.Pl = Player('Jose',15000)
        self.Pl.readData()
        self.last_digit = None
        self.last_match = None
    
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
                    self.bet=100
            
                elif event.key == pygame.K_2:
                    self.bet=200
                
                elif event.key == pygame.K_3:
                    self.bet=400
                
                elif event.key == pygame.K_4:
                    self.bet=800
                
                elif event.key == pygame.K_b:
                    self.color="Black"
                    self.my_number=None

                elif event.key == pygame.K_r:
                    self.color="Red"
                    self.my_number=None
                
                elif event.key == pygame.K_UP:
                    if(self.my_number == None):
                        self.my_number=1
                        self.color=None

                    elif(self.my_number<36 and self.start==True):
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
            self.last_digit=result

            if(self.color=="Black"):
                if((result==2) or (result==4) or (result==6) or (result==8) or (result==10) or (result==11) or (result==13) or (result==15)):
                    self.Pl.win(self.bet*2)
                    self.last_match=True

                elif((result==17) or (result==20) or (result==22) or (result==24) or (result==26) or (result==28) or (result==29) or (result==33) or (result==35)):
                    self.Pl.win(self.bet*2)
                    self.last_match=True

                else:
                    self.Pl.lose(self.bet)
                    self.last_match=False

            elif(self.color=="Red"):
                if((result==1) or (result==3) or (result==5) or (result==7) or (result==9) or (result==12) or (result==14) or (result==16)):
                    self.Pl.win(self.bet*2)
                    self.last_match=True

                elif((result==18) or (result==19) or (result==21) or (result==23) or (result==25) or (result==27) or (result==30) or (result==32) or (result==34)):
                    self.Pl.win(self.bet*2)
                    self.last_match=True

                else:
                    self.Pl.lose(self.bet)
                    self.last_match=False

            elif((self.my_number>=0 and self.my_number<=34)):
                if(self.my_number==result):
                    self.Pl.win(self.bet*8)
                    self.last_match=True

                else:
                    self.Pl.lose(self.bet)
                    self.last_match=False

            self.Pl.saveData()
            self.Pl.readData()
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

            fonte_player = pygame.font.Font(None, 36)
            player_info_position = (self.screen_width - 10, 10)
            draw_text_with_background(self.screen,("Player name: " + self.Pl.get_name() + "    Chips: " + str(self.Pl.get_chips())), player_info_position, fonte_player, colors.BOARD_COLOR, colors.WHITE_COLOR, alignment='right')
            

            font=pygame.font.Font(None, 60)
            draw_text_with_background(self.screen,"::Welcome to lucky roulete::", (self.screen_width // 2, self.screen_height // 2 - 150), font, colors.BLUE_COLOR, colors.GRAY_COLOR)

            font=pygame.font.Font(None,40)
            draw_text_with_background(self.screen,"::How to play::", (self.screen_width // 2, self.screen_height // 2 + 50), font, colors.DARK_RED_COLOR, colors.GRAY_COLOR)

            font=pygame.font.Font(None,24)
            draw_text_with_background(self.screen,"Press a number betwen 1 to 3 to choose chip amount   ::   To (Start/Pause) the game press tab", (self.screen_width // 2, self.screen_height // 2 + 100), font, colors.DARK_RED_COLOR, colors.GRAY_COLOR)
            draw_text_with_background(self.screen,"Press (backspace) to spin   ::   To start the game press tab", (self.screen_width // 2, self.screen_height // 2 + 150), font, colors.DARK_RED_COLOR, colors.GRAY_COLOR)
            draw_text_with_background(self.screen,"Press the up and down arrows to choose a number(36 to 1)   ::   Press B or R to bet by colors(2 to 1)", (self.screen_width // 2, self.screen_height // 2 + 200), font, colors.DARK_RED_COLOR, colors.GRAY_COLOR)

            if self.errorMsg==True:
                font=pygame.font.Font(None,40)
                erro_msg=font.render("You are bankrupt! Add more cash::",True,colors.RED_COLOR)
                self.screen.blit(erro_msg,(self.screen_width//2 - erro_msg.get_width()//2,self.screen_height//2 - erro_msg.get_height()+140))
            
        elif(self.errorMsg==False and self.start==True):

            self.screen.fill(colors.BOARD_COLOR)
            fonte_player = pygame.font.Font(None, 36)
            player_info_position = (self.screen_width - 10, 10)
            draw_text_with_background(self.screen,("Player name: " + self.Pl.get_name() + "    Chips: " + str(self.Pl.get_chips())), player_info_position, fonte_player, colors.BOARD_COLOR, colors.WHITE_COLOR, alignment='right')
            
            roulette_image_path = os.path.join(current_path, '..', 'assets','roulette','roulette.png')
            roulette_image = pygame.image.load(roulette_image_path)
            roulette_image1 = pygame.transform.scale(roulette_image,(1020,480))
            self.screen.blit(roulette_image1,(0,0) )
        
            if(self.last_digit!=None):
                numeric_image_path = os.path.join(current_path,'..', 'assets','roulette',f'{self.last_digit}.jpeg')
                numeric_image = pygame.image.load(numeric_image_path)
                numeric_image_scale =  pygame.transform.scale(numeric_image,(100,100))
                self.screen.blit(numeric_image_scale,(750,500))

                
            if(self.last_match!=None):
                if(self.last_match):
                    win_image_path = os.path.join(current_path,'..', 'assets','roulette','win.png')
                    win_image = pygame.image.load(win_image_path)
                    win_image_scale =  pygame.transform.scale(win_image,(200,99.5))
                    self.screen.blit(win_image_scale,(500,500))

                elif(self.last_match == False):
                    win_image_path = os.path.join(current_path,'..', 'assets','roulette','fail.png')
                    win_image = pygame.image.load(win_image_path)
                    win_image_scale =  pygame.transform.scale(win_image,(200,99.5))
                    self.screen.blit(win_image_scale,(500,500))

            if(self.bet!=None):
                if(self.bet==100):
                    coin_image_path = os.path.join(current_path,'..', 'assets','roulette','coin.png')
                    coin_image = pygame.image.load(coin_image_path)
                    coin_image_scale = pygame.transform.scale(coin_image,(200,200))
                    self.screen.blit(coin_image_scale,(50,500))

                elif(self.bet==200):
                    coin_image_path = os.path.join(current_path,'..', 'assets','roulette','coin.png')
                    coin_image = pygame.image.load(coin_image_path)
                    coin_image_scale = pygame.transform.scale(coin_image,(200,200))
                    self.screen.blit(coin_image_scale,(50,500))
                    self.screen.blit(coin_image_scale, (75,500))

                elif(self.bet==400):
                    coin_image_path = os.path.join(current_path,'..', 'assets','roulette','coin.png')
                    coin_image = pygame.image.load(coin_image_path)
                    coin_image_scale = pygame.transform.scale(coin_image,(200,200))
                    self.screen.blit(coin_image_scale,(50,500))
                    self.screen.blit(coin_image_scale, (75,500))
                    self.screen.blit(coin_image_scale, (100,500))
                    self.screen.blit(coin_image_scale,(125,500))

                elif(self.bet==800):
                    coin_image_path = os.path.join(current_path,'..', 'assets','roulette','coin.png')
                    coin_image = pygame.image.load(coin_image_path)
                    coin_image_scale = pygame.transform.scale(coin_image,(200,200))
                    self.screen.blit(coin_image_scale,(50,500))
                    self.screen.blit(coin_image_scale, (75,500))
                    self.screen.blit(coin_image_scale, (100,500))
                    self.screen.blit(coin_image_scale,(125,500))
                    self.screen.blit(coin_image_scale,(150,500))
                    self.screen.blit(coin_image_scale, (175,500))
                    self.screen.blit(coin_image_scale, (200,500))
                    self.screen.blit(coin_image_scale,(225,500))


                     