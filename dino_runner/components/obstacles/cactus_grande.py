import random
from pygame.sprite import Sprite

from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus_Grande(Obstacle):

    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300
