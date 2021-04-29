import sys
import pygame
from settings import Settings


class AlienInvasion:
    """Class for control resource and game"""

    def __init__(self):
        """Initializated game and create game resources"""
        pygame.init()
        self.settigs = Settings()
        self.screen = pygame.display.set_mode((self.settigs.screen_width, self.settigs.screen_heigth))
        pygame.display.set_caption("Alien Invasion")
        # Set screen background color


    def run_game(self):
        """Run main game cycle """
        while True:
            # Track events from keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # At each pass of cycle set background color
            self.screen.fill(self.settigs.bg_color)
            # Display last screen
            pygame.display.flip()


if __name__ == '__main__':
    # Create an instance
    ai = AlienInvasion()
    ai.run_game()
