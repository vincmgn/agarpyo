import pygame
from game.game import Game
from entities.player import Player

class MouseGame(Game):
    """Class representing the game with mouse control"""
    
    def __init__(self, options):
        """Constructor"""
        super().__init__(options)
        self.mouse_pos = pygame.Vector2(0, 0)
    
    def event_handler(self, event):
        """Handle mouse events"""
        if event.type == pygame.MOUSEMOTION:
            self.mouse_pos = pygame.Vector2(event.pos)
            self.player.set_direction_mouse(self.mouse_pos)
