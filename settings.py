# Все константы
import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 900
GRID_SIZE = 20

# Цвет фона:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Скорость игры:
SPEED = 10

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Танчики')

# Настройка времени:
clock = pygame.time.Clock()