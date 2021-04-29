import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class for control resource and game"""

    def __init__(self):
        """Initializated game and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))
        pygame.display.set_caption("Alien Invasion")
        # Imort ship from class Ship
        self.ship = Ship(self)
        # Set screen background color

    def run_game(self):
        """Run main game cycle """
        while True:
            # Track events from keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # At each pass of cycle set background color
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # Display last screen
            pygame.display.flip()


if __name__ == '__main__':
    # Create an instance
    ai = AlienInvasion()
    ai.run_game()
