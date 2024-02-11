import pygame
from game.keybaordgame import KeyboardGame
from game.mousegame import MouseGame
from .colors import colors
from .radiobutton import RadioButton
from .button import Button

class Menu:
    """The main menu of the game"""
    
    def __init__(self):
        self.screen = self.initMenuScreen()
        self.running = True
        self.options = {
            "difficulty": 2,
            "with": "Keyboard"
        }
    
    def mainMenu(self):
        """ Main menu of the game """
        # List comprehension pour JP
        radio_buttons_text = ["Easy", "Medium", "Hard"]
        radio_buttons = [RadioButton(text, (1280/4 + i * 300, 600), (50, 50)) for i, text in enumerate(radio_buttons_text)]
        radio_buttons[0].selected = True
        button_text = ["Play with keyboard (K)", "Play with mouse", "Exit (L)"]
        buttons = [Button(text, ((1280/2 - 350/2), 210 + i * 100), (350, 50)) for i, text in enumerate(button_text)]
        
        # Menu loop
        while self.running:
            for event in pygame.event.get():
                
                # Quit the game when the window is closed
                if event.type == pygame.QUIT:
                    self.running = False
                
                # Quit the game when the 'l' key is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        self.running = False
                    if event.key == pygame.K_k:
                        self.options["with"] = "Keyboard"
                        keyboard_game = KeyboardGame(self.options)
                        keyboard_game.start_game()
                
                ## Game choice
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    # Radio buttons
                    for button in radio_buttons:
                        if button.rect.collidepoint(event.pos):
                            for other in radio_buttons:
                                if other != button:
                                    other.selected = False
                                    other.draw(self.screen)
                            button.toggle_selected()
                            button.draw(self.screen)
                            
                            if button.selected:
                                if button.text == "Easy":
                                    self.options["difficulty"] = 2
                                elif button.text == "Medium":
                                    self.options["difficulty"] = 3
                                elif button.text == "Hard":
                                    self.options["difficulty"] = 4
                    
                    # Buttons
                    for button in buttons:
                        if button.rect.collidepoint(event.pos):
                            if button.text == "Exit (L)":
                                self.running = False
                            elif button.text == "Play with keyboard (K)":
                                self.options["with"] = "Keyboard"
                                keyboard_game = KeyboardGame(self.options)
                                keyboard_game.start_game()
                            elif button.text == "Play with mouse":
                                self.options["with"] = "Mouse"
                                mouse_game = MouseGame(self.options)
                                mouse_game.start_game()
                
                # Hover effects
                if event.type == pygame.MOUSEMOTION:
                    for button in buttons:
                        button.check_hover(event.pos)
                    for button in radio_buttons:
                        button.check_hover(event.pos)
            
            # Front
            self.screen.fill(colors["amethyst"])
            
            #Title
            font = pygame.font.Font(None, 80)
            title = font.render("- Main menu -", 1, colors["dark_green"])
            titlepos = title.get_rect(centerx=self.screen.get_width()/2, centery=100)
            self.screen.blit(title, titlepos)
            
            # Buttons
            for button in buttons:
                button.draw(self.screen)
            
            #Radios buttons
            for button in radio_buttons:
                button.draw(self.screen)
            
            # Update the screen
            pygame.display.flip()
            
        pygame.quit()
    
    def initMenuScreen(self):
        """Init the main menu screen"""
        width = 1280
        height = 720
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Agarpyo - Main menu")
        return screen
