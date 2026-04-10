import pygame
from tank import Tank
from settings import *
from bullet import Bullet

def main():
    """Основная функция игры."""
    # Инициализация PyGame:
    pygame.init()

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
            bullet_list.append(Bullet(tank.x + 15, tank.y + 15))

        screen.fill((0, 0, 0))
        tank.draw(screen)
        for bullet in bullet_list:
            bullet.draw(screen)
            bullet.move()
            print((bullet))
        pygame.display.update()

if __name__ == '__main__':
    main()
