# Все константы
import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 900
GRID_SIZE = 20

# Цвет фона:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Скорость игры:
SPEED = 20

ROOM_GRID_WIDTH = 3 # ширина сетки комнат 
ROOM_GRID_HEIGHT = 3  # высота сетки комнат 
ROOM_MIN_LENGTH = 2  # минимальная длина пути от старта до выхода 
ROOM_MAX_LENGTH = 2  # максимальная длина пути от старта до выхода 
DOOR_START = 380  # начало открытой части стены
DOOR_END = 520  # конец открытой части стены

ROOM_STEPS = {  # шаги по сетке комнат для генерации пути
    'UP': (0, -1),
    'DOWN': (0, 1),
    'LEFT': (-1, 0),
    'RIGHT': (1, 0),
}

ROOM_OPPOSITE = {  # противоположные направления для связки дверей между комнатами
    'UP': 'DOWN',
    'DOWN': 'UP',
    'LEFT': 'RIGHT',
    'RIGHT': 'LEFT',
}

ROOM_ENTRY_OFFSET = 100  # отступ при появлении игрока из двери
ROOM_EXIT_OFFSET = 100  # отступ при выходе из комнаты

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Танчики')

# Настройка времени:
clock = pygame.time.Clock()