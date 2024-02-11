import random
import pygame
from menu.colors import colors

class Player:
    """Class representing the player"""
    INITIAL_POSITION = pygame.Vector2(640, 360)
    MIN_SPEED = 100
    MAX_SPEED = 500
    MIN_SIZE = 40
    MAX_SIZE = 200
    
    def __init__(self):
        """Constructor"""
        self.position = Player.INITIAL_POSITION
        self.direction = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()
        self.color = colors['mauve']
        self.radius = 40
        self.score = 0
        self.speed = 100
        self.size = 40
    
    def draw(self, screen):
        """Draw player"""
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.size)
    
    def move(self, dt, screen, opptions):
        """Move player"""
        if opptions["difficulty"] == 2:
            boost = 1
        elif opptions["difficulty"] == 3:
            boost = 1.5
        elif opptions["difficulty"] == 4:
            boost = 2
        
        self.position += self.direction * (self.speed * boost) * dt
        
        if self.position.x < 0:
            self.position.x = screen.get_width()
        elif self.position.x > screen.get_width():
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = screen.get_height()
        elif self.position.y > screen.get_height():
            self.position.y = 0
            
        self.position.x = min(screen.get_width(), max(0, self.position.x))
        self.position.y = min(screen.get_height(), max(0, self.position.y))
    
    def set_direction_keyboard(self, key_pressed):
        """Set the direction of the player using the keyboard"""
        direction_x = 0
        direction_y = 0
        for key in key_pressed:
            if key == pygame.K_z or key == pygame.K_UP:
                direction_y -= 1
            elif key == pygame.K_q or key == pygame.K_LEFT:
                direction_x -= 1
            elif key == pygame.K_s or key == pygame.K_DOWN:
                direction_y += 1
            elif key == pygame.K_d or key == pygame.K_RIGHT:
                direction_x += 1
        if direction_x != 0 or direction_y != 0:
            self.direction = pygame.Vector2(direction_x, direction_y).normalize()
    
    def set_direction_mouse(self, mouse_pos):
        """Set the direction of the player using the mouse"""
        self.direction = mouse_pos - self.position
        
        if self.direction.length() != 0:
            self.direction = self.direction.normalize()