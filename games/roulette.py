import pygame
from .game import Game
import includes.colors as colors
import random
import sys

class Roulette(Game):
    def __init__(self, screen, screen_width, screen_height):
        super().__init__(screen, screen_width, screen_height)
        self.bet = None
        self.result = None
        self.roulette_numbers = list(range(37))  # 0-36

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_RETURN:
                    self.spin_roulette()
                elif event.unicode.isdigit():
                    self.bet = int(event.unicode)
                    if self.bet < 0 or self.bet > 36:
                        self.bet = None  # Aposta inválida, redefine

    def spin_roulette(self):
        self.result = random.choice(self.roulette_numbers)
        print(f"Resultado: {self.result}")

    def update(self):
        pass

    def draw(self):
        self.screen.fill(colors.WHITE_COLOR)
        if self.bet is not None:
            font = pygame.font.Font(None, 36)
            bet_text = font.render(f"Aposta: {self.bet}", True, colors.BLACK_COLOR)
            self.screen.blit(bet_text, (self.screen_width//2 - bet_text.get_width()//2, self.screen_height//2 - bet_text.get_height()//2 - 50))
        if self.result is not None:
            font = pygame.font.Font(None, 36)
            result_text = font.render(f"Resultado: {self.result}", True, colors.RED_COLOR)
            self.screen.blit(result_text, (self.screen_width//2 - result_text.get_width()//2, self.screen_height//2 - result_text.get_height()//2 + 50))
        else:
            font = pygame.font.Font(None, 36)
            instructions_text = font.render("Pressione um número para apostar e Enter para girar", True, colors.BLACK_COLOR)
            self.screen.blit(instructions_text, (self.screen_width//2 - instructions_text.get_width()//2, self.screen_height//2 - instructions_text.get_height()//2 + 100))
