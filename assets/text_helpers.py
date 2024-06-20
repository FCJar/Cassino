import pygame
import includes.colors as colors

def draw_text_with_shadow(screen, text, font, color, shadow_color, position, offset=(2, 2)):
    text_surface = font.render(text, True, color)
    shadow_surface = font.render(text, True, shadow_color)

    text_rect = text_surface.get_rect(center=position)
    shadow_rect = text_rect.copy()
    shadow_rect.x += offset[0]
    shadow_rect.y += offset[1]

    screen.blit(shadow_surface, shadow_rect)
    screen.blit(text_surface, text_rect)

def draw_text_with_background(screen,text, position, font, text_color, bg_color, alignment='center', padding=10, border_thickness=2, border_color=colors.BLACK_COLOR):
        text_surface = font.render(text, True, text_color)
        if alignment == 'center':
            text_rect = text_surface.get_rect(center=position)
        elif alignment == 'left':
            text_rect =text_surface.get_rect(midleft = position)
        elif alignment == 'right':
            text_rect = text_surface.get_rect(midright=position)

        background_rect = text_rect.inflate(padding, padding)
        border_rect = background_rect.inflate(border_thickness * 2, border_thickness * 2)
        pygame.draw.rect(screen, border_color, border_rect)
        pygame.draw.rect(screen, bg_color, background_rect)
        screen.blit(text_surface, text_rect)
