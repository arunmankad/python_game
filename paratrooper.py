import sys
import pygame

class Paratrooper:
    """Overall class to manage game assets and behaviou"""

    def __init__(self):
        """Initialzie the game create the game resources"""

        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))

        pygame.display.set_caption("Paratrooper")

        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game """
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            # Make the most recently drawn screen visible.
            pygame.display.flip()
if __name__ == '__main__':
    # Make a game instance, and run the game.
    para = Paratrooper()
    para.run_game()