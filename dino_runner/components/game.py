from distutils.dep_util import newer_group
from pickle import TRUE
from pygame import mixer
from turtle import Screen
import pygame
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.pow_ups.pows_ups_manager import PowerUpManager


from dino_runner.utils.constants import BG, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEAD
from dino_runner.components.dinosaur import Dinosaur
#from dino_runner.assets.Other import soundtr

FONT_STYLE = 'freesansbold.ttf'


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Dinosaur()
        self.power_up_manager = PowerUpManager()
        self.obstacle_manager = ObstacleManager()
        self.playing = False
        self.time_to_show = Dinosaur()
        self.game_speed = 20
        self.running = False
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.ext_points = PowerUpManager()

        self.points = 0
        self.death_count = 0
        #self.play = PLAY
        #self.SOUND = pygame.mixer.Sound("")
        
    def execute(self):
        self.running = True
        self.Music = "soundtrack.ogg"
        mixer.init()
        pygame.mixer.music.load(self.Music)
        pygame.mixer.music.play(-1)
        while self.running:
            if not self.playing:
                self.show_menu()
        
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.playing = True
        self.game_speed = 20
        self.points = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.update_score()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player,self.ext_points)
        
#implementar un power ups

    def update_score(self):
        self.points += 1
        if self.points % 200 == 0:
            self.game_speed += 3
        
    def draw_score(self):
        font = pygame.font.SysFont('Troika',40,True,True)
        text = font.render(f"POINTS: {self.points}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (100, 50)
        self.screen.blit(text, text_rect)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.player.check_invicibility(self.screen)
        self.power_up_manager.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        self.player.draw(self.screen)
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.run()
                
    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            font = pygame.font.Font(FONT_STYLE,30)
            text = font.render("Press  any key to start", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)
        elif self.death_count > 0:
            font = pygame.font.Font(FONT_STYLE,70)
            text = font.render("\ \ \__GAME OVER___/ / /", True, (100,50,25))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)

            #MOSTRAR PUNTOS
            font = pygame.font.SysFont(FONT_STYLE,40,True,True)
            text = font.render(f"POINTS: {self.points}", True, (0,250,0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height-80)
            self.screen.blit(text, text_rect)

            #TIME_TO_SHOW
            #font = pygame.font.Font(FONT_STYLE,40)
            #text = font.render(f"POINTS PLUS: {self.ext_points}", True, (0,250,0))
            #text_rect = text.get_rect()
            #text_rect.center = (self.half_screen_width + 80, self.half_screen_height - 80)
            #self.screen.blit(text, text_rect)

            #MOSTRAR MUERTES
            font = pygame.font.Font(FONT_STYLE,40)
            text = font.render(f"Death's?: {self.death_count}", True, (255,0,0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height-120)
            self.screen.blit(text, text_rect)

            #INTENTAR DE NUEVO         False, (0,0,250)
            font = pygame.font.SysFont('Troika',35,True,True)
            text = font.render(" _*_*_*_*_PRESS ANY KEY FOR TRY AGAIN_*_*_*_*_ ", True, (0,0,250) )
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height+170)
            self.screen.blit(text, text_rect)


        self.screen.blit(DEAD, (half_screen_height+165, half_screen_width-200))

        pygame.display.update()
        self.handle_key_events_on_menu()