# name, ammo, firerate, bullet speed, damage
class Gun:
    def __init__(self, name, ammo, firerate, bullet_V, damage, ready2_fire, cooldown, a_count, sound_effects, powerup, buff):
        self.name = str(name)
        self.ammo = ammo
        self.firerate = firerate
        self.bullet_V = bullet_V
        self.damage = damage
        self.ready2_fire = ready2_fire
        self.reload = 0    
        self.cooldown = cooldown
        self.a_count = a_count
        self.sound_effects = sound_effects
        self.powerup = powerup
        self.buff = buff
    def power_track(self):
        # if power up is active, do something
        if self.powerup > 1:
            self.powerup-=1
        elif self.powerup == 1:
            self.damage -= self.buff
            self.powerup-=1
        else:
            pass
    def fire_countdown(self):
        self.ready2_fire -= self.firerate
    
    def reset_ready2_fire(self, ready2_fire):
        self.ready2_fire = ready2_fire
    
    def is_ready2_fire(self):
        if self.ready2_fire <= 0:
            return True
        return False
    
    def shoot(self, direction):
        print(self.name + " shoots " + str(direction))
    def reload_countdown(self):
        if self.reload > 0:
            self.reload-= 1
    def reset_reload(self, reload):
        self.reload = reload