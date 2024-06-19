import pygame
import sys 
import os
import includes.colors as colors
from includes.Player import Player

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, '..', 'assets', 'images', 'main_background.jpg')
main_background=pygame.image.load(image_path)


class MainMenu:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.running = True
        self.selection = None
        self.Pl=Player('Jose',15000)
        self.Pl.readData()

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()

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

    def draw(self):
        fonte_base = pygame.font.Font(None, 36)
        fonte_titulo = pygame.font.Font(None, 72)
        fonte_player = pygame.font.Font(None,36)
        self.screen.fill(colors.WHITE_COLOR)
        self.screen.blit(main_background,(0,0))
        text = fonte_titulo.render("Welcome to Cassino", True, colors.BLUE_COLOR)
        self.screen.blit(text,(self.screen_width//2 - text.get_width()//2, self.screen_height//2 - text.get_height()//2- 150))
        text=fonte_player.render(("Player name:: " + self.Pl.get_name() + "      Actual chips:: " + str(self.Pl.get_chips())),True,colors.BOARD_COLOR)
        self.screen.blit(text,(self.screen_width//2 - text.get_width()//2, self.screen_height//2 - text.get_height()//2))
        text = fonte_base.render("Press 1 to play Blackjack", True, colors.GREEN_COLOR)
        self.screen.blit(text, (self.screen_width//2 - text.get_width()//2, self.screen_height//2 - text.get_height()//2 + 50))
        text = fonte_base.render("Press 2 to play lucky roulette", True, colors.GREEN_COLOR)
        self.screen.blit(text, (self.screen_width//2 - text.get_width()//2, self.screen_height//2 - text.get_height()//2 + 100))
        text = fonte_base.render("Press 3 to exit",True,colors.GREEN_COLOR)
        self.screen.blit(text,(self.screen_width//2 - text.get_width()//2, self.screen_height//2 - text.get_height()//2 + 150))