# Снаряд
import pygame

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 10, 10))
    def move(self):
        self.y -= self.speed
    
    def __str__(self):
        return f'({self.x}, {self.y})'