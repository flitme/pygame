import pygame 
from bullet import Bullet
from settings import *

class sEnemy:
    image = 'sprites/enemy.png'
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.image = pygame.image.load(self.image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.image_rotated = self.image
        self.old_direction = 'UP'
        self.direction = 'RIGHT'
        self.angle = 0
        self.rect = self.image.get_rect()
    def draw(self, screen):
        self.rect  = pygame.Rect(self.x, self.y, 40, 40)
        screen.blit(self.image_rotated, self.rect)
    def move(self, direction, wall_list):
        self.direction = direction
        if self.direction == 'UP':
            self.y -= self.speed
            if self.old_direction != direction:
                self.angle = 0
                self.image_rotated = pygame.transform.rotate(self.image, self.angle)
                self.old_direction = direction
            index = self.rect.collidelist(wall_list)
            if index != -1:
                wall = wall_list[index]
                self.y += (20 + 10)
        if self.direction == 'DOWN':
            self.y += self.speed
            if self.old_direction != direction:
                self.angle = 180
                self.image_rotated = pygame.transform.rotate(self.image, self.angle)
                self.old_direction = direction
            index = self.rect.collidelist(wall_list)
            if index != -1:
                wall = wall_list[index]
                self.y -= (20 + 10)
        if self.direction == 'LEFT':
            self.x -= self.speed
            if self.old_direction != direction:
                self.angle = 90
                self.image_rotated = pygame.transform.rotate(self.image, self.angle)
                self.old_direction = direction
            index = self.rect.collidelist(wall_list)
            if index != -1:
                wall = wall_list[index]
                self.x += (20 + 10)
        if self.direction == 'RIGHT':
            self.x += self.speed
            if self.old_direction != direction:
                self.angle = 270
                self.image_rotated = pygame.transform.rotate(self.image, self.angle)
                self.old_direction = direction
            index = self.rect.collidelist(wall_list)
            if index != -1:
                wall = wall_list[index]
                self.x -= (20 + 10)