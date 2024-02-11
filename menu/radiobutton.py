import pygame
from .colors import colors
from .button import Button

class RadioButton(Button):
    """ Class to represent a radio button """
    
    def __init__(self, text, position, size):
        super().__init__(text, position, size)
        self.radius = size[0] // 2
        self.selected = False

    def draw(self, screen):
        """ Draw the radio button with the text"""
        
        # Draw the button
        if self.selected:
            pygame.draw.circle(screen, self.hovered_color if self.hovered else self.color, self.rect.center, self.radius)
            pygame.draw.circle(screen, colors["dark_green"], self.rect.center, self.radius // 2)
        else:
            pygame.draw.circle(screen, self.hovered_color if self.hovered else self.color, self.rect.center, self.radius)
        
        # Draw the text
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, colors["dark_green"])
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.centerx, self.rect.centery + self.radius + 20
        screen.blit(text_surface, text_rect)
    
    def toggle_selected(self):
        """ Toggle the selected state of the button """
        self.selected = not self.selected
