import pygame
from tank import Tank
from settings import *
from bullet import Bullet
from wall import Wall
import time


def menu():
    
    pygame.init()

    font = pygame.font.Font(None, 24)
    # Тут крч кнопки создаём
    button_start = pygame.Rect(380, 350, 150, 50) 
    button_exit = pygame.Rect(380, 450, 150, 50)
    # Тут текст для кнопок и его позиция, которая задаётся в центре самой кноки
    text_start = font.render('Start Game', True, (0, 137, 0))
    text_start_rect = text_start.get_rect(center=button_start.center)
    
    text_exit = font.render('Exit Game', True, (0, 137, 0))
    text_exit_rect = text_exit.get_rect(center=button_exit.center)

    while True:
        clock.tick(SPEED)
        screen.fill((0, 7, 0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.collidepoint(event.pos): #collidepoint чекает пересекаются ли объекты, в данном случае кнопка и курсор
                    main()
                elif button_exit.collidepoint(event.pos):
                    pygame.quit()
            elif event.type == pygame.QUIT:
                pygame.quit()
        pygame.draw.rect(screen, (200, 255, 0), button_start)
        pygame.draw.rect(screen, (200, 255, 0), button_exit)

        screen.blit(text_start, text_start_rect)
        screen.blit(text_exit, text_exit_rect)
        pygame.display.update()

def main():
    """Основная функция игры."""
    # Инициализация PyGame:
    #pygame.init()
    start_point = 11
    start_time = time.monotonic()
    tank = Tank()
    bullet_list = []
    wall_list = []
    wall_list.append(Wall(500, 500, 2, 'sprites/wall.png'))
    while True:
        
        clock.tick(SPEED)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # Получаем состояние всех клавиш
        keys = pygame.key.get_pressed()
        # Определяем направление движения на основе зажатых клавиш
        if keys[pygame.K_UP]:
            tank.move('UP', wall_list)
        elif keys[pygame.K_DOWN]:
            tank.move('DOWN', wall_list)
        elif keys[pygame.K_LEFT]:
            tank.move('LEFT', wall_list)
        elif keys[pygame.K_RIGHT]:
            tank.move('RIGHT', wall_list)
        if keys[pygame.K_SPACE]:
            if time.monotonic() - start_time >= 1:
                start_time = time.monotonic()
                bullet_list.append(Bullet(tank.x + 15, tank.y + 15, tank.old_direction))

        screen.fill((0, 0, 0))

        tank.draw(screen)
        
        for wall in wall_list:
            wall.draw(screen)
            if pygame.sprite.spritecollide(wall, bullet_list, False):
                wall.HP -= 1
                bullet_list.remove(bullet)
                if wall.HP <= 0:
                    wall_list.remove(wall)

        for bullet in bullet_list:
            bullet.draw(screen)
            bullet.move()
            if bullet.x > SCREEN_WIDTH or bullet.x < 0 or bullet.y > SCREEN_HEIGHT or bullet.y < 0:
                bullet_list.remove(bullet)
        pygame.display.update()


     

            

if __name__ == '__main__':
    menu()
