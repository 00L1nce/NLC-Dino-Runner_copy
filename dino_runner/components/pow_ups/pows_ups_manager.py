import random
from pygame import mixer
import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from dino_runner.components.pow_ups.shield import Shield
from dino_runner.components.pow_ups.hammer import Hammer

FONT_STYLE = 'freesansbold.ttf'

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appers = 0
        self.half_screen_height = SCREEN_HEIGHT // 2
        self.half_screen_width = SCREEN_WIDTH // 2
        self.ext_points = 0
        mixer.init()
        self.chad_sound = pygame.mixer.Sound('chad.ogg') 

    def generate_power_ups(self, points):
        if len(self.power_ups) >= 0:
            pow_sel = random.randint(0, 1)
            if self.when_appers == points and pow_sel == 0:
                self.when_appers = random.randint(self.when_appers * 100, self.when_appers * 500)
                self.power_ups.append(Shield())
            elif self.when_appers == points and pow_sel == 1:
                self.when_appers = random.randint(self.when_appers * 200, self.when_appers * 300)
                self.power_ups.append(Hammer())


    def update(self, points, game_speed, player, ext_points):
        self.generate_power_ups(points)
        
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            #pow_sel = random.randint(0, 2)
            if player.dino_rect.colliderect(power_up.rect):
                self.chad_sound.play()
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                player.show_text = True
                player.type = power_up.type
                time_random = 10
                player.shield_time_up = power_up.start_time + (time_random * 1000)
                
                self.power_ups.remove(power_up)
                self.ext_points += 1

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):  
        self.power_ups = []
        self.when_appers = random.randint(100, 300)