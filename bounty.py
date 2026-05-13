import pygame
from tank import Tank
from settings import *
from bullet import Bullet
from wall import Wall
from enemy import sEnemy
from gen_level import generate_floor, build_room_walls, spawn_room_enemies, enter_room, move_tank_after_transition
import time
import random

class BountyEnemy():
    def __init__(self, x , y):
        self.x = x 
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
    def draw(self, screen):
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
