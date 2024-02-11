import pygame
from menu.colors import colors

class Button:
    """Class to represent a basic button"""
    
    def __init__(self, text, position, size):
        self.text = text
        self.position = position
        self.size = size
        self.rect = pygame.Rect(self.position, self.size)
        self.color = colors["rose_quartz"]
        self.hovered_color = colors["dark_green"]
        self.hovered = False
    
    def draw(self, screen):
        """ Draw the button with the text"""
        if self.hovered:
            pygame.draw.rect(screen, self.hovered_color, self.rect)
            color = colors["rose_quartz"]
        else:
            pygame.draw.rect(screen, self.color, self.rect)
            color = colors["dark_green"]
        
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, 1, color)
        textpos = text.get_rect(centerx=self.rect.centerx, centery=self.rect.centery)
        screen.blit(text, textpos)
    
    def check_hover(self, mouse_pos):
        """ Check if the button is hovered by the mouse """
        self.hovered = self.rect.collidepoint(mouse_pos)

