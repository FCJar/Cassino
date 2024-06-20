import pygame
import sys
from abc import ABC, abstractmethod

class Game(ABC):
    #builder
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.running = True
        
    #perform the basic game mechanics
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()

    #processing game input events
    @abstractmethod
    def handle_events(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    #draw the game interface
    @abstractmethod
    def draw(self):
        pass