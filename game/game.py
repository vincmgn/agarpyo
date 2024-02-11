import sys
import pygame
from menu.colors import colors
from entities.player import Player
from entities.food import Food
from entities.trap import Trap
from menu.result import Result

class Game:
    """Class representing the game"""
    
    def __init__(self, options):
        """Constructor"""
        self.screen = self.initGameScreen()
        self.running = True
        self.options = options
        self.player = Player()
        self.foods = []
        self.traps = []
        self.time_left = 60
    
    def start_game(self):
        """Start the game"""        
        self.generate_food()
        self.generate_traps()
        while self.running:    
            for event in pygame.event.get():
                # Quit the game when the window is closed
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()    
                    sys.exit()               
                
                # Quit the game when the 'l' key is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        self.running = False
                        pygame.quit()
                        sys.exit()
                
                # Display the menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                        self.running = False
                        break
                    
                # Handle the events
                self.event_handler(event)
            
            # Background color
            self.screen.fill(colors["amethyst"])
            
            # Timer 
            dt = pygame.time.Clock().tick(60) / 1000
            self.time_left -= dt
            self.end_game(self.time_left)
            
            # Move the player
            self.player.move(dt, self.screen, self.options)
            
            # Check
            self.check_eaten_food()
            self.check_trapped()
            
            # Draw the player, foods and traps
            self.player.draw(self.screen)
            for food in self.foods:
                food.draw()
            for trap in self.traps:
                trap.draw()
            
            # Display the stats
            self.display_stats(self.screen, self.player.score, self.player.size, self.player.speed)
            
            # Update the display
            pygame.display.flip()
    
    def display_stats(self, screen, score, size, speed):
        """Display the stats"""
        # Create texts
        font = pygame.font.Font(None, 30)
        text_score = font.render("Score: " + str(int(score)), True, colors["white"])
        text_size = font.render("Size: " + str(int(size)), True, colors["white"])
        text_speed = font.render("Speed: " + str(int(speed)), True, colors["white"])
        if self.options["difficulty"] == 2:
            boost = "x1"
        elif self.options["difficulty"] == 3:
            boost = "x1.5"
        elif self.options["difficulty"] == 4:
            boost = "x2"
        text_boost = font.render("Speed boost: " + str(boost), True, colors["white"])
        text_time = font.render("Time left : " + str(int(self.time_left)) + "s", True, colors["white"])
        if self.options["difficulty"] == 2:
            difficulty = "Easy"
        elif self.options["difficulty"] == 3:
            difficulty = "Medium"
        elif self.options["difficulty"] == 4:
            difficulty = "Hard"
        text_difficulty = font.render("Difficulty: " + difficulty, True, colors["white"])
        
        # Display the stats
        screen.blit(text_score, (10, 10))
        screen.blit(text_size, (10, 40))
        screen.blit(text_speed, (10, 70))
        screen.blit(text_time, (self.screen.get_width() - 200, 10))
        screen.blit(text_difficulty, (self.screen.get_width() - 200, 40))
        screen.blit(text_boost, (self.screen.get_width() - 200, 70))
    
    def end_game(self, time_left):
        """End the game if the time is over"""
        if time_left <= 0:
            self.running = False
            results = Result(self.screen, self.player, self.options)
            results.display()
    
    def generate_food(self):
        """Generate food in function of the options"""
        num_food = 0
        if self.options["difficulty"] == 2:
            num_food = 5
        elif self.options["difficulty"] == 3:
            num_food = 3
        elif self.options["difficulty"] == 4:
            num_food = 2
        
        for _ in range(num_food):
            food = Food(self.screen)
            food.generate_random_position()
            self.foods.append(food)
    
    def check_eaten_food(self):
        """Check if the food is eaten"""
        for food in self.foods:
            if food.is_near_player(self.player):
                self.foods.remove(food)
                
                new_food = Food(self.screen)
                new_food.generate_random_position()
                self.foods.append(new_food)
                
                self.player.score += 1
                if self.player.size < self.player.MAX_SIZE:
                    self.player.size += 2
                if self.player.speed < self.player.MAX_SPEED:
                    self.player.speed += 5
    
    def generate_traps(self):
        """Generate traps in function of the options"""
        num_traps = 0
        if self.options["difficulty"] == 2:
            num_traps = 2
        elif self.options["difficulty"] == 3:
            num_traps = 3
        elif self.options["difficulty"] == 4:
            num_traps = 4
        
        for _ in range(num_traps):
            trap = Trap(self.screen)
            trap.generate_random_position()
            self.traps.append(trap)     
    
    def check_trapped(self):
        """Check if the player is trapped"""
        for trap in self.traps:
            if trap.is_player_trapped(self.player):
                self.traps.remove(trap)
                new_trap = Trap(self.screen)
                new_trap.generate_random_position()
                self.traps.append(new_trap)
                
                # Check size and speed
                self.player.size /= self.options["difficulty"]
                if self.player.size < self.player.MIN_SIZE:
                    self.player.size = self.player.MIN_SIZE
                    
                self.player.speed /= self.options["difficulty"]
                if self.player.speed < self.player.MIN_SPEED:
                    self.player.speed = self.player.MIN_SPEED
    
    def initGameScreen(self):
        """Initialize the game screen"""
        width = 1280
        height = 720
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Agarpyo - Game")
        return screen