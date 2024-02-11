import pygame
import random
from math import sqrt
from menu.colors import colors

class Food:
    """Class representing the food"""
    
    def __init__(self, screen):
        """Constructor"""
        self.screen = screen
        self.radius = 20
        self.color = colors['rosy_brown']
        self.position = self.generate_random_position()
    
    def generate_random_position(self):
        """Generate a random position"""
        position_x = random.randint(0, self.screen.get_width())
        position_y = random.randint(0, self.screen.get_height())
        return pygame.Vector2(position_x, position_y)
    
    def draw(self):
        """Draw food"""
        pygame.draw.circle(self.screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)
        
    def is_near_player(self, player):
        """Check if food is eaten"""
        distance = sqrt((self.position.x - player.position.x)**2 + (self.position.y - player.position.y)**2)
        if abs(distance) - self.radius - player.size < 0:
            return True
        else:
            return False