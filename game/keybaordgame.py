import pygame
from game.game import Game

class KeyboardGame(Game):
    """Class representing the game with keyboard control"""
    
    def __init__(self, options):
        """Constructor"""
        super().__init__(options)
        self.keys_pressed = {}
    
    def event_handler(self, event):
        """Handle keyboard events"""
        if event.type == pygame.KEYDOWN:
            self.keys_pressed[event.key] = True
            self.player.set_direction_keyboard(self.keys_pressed)
        if event.type == pygame.KEYUP:
            if event.key in self.keys_pressed:
                del self.keys_pressed[event.key]