import pygame
import sys
from games.menu import MainMenu
from games.blackjack import Blackjack
from games.roulette import Roulette

def main():
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Cassino")

    while True:
        menu = MainMenu(screen, screen_width, screen_height)
        menu.run()
        
        if menu.selection == "blackjack":
            game = Blackjack(screen, screen_width, screen_height)
        elif menu.selection == "roulette":
            game = Roulette(screen, screen_width, screen_height)
        
        if game:
            game.run()

main()
