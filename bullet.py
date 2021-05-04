import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for controlling bullets fired by ship"""

    def __init__(self, ai_game):
        """Create object of bullet in current ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create bullet in position (0,0) and assigning the right position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Position of bullet save in float format
        self.y = float(self.rect.y)

    def update(self):
        """moving bullet in top of the screen"""
        # update position of bullet in float format
        self.y -= self.settings.bullet_speed
        # Update position of rectangle
        self.rect.y = self.y

    def draw_bullet(self):
        """Show bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
