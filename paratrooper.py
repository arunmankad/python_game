import sys
import pygame

from settings import Settings
from ship import Ship

class Paratrooper:
    """Overall class to manage game assets and behaviou"""

    def __init__(self):
        """Initialzie the game create the game resources"""

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.ship = Ship(self)
        pygame.display.set_caption("Paratrooper")

        # self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game """
        while True:
            # Watch for keyboard and mouse events
            self._check_events()
            self._update_events()

            
    
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
    
    def _update_events(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    para = Paratrooper()
    para.run_game()