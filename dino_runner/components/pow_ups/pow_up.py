from pygame.sprite import Sprite
import random
from dino_runner.utils.constants import SCREEN_WIDTH


class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image == image
        self.rect = self.image.get_rect()
        self.type = type
        self.rect.y = random.randint(100, 150)
        self.rect.x = SCREEN_WIDTH + random.randint(800,1000)
        self.start_time = 0
        
    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            power_ups.pop()

    #inver¿stigar <-self.asjfjahhdg

    def draw(self, screen):
        screen.blit(self.image, self.rect)