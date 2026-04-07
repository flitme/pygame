# Класс танка
import pygame 

class Tank:
    def __init__(self):
        self.x = 200
        self.y = 400
        self.image = pygame.image.load('sprites/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, 40, 40)
        screen.blit(self.image, rect)