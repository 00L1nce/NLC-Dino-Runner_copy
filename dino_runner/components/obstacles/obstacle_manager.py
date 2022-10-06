from ast import Break
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS
class ObstacleManager:
    def __init__(self):
        self.obstacle = []

    def update(self, game):
        if len(self.obstacle) == 0:
            small_cactus = Cactus(SMALL_CACTUS)
            self.obstacle.append(small_cactus)

#tarea: imlementar cactus grandes
        for obstacle in self.obstacle:
            obstacle.update(game.game_speed, self.obstacle)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                #cosa para cuando pierda
                Break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacle = []

#Clase 2 : Obstacles
#Clase 2 : Tarea