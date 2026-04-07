import pygame
from tank import Tank
from settings import *

def main():
    """Основная функция игры."""
    # Инициализация PyGame:
    pygame.init()

    tank = Tank()

    while True:
        clock.tick(SPEED)

        tank.draw(screen)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Получаем состояние всех клавиш
        keys = pygame.key.get_pressed()
        # Определяем направление движения на основе зажатых клавиш
        if keys[pygame.K_UP]:
            tank.move('UP')
        elif keys[pygame.K_DOWN]:
            tank.move('DOWN')
        elif keys[pygame.K_LEFT]:
            tank.move('LEFT')
        elif keys[pygame.K_RIGHT]:
            tank.move('RIGHT')

        screen.fill((0, 0, 0))
        tank.draw(screen)

        pygame.display.update()

if __name__ == '__main__':
    main()
