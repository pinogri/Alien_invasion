import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class for control resource and game"""

    def __init__(self):
        """Initialized game and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))
        pygame.display.set_caption("Alien Invasion")
        # Import ship from class Ship
        self.ship = Ship(self)
        # Set screen background color

    def run_game(self):
        """Run main game cycle """
        while True:
            # Track events from keyboard and mouse
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

    # At each pass of cycle set background color
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Display last screen
        pygame.display.flip()


if __name__ == '__main__':
    # Create an instance
    ai = AlienInvasion()
    ai.run_game()
