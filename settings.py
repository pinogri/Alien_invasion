class Settings():
    """Class for store all game settings"""

    def __init__(self):
        """Initialized game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_heigth = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

