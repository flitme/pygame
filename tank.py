# Класс танка
import pygame 
from bullet import Bullet
from settings import *

class Tank:
    image = 'sprites/player.png'
    def __init__(self):
        self.x = 350
        self.y = 800
        self.speed = 7
        self.image = pygame.image.load(self.image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.image_rotated = self.image
        self.old_direction = 'UP'
        self.angle = 0
        self.HP = 2
        self.rect = self.image.get_rect()
    def draw(self, screen):
        self.rect  = pygame.Rect(self.x, self.y, 40, 40)
        screen.blit(self.image_rotated, self.rect)
    def move(self, direction, wall_list):
        if direction == 'UP':
            if self.old_direction != direction:
                self.angle = 0
                self.image_rotated = pygame.transform.rotate(self.image, self.angle)
                self.old_direction = direction
            index = self.rect.collidelist(wall_list)
            if index != -1:
                wall = wall_list[index]
                self.y += (SPEED + 7)
            self.y -= self.speed
        if direction == 'DOWN':
            if self.old_direction != direction:
                self.angle = 180
                self.image_rotated = pygame.transform.rotate(self.image, self.angle)
                self.old_direction = direction
            index = self.rect.collidelist(wall_list)
            if index != -1:
                wall = wall_list[index]
                self.y -= (SPEED + 7)
            self.y += self.speed
        if direction == 'LEFT':
            if self.old_direction != direction:
                self.angle = 90
                self.image_rotated = pygame.transform.rotate(self.image, self.angle)
                self.old_direction = direction
            index = self.rect.collidelist(wall_list)
            if index != -1:
                wall = wall_list[index]
                self.x += (SPEED + 7)
            self.x -= self.speed
        if direction == 'RIGHT':
            if self.old_direction != direction:
                self.angle = 270
                self.image_rotated = pygame.transform.rotate(self.image, self.angle)
                self.old_direction = direction
            index = self.rect.collidelist(wall_list)
            if index != -1:
                wall = wall_list[index]
                self.x -= (SPEED + 7)
            self.x += self.speed

