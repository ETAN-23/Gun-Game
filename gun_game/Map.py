# name, obstacles, screen width, screen height, background color, obstacle color
class Map:
    def __init__(self, name, obstacles, projectiles, screen_width, screen_height, bg_color, obstacle_color, power_ups):
        """Create a Map container.

        Parameters
        - name: str - map name
        - obstacle: None, a single obstacle, or an iterable of obstacles (stored as list)
        - screen_width: int
        - screen_height: int
        - bg_color: color value (any type the caller uses, e.g., (r,g,b))
        - obstacle_color: color value for drawing obstacles

        Obstacles are stored as provided; drawing/interpretation is left to the game code.
        """
        self.name = str(name)
        self.obstacles = list(obstacles)
        self.projectiles = list(projectiles)
        self.screen_width = int(screen_width)
        self.screen_height = int(screen_height)
        self.bg_color = bg_color
        self.obstacle_color = obstacle_color
        self.power_ups = power_ups