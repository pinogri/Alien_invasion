import sys
import pygame


class AlienInvasion:
    """Class for control resource and game"""

    def __init__(self):
        """Initializated game and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        # Set screen background color
        self.bg_color = (230, 230, 230)


    def run_game(self):
        """Run main game cycle """
        while True:
            # Track events from keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # At each pass of cycle set background color
            self.screen.fill(self.bg_color)
            # Display last screen
            pygame.display.flip()


if __name__ == '__main__':
    # Create an instance
    ai = AlienInvasion()
    ai.run_game()
