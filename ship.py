import pygame

class Ship:
    def __init__(self, para_game):

        self.screen = para_game.screen
        self.settings = para_game.settings
        self.screen_rect = para_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/para.png')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left >0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
            

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)