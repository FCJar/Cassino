import pygame
import sys
from .game import Game
import includes.colors as colors
from includes.Player import Player
from includes.Dealer import Dealer

class Blackjack(Game):
    def __init__(self, screen, screen_width, screen_height):
        super().__init__(screen, screen_width, screen_height)
        self.player = Player("Player", 1000)  
        self.dealer = Dealer()
        self.game_running = False
        self.game_bust = False
        self.betting = False
        self.aposta = 0

    def deal_initial_cards(self):
        self.dealer.create_deck()
        self.player.add_card(self.dealer.deal_card())
        self.player.add_card(self.dealer.deal_card())
        self.dealer.add_card_to_hand(self.dealer.deal_card())
        self.dealer.add_card_to_hand(self.dealer.deal_card())

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

    def make_bet(self):
        self.betting = True
        self.aposta = 0
        self.player.clear_hand()
        self.dealer.clear_hand()

    def handle_events(self):
        for event in pygame.event.get():
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

    def update(self):
        if self.player.get_score() > 21:
            self.game_bust = True

    def draw(self):
        font = pygame.font.Font(None, 36)
        hand_score = font.render(f"hand score is {self.player.get_score()}",True, colors.BLACK_COLOR)
        player_text = font.render(str(self.player), True, colors.BLACK_COLOR)
        dealer_text = font.render(str(self.dealer), True, colors.BLACK_COLOR)
        deck_text = font.render(str(self.dealer.deck), True, colors.BLACK_COLOR)
        bust_text = font.render(f"You busted, please restart", True, colors.BLACK_COLOR)
        beting_text = font.render(f"Make your bet:", True, colors.BLACK_COLOR)
        bet_text = font.render(f"Bet amount: {self.aposta}", True, colors.BLACK_COLOR)
        dealer_score_text = font.render(f"Dealer score is{self.dealer.get_score()}", True, colors.BLACK_COLOR)

        self.screen.fill(colors.BOARD_COLOR)
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