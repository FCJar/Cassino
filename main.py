import pygame

import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BLACK = (0,0,0)
RED = (255,0,0)
pygame.display.set_caption("Cartas uwu")

boxes = []
images = []

for i in range(0,3):
    x,y = random.randint(1,100), random.randint(1,200)

    temp_img = pygame.image.load(f"{i}.png").convert_alpha()
    image = pygame.transform.scale(temp_img, (100,100))
    object_rect = image.get_rect()
    object_rect.center = (x,y)
    boxes.append(object_rect)
    images.append(image)

active_box = None

run = True
while run:
    
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    index=0
    for image in images:
        screen.blit(image,boxes[index])
        index+=1
    
    pygame.display.update()
    
pygame.quit()