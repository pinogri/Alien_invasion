import pygame


class Ship():
    """Ship control class"""

    def __init__(self, ai_game):
        """Initialize ship and set the first position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Download image of ship and get rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Each new ship initialize at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship in current position"""
        self.screen.blit(self.image, self.rect)
