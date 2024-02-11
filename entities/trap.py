import pygame
import random
from math import sqrt
from menu.colors import colors

class Trap:
    """Class representing the traps"""
    
    def __init__(self, screen):
        """Constructor"""
        self.screen = screen
        self.radius = random.randint(40,150)
        self.color = colors['dark_green']
        self.position = self.generate_random_position()
    
    def generate_random_position(self):
        """Generate a random position"""
        position_x = random.randint(0, self.screen.get_width())
        position_y = random.randint(0, self.screen.get_height())
        
        return pygame.Vector2(position_x, position_y)
    
    def draw(self):
        """Draw traps"""        
        pygame.draw.circle(self.screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)
    
    def is_player_trapped(self, player):
        """Check if the player is trapped"""
        distance = sqrt((self.position.x - player.position.x)**2 + (self.position.y - player.position.y)**2)
        
        if abs(distance) - self.radius - player.size < 0:
            if player.size > self.radius:
                return True
        else:
            return False