import pygame 
from bullet import Bullet
from settings import *
from tank import Tank

class sEnemy(Tank):
    image = 'sprites/enemy.png'
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.image = pygame.image.load(self.image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.image_rotated = self.image
        self.old_direction = 'UP'
        self.start_time_direction = 1
        self.start_time_bullet = 1
        self.angle = 0
        self.rect = self.image.get_rect()
        self.HP = 2

class BossEnemy(Tank):
    image = 'sprites/enemy.png'
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 3
        self.image = pygame.image.load(self.image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.image_rotated = self.image
        self.old_direction = 'UP'
        self.start_time_direction = 1
        self.start_time_bullet = 1
        self.angle = 0
        self.rect = self.image.get_rect()
        self.HP = 10