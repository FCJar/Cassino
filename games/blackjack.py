import pygame
import sys
import os
from .game import Game
import includes.colors as colors
from includes.Player import Player
from includes.Dealer import Dealer
from assets.text_helpers import draw_text_with_background, draw_text_with_shadow

current_path = os.path.dirname(__file__)
background_path = os.path.join(current_path, '..', 'assets', 'images', 'blackjack.jpg')
background=pygame.image.load(background_path)

class Blackjack(Game):
    def __init__(self, screen, screen_width, screen_height):
        super().__init__(screen, screen_width, screen_height)
        self.player = Player("Player", 1000)  
        self.dealer = Dealer()
        self.game_running = False
        self.game_bust = False
        self.betting = False
        self.aposta = 0
        self.load_card_images()
    
    def load_card_images(self):
        self.card_images = {}
        card_width, card_height = 100, 144  # Defina o tamanho desejado das cartas aqui
        for rank in range(1, 14):
            for suit in range(1, 5):
                card_code = f"{rank:02}{suit}"
                image_path = os.path.join(current_path, '..', 'assets', 'cards', f'{card_code}.png')
                try:
                    image = pygame.image.load(image_path).convert_alpha()
                    # Redimensionar a imagem para o novo tamanho
                    self.card_images[card_code] = pygame.transform.scale(image, (card_width, card_height))
                    print(f"Loaded and resized image {card_code}.png successfully")
                except pygame.error as e:
                    print(f"Failed to load image {image_path}: {e}")


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
        self.screen.blit(background, (0, 0))
        font = pygame.font.Font(None, 36)
        draw_text_with_shadow(self.screen, "Dealer must hit until 17", font, colors.DARK_RED_COLOR, colors.BLACK_COLOR, (self.screen_width // 2, 50))

        # Inicia as posições das cartas na tela
        player_start_x = 100
        player_start_y = 200
        offset_x = 30  # Deslocamento horizontal entre as cartas
        angle = -5  # Ângulo de rotação para o efeito visual

        # Desenha as cartas do jogador
        for i, card in enumerate(self.player.hand):
            card_image = pygame.transform.rotate(self.card_images[card.code], i * angle)
            self.screen.blit(card_image, (player_start_x + i * offset_x, player_start_y))
            
        dealer_start_x = 800
        dealer_start_y = 200
        angle = 5  # Ângulo de rotação para o efeito visual

        # Desenha as cartas do dealer
        for i, card in enumerate(self.dealer.hand):
            card_image = pygame.transform.rotate(self.card_images[card.code], i * angle)
            self.screen.blit(card_image, (dealer_start_x + i * offset_x, dealer_start_y))


        hand_score = font.render(f"hand score is {self.player.get_score()}",True, colors.BOARD_COLOR)
        deck_text = font.render(str(self.dealer.deck), True, colors.BOARD_COLOR)
        bust_text = font.render(f"You busted, please restart", True, colors.BOARD_COLOR)
        beting_text = font.render(f"Make your bet:", True, colors.BOARD_COLOR)
        bet_text = font.render(f"Bet amount: {self.aposta}", True, colors.BOARD_COLOR)

        self.screen.blit(deck_text, (self.screen_width // 2 - deck_text.get_width() // 2, self.screen_height // 2 + 100))
        if self.game_running:
            self.screen.blit(hand_score, (self.screen_width // 2 - hand_score.get_width() // 2, self.screen_height // 2 + 150))
            self.screen.blit(bet_text, (self.screen_width // 2 - bet_text.get_width() // 2, self.screen_height // 2 + 200))
        if self.game_bust:
            self.screen.blit(bust_text, (self.screen_width // 2 - bust_text.get_width() // 2, self.screen_height // 2))
        elif self.betting:
            self.screen.blit(beting_text,(self.screen_width // 2 - beting_text.get_width() // 2, self.screen_height // 2 - 100))
        
        pygame.display.flip()  