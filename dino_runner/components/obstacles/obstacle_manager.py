from operator import truediv
from pygame import mixer
from ast import Break
import random

import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactus_grande import Cactus_Grande
from dino_runner.components.obstacles.pajaro import Pajaro
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        mixer.init()
        self.dead_sound = pygame.mixer.Sound('douh.ogg') 

    def update(self, game):
        if len(self.obstacles) == 0:
            selec = random.randint(0, 2)
            #print(selec)
            if selec == 0: #genera 1
                small_cactus = Cactus(SMALL_CACTUS)
                self.obstacles.append(small_cactus)
            elif selec == 1: #genera 0
                large_cactus = Cactus_Grande(LARGE_CACTUS)
                self.obstacles.append(large_cactus)
            elif selec == 2:
                bird = Pajaro(BIRD)
                self.obstacles.append(bird)
            #elif selec == 2:
                

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    self.dead_sound.play()
                    pygame.time.delay(1000)
                    game.playing = False
                    game.death_count += 1
                    #pygame.time.delay(5000)
                else:
                    self.obstacles.remove(obstacle)
            
            Break
            #pygame.time.delay(5000)
            #self.dead_sound.stop()


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []

#Clase 2 : Obstacles
#Clase 2 : Tarea