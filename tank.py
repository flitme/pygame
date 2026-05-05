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
        d = {
            'UP': (0, -self.speed, 0),
            'DOWN': (0, self.speed, 180),
            'LEFT': (-self.speed, 0, 90),
            'RIGHT': (self.speed, 0, 270)
        }
        if self.old_direction != direction:
            self.angle = d[direction][2]
            self.image_rotated = pygame.transform.rotate(self.image, self.angle)
            self.old_direction = direction

        new_x = self.x + d[direction][0]
        new_y = self.y + d[direction][1]

        old_x, old_y = self.x, self.y
        
        self.x, self.y = new_x, new_y
        self.rect.topleft = (self.x, self.y)

        if self.rect.collidelist(wall_list) != -1:
            self.x, self.y = old_x, old_y
            self.rect.topleft = (self.x, self.y)

        


# Тут пока что останется старый функционал 
        # if direction == 'UP':
        #     if self.old_direction != direction:
        #         self.angle = 0
        #         self.image_rotated = pygame.transform.rotate(self.image, self.angle)
        #         self.old_direction = direction
        #     index = self.rect.collidelist(wall_list)
        #     if index != -1:
        #         wall = wall_list[index]
        #         self.y += (SPEED + 7)
        #     self.y -= self.speed
        # if direction == 'DOWN':
        #     if self.old_direction != direction:
        #         self.angle = 180
        #         self.image_rotated = pygame.transform.rotate(self.image, self.angle)
        #         self.old_direction = direction
        #     index = self.rect.collidelist(wall_list)
        #     if index != -1:
        #         wall = wall_list[index]
        #         self.y -= (SPEED + 7)
        #     self.y += self.speed
        # if direction == 'LEFT':
        #     if self.old_direction != direction:
        #         self.angle = 90
        #         self.image_rotated = pygame.transform.rotate(self.image, self.angle)
        #         self.old_direction = direction
        #     index = self.rect.collidelist(wall_list)
        #     if index != -1:
        #         wall = wall_list[index]
        #         self.x += (SPEED + 7)
        #     self.x -= self.speed
        # if direction == 'RIGHT':
        #     if self.old_direction != direction:
        #         self.angle = 270
        #         self.image_rotated = pygame.transform.rotate(self.image, self.angle)
        #         self.old_direction = direction
        #     index = self.rect.collidelist(wall_list)
        #     if index != -1:
        #         wall = wall_list[index]
        #         self.x -= (SPEED + 7)
        #     self.x += self.speed

