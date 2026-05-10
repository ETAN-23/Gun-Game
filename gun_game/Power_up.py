class Power_up:
    def __init__(self, type, color, position):
        self.type = type
        self.color = color
        self.position = position
        self.power = {1 : "health", 2:"speed", 3:"damage", 4:"reload"}
        
        if self.power[self.type] == "health":
            self.color = (0, 255, 0)
        elif self.power[self.type] == "speed":
            self.color = (255, 255, 0)
        elif self.power[self.type] == "damage":
            self.color = (245, 174, 0)
        elif self.power[self.type] == "reload":
            self.color = (0, 0, 255)

    def power_type(self, player):
        if self.power[self.type] == "health":
            player.health += 30
            self.color = (0, 255, 0)
        elif self.power[self.type] == "speed":
            player.speed += 2
            self.color = (255, 255, 0)
        elif self.power[self.type] == "damage":
            if player.weapon.powerup == 0:
                player.weapon.powerup = 2400
                player.weapon.damage += player.weapon.buff
        elif self.power[self.type] == "reload":
            player.weapon.ammo = player.weapon.a_count
            self.color = (0, 0, 255)