import pygame
import sys 
import os
import includes.colors as colors
from includes.Player import Player
from assets.text_helpers import draw_text_with_background, draw_text_with_shadow

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, '..', 'assets', 'images', 'main_background.jpg')
main_background = pygame.image.load(image_path)

class MainMenu:
    #builder
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.running = True
        self.selection = None
        self.Pl = Player('Jose', 15000)
        self.Pl.readData()

    #draw the interface and procesing the events
    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()
    
    #procesing the events and inputs
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.selection = "blackjack"
                    self.running = False
                elif event.key == pygame.K_2:
                    self.selection = "roulette"
                    self.running = False
                elif event.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()

    #draw the interface
    def draw(self):
        fonte_base = pygame.font.Font(None, 36)
        fonte_titulo = pygame.font.Font(None, 72)
        fonte_player = pygame.font.Font(None, 36)
        self.screen.fill(colors.WHITE_COLOR)
        self.screen.blit(main_background, (0, 0))
        player_info_position = (self.screen_width - 10, 10)
        draw_text_with_background(self.screen,"Welcome to Cassino", (self.screen_width // 2, self.screen_height // 2 - 150), fonte_titulo, colors.BLUE_COLOR, colors.GRAY_COLOR)
        draw_text_with_background(self.screen,("Player name: " + self.Pl.get_name() + "    Chips: " + str(self.Pl.get_chips())), player_info_position, fonte_player, colors.BOARD_COLOR, colors.WHITE_COLOR, alignment='right')
        draw_text_with_background(self.screen,"Press 1 to play Blackjack", (self.screen_width // 2, self.screen_height // 2 + 50), fonte_base, colors.DARK_RED_COLOR, colors.GRAY_COLOR)
        draw_text_with_background(self.screen,"Press 2 to play lucky roulette", (self.screen_width // 2, self.screen_height // 2 + 100), fonte_base, colors.DARK_RED_COLOR, colors.GRAY_COLOR)
        draw_text_with_background(self.screen,"Press 3 to exit", (self.screen_width // 2, self.screen_height // 2 + 150), fonte_base, colors.DARK_RED_COLOR, colors.GRAY_COLOR)
