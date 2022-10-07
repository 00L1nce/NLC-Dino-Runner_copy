import random
import pygame

from dino_runner.components.pow_ups.shield import Shield

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appers = 0

    def generate_power_ups(self, points):
        if len(self.power_ups) == 0:
            if self.when_appers == points:
                self.when_appers = random.randint(self.when_appers *200, self.when_appers *3)
                self.power_ups.append(Shield())


    def update(self, game_speed, points,  player):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                player.show_text = True
                player.type = power_up.type
                time_random = random.randint(25, 50)
                player.shield_time_up = power_up.start_time * (time_random * 1000)
                self.power_ups.remove(power_up)
            #pasa algo cuando se choca con el power up

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):  
        self.power_ups = []
        self.when_appers = random.randint(25, 50)