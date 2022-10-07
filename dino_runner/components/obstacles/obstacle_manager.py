from ast import Break
import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                small_cactus = Cactus(SMALL_CACTUS)
                self.obstacles.append(small_cactus)
            elif random.randint(0, 2) == 0:
                large_cactus = Cactus(LARGE_CACTUS)
                self.obstacles.append(large_cactus) 

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacle)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                    #cosa para cuando pierda
                else:
                    self.obstacles.remove(obstacle)
            #Break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacle = []

#Clase 2 : Obstacles
#Clase 2 : Tarea