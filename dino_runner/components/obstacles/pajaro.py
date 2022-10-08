import random
from pygame.sprite import Sprite

from dino_runner.components.obstacles.obstacle import Obstacle


class Pajaro(Obstacle):

    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = random.randint(230, 300)
