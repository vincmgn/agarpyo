import sys
import pygame
from .colors import colors
from .button import Button

class Result:
    """Results screen"""
    
    def __init__(self, screen, player, options):
        self.screen = screen
        self.player = player
        self.options = options
        self.running = True
        
    def display(self):
        """Results screen"""
        button = Button("Back to main menu", (1280/2 - 300/2, 600), (300, 50))
        
        while self.running:
            for event in pygame.event.get():
                
                # Quit the game when the window is closed
                if event.type == pygame.QUIT:
                    self.running = False
                    
                # Quit the game when the 'l' key is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        self.running = False
                        sys.exit()
                    
                ## Back to main menu
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button.rect.collidepoint(event.pos):
                        self.running = False
                
                # Hover effects
                if event.type == pygame.MOUSEMOTION:
                    button.check_hover(event.pos)
            
            # Stats display
            font = pygame.font.Font(None, 36)
            fontTitle = pygame.font.Font(None, 80)
            title = fontTitle.render("- RESULTS -", True, colors["dark_green"])
            if self.options["difficulty"] == 2:
                difficultyStr = "Easy"
            elif self.options["difficulty"] == 3:
                difficultyStr = "Medium"
            elif self.options["difficulty"] == 4:
                difficultyStr = "Hard"
            difficulty = font.render("Difficulty: " + difficultyStr, True, colors["white"])
            gamewith = font.render("With: " + str(self.options["with"]), True, colors["white"])
            score = font.render("Score: " + str(self.player.score), True, colors["white"])
            size = font.render("Size: " + str(int(self.player.size)), True, colors["white"])
            speed = font.render("Speed: " + str(int(self.player.speed)), True, colors["white"])
            titlepos = title.get_rect(centerx=self.screen.get_width()/2, centery=100)
            difficultypos = difficulty.get_rect(centerx=self.screen.get_width()/2, centery=200)
            gamewithpos = gamewith.get_rect(centerx=self.screen.get_width()/2, centery=250)
            scorepos = score.get_rect(centerx=self.screen.get_width()/2, centery=300)
            sizepos = size.get_rect(centerx=self.screen.get_width()/2, centery=350)
            speedpos = speed.get_rect(centerx=self.screen.get_width()/2, centery=400)
            
            # Drawing on the screen
            self.screen.fill(colors["amethyst"])
            self.screen.blit(title, titlepos)
            self.screen.blit(difficulty, difficultypos)
            self.screen.blit(gamewith, gamewithpos)
            self.screen.blit(score, scorepos)
            self.screen.blit(size, sizepos)
            self.screen.blit(speed, speedpos)
            
            # Drawing the button
            button.draw(self.screen)
            
            # Update the display
            pygame.display.flip()

        return False

    def initResultsScreen(self):
        """Initialize the results screen"""
        width = 1280
        height = 720
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Agarpyo - Results")
        return screen
