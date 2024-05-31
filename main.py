#imports globais
import pygame

import random

#imports locais

pygame.init()
# Informações da janela 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cartas uwu")

# Variáveis de Jogo
jogo_pausado = False

# Definindo cores
BLACK = (0,0,0)
RED = (255,0,0)
COR_TEXTO = (255,255,255)

# Definindo fonte
fonte = pygame.font.SysFont("arialblack", 40)

def Escrever_Tela(texto, fonte, COR_TEXTO, x, y):
    img = fonte.render(texto, True, COR_TEXTO)
    screen.blit(img,(x,y))

run = True
while run:
    
    if jogo_pausado == True:
        screen.fill(BLACK)
        Escrever_Tela("Tela de pausa", fonte, COR_TEXTO, 160, 250)
    else:
        screen.fill(RED)
        Escrever_Tela("Teste De TexTo", fonte, COR_TEXTO, 160, 250)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jogo_pausado = True
                
            if event.key == pygame.K_ESCAPE:
                jogo_pausado = False
        if event.type == pygame.QUIT:
            print("quit")
            run = False

    pygame.display.update()
    
pygame.quit() 