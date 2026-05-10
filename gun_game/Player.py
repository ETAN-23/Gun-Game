# Player
# Skin, Position, Weapon, Health, Direction
# Skin - img file
# Position - PyGame rectangle
# Weapon - custom Gun object
# Health - integer
# Direction - "U", "D", "L", "R"

class Player:
    def __init__(self, skin, position, weapon, health, direction, speed):
        self.skin = skin
        self.position = position
        self.weapon = weapon
        self.health = health
        self.direction = direction
        self.speed = speed 
    def decrease_health(self, amount):
        self.health -= amount
    
    def update_position(self, dx, dy):
        self.position.x += dx
        self.position.y += dy
    
    def update_direction(self, new_direction):
        self.direction = new_direction

    def shoot(self):
        self.weapon.shoot()