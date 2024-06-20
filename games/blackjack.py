import pygame
import sys
import os
from .game import Game
import includes.colors as colors
from includes.Player import Player
from includes.Dealer import Dealer

current_path = os.path.dirname(__file__)
background_path = os.path.join(current_path, '..', 'assets', 'images', 'blackjack.jpg')
background=pygame.image.load(background_path)

class Blackjack(Game):
    #builder
    def __init__(self, screen, screen_width, screen_height):
        super().__init__(screen, screen_width, screen_height)
        self.player = Player("Player", 1000)
        self.player.readData()  
        self.dealer = Dealer()
        self.game_running = False
        self.game_bust = False
        self.betting = False
        self.aposta = 0

    # distribute the initial cards
    def deal_initial_cards(self):
        self.dealer.create_deck()
        self.player.add_card(self.dealer.deal_card())
        self.player.add_card(self.dealer.deal_card())
        self.dealer.add_card_to_hand(self.dealer.deal_card())
        self.dealer.add_card_to_hand(self.dealer.deal_card())

    #  calculate the game result
    def calculate_result(self):
        while self.dealer.get_score() < 17:
            self.dealer.add_card_to_hand(self.dealer.deal_card())
        if self.dealer.get_score() > 21:
            self.player.win(self.aposta)    
        elif self.player.get_score() > self.dealer.get_score():
            self.player.win(self.aposta)
        elif self.player.get_score() < self.dealer.get_score():
            self.player.lose(self.aposta)
        self.make_bet()

    # bet a value in the game 
    def make_bet(self):
        self.betting = True
        self.aposta = 0
        self.player.clear_hand()
        self.dealer.clear_hand()

    #processing game input events
    def handle_events(self):
        for event in pygame.event.get():
            self.player.saveData()
            self.player.readData()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # Return to main menu
                    self.running = False
                elif self.betting: 
                    if event.key == pygame.K_1: # Bet 10 chips
                        self.aposta += 10
                    if event.key == pygame.K_2: # Bet 50 chips
                        self.aposta += 50
                    if event.key == pygame.K_3: # Bet 100 chips
                        self.aposta += 100
                    if event.key == pygame.K_4: # Bet 500 chips
                        self.aposta += 500
                    if event.key == pygame.K_RETURN: # Confirm Bet
                        self.betting = False
                        self.deal_initial_cards()
                elif self.game_bust:
                    if event.key == pygame.K_4 and self.game_bust: # Reset after bust
                        self.game_bust = False
                        self.player.lose(self.aposta)
                        self.make_bet()
                elif self.game_running:
                    if event.key == pygame.K_h: # Hit
                        self.player.add_card(self.dealer.deal_card())
                    if event.key == pygame.K_s: # Stand
                        self.calculate_result()
                    if event.key == pygame.K_d: # Double down
                        self.aposta = self.aposta * 2
                        self.player.add_card(self.dealer.deal_card())
                        self.calculate_result()
                elif event.key == pygame.K_RETURN: # Start game
                    self.make_bet()
                    self.game_running = True
    
    #updating game status
    def update(self):
        if self.player.get_score() > 21:
            self.game_bust = True


    #draw the game interface
    def draw(self):
        font = pygame.font.Font(None, 36)
        hand_score = font.render(f"hand score is {self.player.get_score()}",True, colors.BOARD_COLOR)
        player_text = font.render(str(self.player), True, colors.BOARD_COLOR)
        dealer_text = font.render(str(self.dealer), True, colors.BOARD_COLOR)
        deck_text = font.render(str(self.dealer.deck), True, colors.BOARD_COLOR)
        bust_text = font.render(f"You busted, please restart", True, colors.BOARD_COLOR)
        beting_text = font.render(f"Make your bet:", True, colors.BOARD_COLOR)
        bet_text = font.render(f"Bet amount: {self.aposta}", True, colors.BOARD_COLOR)
        dealer_score_text = font.render(f"Dealer score is{self.dealer.get_score()}", True, colors.BOARD_COLOR)

        self.screen.blit(background,(0,0))
        self.screen.blit(player_text, (self.screen_width // 2 - player_text.get_width() // 2, self.screen_height // 2 - 50))
        self.screen.blit(dealer_text, (self.screen_width // 2 - dealer_text.get_width() // 2, self.screen_height // 2 + 50))
        self.screen.blit(deck_text, (self.screen_width // 2 - deck_text.get_width() // 2, self.screen_height // 2 + 100))
        if self.game_running:
            self.screen.blit(hand_score, (self.screen_width // 2 - hand_score.get_width() // 2, self.screen_height // 2 + 150))
            self.screen.blit(bet_text, (self.screen_width // 2 - bet_text.get_width() // 2, self.screen_height // 2 + 200))
            self.screen.blit(dealer_score_text, (self.screen_width // 2 - bet_text.get_width() // 2, self.screen_height // 2 + 250))
        if self.game_bust:
            self.screen.blit(bust_text, (self.screen_width // 2 - bust_text.get_width() // 2, self.screen_height // 2))
        if self.betting:
            self.screen.blit(beting_text,(self.screen_width // 2 - beting_text.get_width() // 2, self.screen_height // 2 - 100))