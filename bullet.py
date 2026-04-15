# Снаряд
import pygame

class Bullet:
    def __init__(self, x, y, derection):
        self.x = x
        self.y = y
        self.speed = 10
        self.derection = derection
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 10, 10))
    def move(self):
        if self.derection == 'UP':
            self.y -= self.speed
        elif self.derection == 'DOWN':
            self.y += self.speed
        elif self.derection == 'LEFT':  
            self.x -= self.speed
        elif self.derection == 'RIGHT':
            self.x += self.speed
    
    def __str__(self):
        return f'({self.x}, {self.y})'
