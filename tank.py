# Класс танка
import pygame 
from bullet import Bullet

class Tank:
    image = 'sprites/player.png'
    def __init__(self):
        self.x = 350
        self.y = 850
        self.speed = 7
        self.image = pygame.image.load(self.image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.image_rotated = self.image
        self.old_direction = 'UP'
        self.angle = 0
    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, 40, 40)
        screen.blit(self.image_rotated, rect)
    def move(self, direction):
        if direction == 'UP':
            self.y -= self.speed
            if self.old_direction != direction:
                self.angle = 0
                self.image_rotated = pygame.transform.rotate(self.image, self.angle)
                self.old_direction = direction
        if direction == 'DOWN':
            self.y += self.speed
            if self.old_direction != direction:
                self.angle = 180
                self.image_rotated = pygame.transform.rotate(self.image, self.angle)
                self.old_direction = direction
        if direction == 'LEFT':
            self.x -= self.speed
            if self.old_direction != direction:
                self.angle = 90
                self.image_rotated = pygame.transform.rotate(self.image, self.angle)
                self.old_direction = direction
        if direction == 'RIGHT':
            self.x += self.speed
            if self.old_direction != direction:
                self.angle = 270
                self.image_rotated = pygame.transform.rotate(self.image, self.angle)
                self.old_direction = direction
        def shot(self):
            pass