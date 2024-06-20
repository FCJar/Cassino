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
    #builder
    def __init__(self, screen, screen_width, screen_height):
        super().__init__(screen, screen_width, screen_height)
        self.player = Player("Player", 1000)
        self.player.readData()  
        self.dealer = Dealer()
        self.game_running = True
        self.game_bust = False
        self.betting = False
        self.dealer_reveals = False
        self.aposta = 0
        self.result = None
        self.show_result = False
        self.show_dealer_score = False
        self.load_card_images()
        self.make_bet()
    
    def load_card_images(self):
        self.card_images = {}
        card_width, card_height = 100, 144  # Defina o tamanho desejado das cartas aqui
        image_path = os.path.join(current_path, '..', 'assets', 'cards', 'back.png')
        image = pygame.image.load(image_path).convert_alpha()
        self.card_images['back'] = pygame.transform.scale(image, (card_width, card_height))
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


    # distribute the initial cards
    def deal_initial_cards(self):
        self.dealer.create_deck()
        self.player.add_card(self.dealer.deal_card())
        self.player.add_card(self.dealer.deal_card())
        hidden_card = self.dealer.deal_card()  # Carta que será oculta
        hidden_card.hide()
        self.dealer.add_card_to_hand(hidden_card)
        self.dealer.add_card_to_hand(self.dealer.deal_card())


    #  calculate the game result
    def calculate_result(self):
        self.show_dealer_score = True
        self.dealer.hand[0].reveal()  # Revela a primeira carta 
        self.draw()  
        pygame.display.flip()

        next_card_time = pygame.time.get_ticks() + 2000  # Define o momento para a próxima carta
        if self.game_bust:
            self.player.lose(self.aposta)
            self.result = 'Lose'
            self.show_dealer_score = False
            self.show_result = True
        else:
            while self.dealer.get_score() < 17:
                if pygame.time.get_ticks() >= next_card_time:
                    new_card = self.dealer.deal_card()
                    self.dealer.add_card_to_hand(new_card)
                    self.draw()  # Atualiza a interface para mostrar a nova carta
                    pygame.display.flip()
                    next_card_time = pygame.time.get_ticks() + 2000

            if self.dealer.get_score() > 21:
                self.player.win(self.aposta)
                self.result = 'Win' 
            elif self.player.get_score() > self.dealer.get_score():
                self.player.win(self.aposta)
                self.result = 'Win'
            elif self.player.get_score() < self.dealer.get_score():
                self.player.lose(self.aposta)
                self.result = 'Lose'
            self.show_dealer_score = False
            self.show_result = True

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
                elif self.show_result and not self.game_bust:
                    if event.key == pygame.K_RETURN: # Start game
                        self.make_bet()
                        self.show_result = False
                elif self.betting: 
                    if event.key == pygame.K_1: # Bet 10 chips
                        self.aposta += 10
                    if event.key == pygame.K_2: # Bet 50 chips
                        self.aposta += 50
                    if event.key == pygame.K_3: # Bet 100 chips
                        self.aposta += 100
                    if event.key == pygame.K_4: # Bet 500 chips
                        self.aposta += 500
                    if event.key == pygame.K_RETURN and self.aposta != 0: # Confirm Bet
                        self.betting = False
                        self.deal_initial_cards()
                elif self.game_bust:
                    if event.key == pygame.K_RETURN and self.game_bust: # Reset after bust
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
    
    #updating game status
    def update(self):
        if self.player.get_score() > 21:
            self.game_bust = True


    #draw the game interface
    def draw(self):
        self.screen.blit(background, (0, 0))
        font = pygame.font.Font(None, 36)
        draw_text_with_shadow(self.screen, "Dealer must hit until 17", font, colors.DARK_RED_COLOR, colors.BLACK_COLOR,(self.screen_width // 2, 50),'center')
        player_text =("Name: " + self.player.get_name())
        chips_text = ("Chips: " + str(self.player.get_chips()))
        draw_text_with_background(self.screen, chips_text,(self.screen_width // 2  + 420, self.screen_height//2 -333), font, colors.LIGHT_BLUE_COLOR, colors.GRAY_COLOR)
        draw_text_with_background(self.screen, player_text,(self.screen_width // 2  - 420, self.screen_height//2 -333), font, colors.LIGHT_BLUE_COLOR, colors.GRAY_COLOR)
        
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
            if card.hidden:
                card_image = self.card_images['back']
            else:
                card_image = pygame.transform.rotate(self.card_images[card.code], i * angle)
            self.screen.blit(card_image, (dealer_start_x + i * offset_x, dealer_start_y))

        # Desenha os textos relevantes para o jogo
        if self.game_running and not self.betting:
            draw_text_with_background(self.screen, 'Press H to Hit',(self.screen_width // 2  - 410, self.screen_height//2 + 150), font, colors.BLACK_COLOR, colors.GRAY_COLOR)
            draw_text_with_background(self.screen, 'Press S to Stand',(self.screen_width // 2  - 400, self.screen_height//2 + 200), font, colors.BLACK_COLOR, colors.GRAY_COLOR)
            draw_text_with_background(self.screen, 'Press D to Double Down',(self.screen_width // 2  - 355, self.screen_height//2 + 250), font, colors.BLACK_COLOR, colors.GRAY_COLOR)
            draw_text_with_background(self.screen, f"Hand score: {self.player.get_score()}",(self.screen_width // 2  - 400, self.screen_height//2 + 30 ), font, colors.BLUE_COLOR, colors.GRAY_COLOR)
            draw_text_with_background(self.screen, f"Bet amount: {self.aposta}", (self.screen_width // 2 , self.screen_height // 2 + 200), font, colors.SILVER_COLOR, colors.GRAY_COLOR)
            if self.show_dealer_score:
                draw_text_with_background(self.screen, f"Dealer score: {self.dealer.get_score()}",(self.screen_width // 2  + 400, self.screen_height//2 + 30 ), font, colors.BLUE_COLOR, colors.GRAY_COLOR)        
        if self.game_bust:
            draw_text_with_shadow(self.screen, 'You busted, press enter to restart',font, colors.RED_COLOR, colors.BLACK_COLOR,(self.screen_width // 2 , self.screen_height // 2),'center')
        elif self.betting:
            draw_text_with_background(self.screen, 'Press 1 to bet 10',(self.screen_width // 2  - 410, self.screen_height//2 + 150), font, colors.BLACK_COLOR, colors.GRAY_COLOR)
            draw_text_with_background(self.screen, 'Press 2 to bet 50',(self.screen_width // 2  - 410, self.screen_height//2 + 200), font, colors.BLACK_COLOR, colors.GRAY_COLOR)
            draw_text_with_background(self.screen, 'Press 3 to bet 100',(self.screen_width // 2  - 410, self.screen_height//2 + 250), font, colors.BLACK_COLOR, colors.GRAY_COLOR)
            draw_text_with_background(self.screen, 'Press 4 to bet 500',(self.screen_width // 2  - 410, self.screen_height//2 + 300), font, colors.BLACK_COLOR, colors.GRAY_COLOR)
            draw_text_with_background(self.screen, f"Bet amount: {self.aposta}", (self.screen_width  // 2, self.screen_height // 2 + 200), font, colors.SILVER_COLOR, colors.GRAY_COLOR)
            draw_text_with_shadow(self.screen, 'Make your bet:',font, colors.SILVER_COLOR, colors.BLACK_COLOR,(self.screen_width // 2, 100),'center')
        elif self.show_result:
            draw_text_with_background(self.screen, 'Press enter to redraw',(self.screen_width // 2, self.screen_height // 2 ), font, colors.DARK_RED_COLOR, colors.GRAY_COLOR)
            draw_text_with_background(self.screen, f"Dealer score: {self.dealer.get_score()}",(self.screen_width // 2  + 400, self.screen_height//2 + 30 ), font, colors.BLUE_COLOR, colors.GRAY_COLOR)
            if self.result == 'Win':
                draw_text_with_shadow(self.screen, 'YOU WIN',font, colors.GOLD_COLOR, colors.BLACK_COLOR, (self.screen_width // 2, 100),'center')
            if self.result == 'Lose':
                draw_text_with_shadow(self.screen, 'You Lose',font, colors.RED_COLOR, colors.BLACK_COLOR,(self.screen_width // 2, 100),'center')
        
        pygame.display.flip()  