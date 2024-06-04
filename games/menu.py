import pygame
import sys 
import includes.colors as colors


class MainMenu:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.running = True
        self.selection = None

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

    def draw(self):
        fonte_base = pygame.font.Font(None, 36)
        fonte_titulo = pygame.font.Font(None, 72)
        self.screen.fill(colors.WHITE_COLOR)
        text = fonte_titulo.render("Bem Vindo ao cassino", True, colors.BLUE_COLOR)
        self.screen.blit(text,(self.screen_width//2 - text.get_width()//2, self.screen_height//2 - text.get_height()//2- 150))
        text = fonte_base.render("Pressione 1 para jogar Blackjack", True, (0, 0, 0))
        self.screen.blit(text, (self.screen_width//2 - text.get_width()//2, self.screen_height//2 - text.get_height()//2 + 50))
        text = fonte_base.render("Pressione 2 para jogar Roleta", True, (0, 0, 0))
        self.screen.blit(text, (self.screen_width//2 - text.get_width()//2, self.screen_height//2 - text.get_height()//2 + 100))