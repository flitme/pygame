import pygame

class Wall:
    def __init__(self, x, y, HP, image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.HP = HP
        self.rect = self.image.get_rect()
    def draw(self, screen):
        self.rect = pygame.Rect(self.x, self.y, 40, 40)
        screen.blit(self.image, self.rect)
    