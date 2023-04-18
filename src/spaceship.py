
class Spaceship:
    def __init__(self, x, y, speed, health):
        self.x = x
        self.y = y
        self.base_speed = speed
        self.health = health
        self.speed = speed
        self.current_shot_cooldown = 0
        self.shot_cooldown = 200
        self.damage_immunity = 0

    def hit(self, damage):
        self.health -= damage
        self.damage_immunity = 20

    def damage_immunity_update(self):
        if self.damage_immunity > 0:
            self.damage_immunity -= 1

