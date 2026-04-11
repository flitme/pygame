import pygame
from tank import Tank
from settings import *
from bullet import Bullet
from saport import *
import time

def main():
    """Основная функция игры."""
    # Инициализация PyGame:
    pygame.init()
    start_point = 11
    start_time = time.monotonic()
    tank = Tank()
    bullet_list = []
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
        if keys[pygame.K_SPACE]:
            if time.monotonic() - start_time >= 1:
                start_time = time.monotonic()
                bullet_list.append(Bullet(tank.x + 15, tank.y + 15, tank.old_direction))

        screen.fill((0, 0, 0))
        tank.draw(screen)
        for bullet in bullet_list:
            bullet.draw(screen)
            bullet.move()
            if bullet.x > SCREEN_WIDTH or bullet.x < 0 or bullet.y > SCREEN_HEIGHT or bullet.y < 0:
                bullet_list.remove(bullet)
        pygame.display.update()

if __name__ == '__main__':
    main()
