import pygame

class Ship:
    def __init__(self, para_game):

        self.screen = para_game.screen
        self.screen_rect = para_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/para.png')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)