# Position - pygame rectangle

class Bullet:
    def __init__(self, speed, direction, position, damage, shot_by):
        self.speed = speed
        self.direction = direction
        self.position = position
        self.damage = damage
        self.shot_by = shot_by
    def update_position(self):
        # Update position based on speed and direction
        if self.direction == "R":
            self.position.x += self.speed
        if self.direction == "L":
            self.position.x -= self.speed
        if self.direction == "U":
            self.position.y -= self.speed 
        if self.direction == "D":
            self.position.y += self.speed                                                                                                                                                                                                                                                                                                        