import pygame

class Jogo:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rodando = True

    def run(self):
        while self.rodando = True
            self.controle_eventos()
            self.logica()
            self.Escreve_tela()
            pygame.display.flip()

    def controle_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
