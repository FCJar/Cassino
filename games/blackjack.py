import pygame
import sys
from .game import Game
import includes.colors as colors
from includes.player import Player
from includes.dealer import Dealer

class Blackjack(Game):
    def __init__(self, screen, screen_width, screen_height):
        super().__init__(screen, screen_width, screen_height)
        self.player = Player("Player", 1000)  
        self.dealer = Dealer()
        self.deal_initial_cards()

    def deal_initial_cards(self):
        self.player.clear_hand()
        self.dealer.clear_hand()
        self.player.add_card(self.dealer.deal_card())
        self.player.add_card(self.dealer.deal_card())
        self.dealer.add_card_to_hand(self.dealer.deal_card())
        self.dealer.add_card_to_hand(self.dealer.deal_card())

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:  
                    self.player.add_card(self.dealer.deal_card())
                elif event.key == pygame.K_4:  
                    self.deal_initial_cards()

    def update(self):
        pass  

    def draw(self):
        self.screen.fill(colors.BOARD_COLOR)
        font = pygame.font.Font(None, 36)
        player_text = font.render(str(self.player), True, colors.BLACK_COLOR)
        dealer_text = font.render(str(self.dealer), True, colors.BLACK_COLOR)
        deck_text = font.render(str(self.dealer.deck), True, colors.BLACK_COLOR)
        self.screen.blit(player_text, (self.screen_width // 2 - player_text.get_width() // 2, self.screen_height // 2 - 50))
        self.screen.blit(dealer_text, (self.screen_width // 2 - dealer_text.get_width() // 2, self.screen_height // 2 + 50))
        self.screen.blit(deck_text, (self.screen_width // 2 - dealer_text.get_width() // 2, self.screen_height // 2 + 100))
