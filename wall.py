import pygame

class Wall:
    def __init__(self, x, y, HP, image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.HP = HP
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(self.x, self.y, 40, 40)
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Baza(Wall):
    def __init__(self, x, y, HP, image):
        super().__init__(x, y, HP, image)

class Exit(Wall):
    def __init__(self, x, y, HP, image):
        super().__init__(x, y, HP, image)