import pygame
from tank import Tank
from settings import *
from bullet import Bullet
from wall import Wall, Baza
from enemy import sEnemy
import time
import random


def menu():
    
    pygame.init()

    font = pygame.font.Font(None, 24)
    # Тут крч кнопки создаём
    button_start = pygame.Rect(380, 350, 150, 50) 
    button_exit = pygame.Rect(380, 450, 150, 50)
    # Тут текст для кнопок и его позиция, которая задаётся в центре самой кноки
    text_start = font.render('Начать игру', True, (0, 137, 0))
    text_start_rect = text_start.get_rect(center=button_start.center)
    
    text_exit = font.render('Выйти из игры', True, (0, 137, 0))
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

def menu_end():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 24)
    button_restart = pygame.Rect(380, 350, 150, 50)
    text_good_end = font.render(f'Рестарт', True, (0, 0, 0))
    text_good_end_rect = text_good_end.get_rect(center=button_restart.center)
    pygame.draw.rect(screen, (200, 255, 0), button_restart)
    screen.blit(text_good_end, text_good_end_rect)
    button_menu = pygame.Rect(380, 450, 150, 50)
    text_menu = font.render(f'Выйти в меню', True, (0, 0, 0))
    text_menu_rect = text_menu.get_rect(center=button_menu.center)
    pygame.draw.rect(screen, (200, 255, 0), button_menu)
    screen.blit(text_menu, text_menu_rect)

    pygame.display.update()
    while True:
        clock.tick(SPEED)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_restart.collidepoint(event.pos):
                    main()
                elif button_menu.collidepoint(event.pos):
                    menu()
            elif event.type == pygame.QUIT:
                pygame.quit()
def main():
    """Основная функция игры."""
    # Инициализация PyGame:
    #pygame.init()
    start_point = 11
    start_time = time.monotonic()
    tank = Tank()
    bullet_list = []
    bullet_list_mob = []
    wall_list = []
    count = 0
    baza = Baza(400, 800, 10, 'sprites/baza.jpg')

    for i in range(0, 900, 40):
        wall_list.append(Wall(i, 0, 100000, 'sprites/wall.png'))
        wall_list.append(Wall(i, 860, 100000, 'sprites/wall.png'))
        wall_list.append(Wall(0, i, 100000, 'sprites/wall.png'))
        wall_list.append(Wall(860, i, 100000, 'sprites/wall.png'))

    wall_list.append(Wall(500, 500, 1, 'sprites/wall.png'))
    wall_list.append(Wall(200, 500, 1, 'sprites/wall.png'))
    enemy_list = []
    enemy_list.append(sEnemy(100, 100))
    direction_list = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    font = pygame.font.SysFont('Arial', 32)

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
        baza.draw(screen)
        # блок отрисовки и движения врагов, а также их стрельбы и спавна новых врагов
        for enemy in enemy_list:
            if time.monotonic() - enemy.start_time_direction >= 4:
                enemy.start_time_direction = time.monotonic()
                enemy.move(random.choice(direction_list), wall_list)
            else:
                enemy.move(enemy.direction, wall_list)
            if time.monotonic() - enemy.start_time_bullet >= 5:
                 enemy.start_time_bullet = time.monotonic()
                 bullet_list_mob.append(Bullet(enemy.x + 15, enemy.y + 15, enemy.old_direction))
            if enemy.x > SCREEN_WIDTH or enemy.x < 0 or enemy.y > SCREEN_HEIGHT or enemy.y < 0:
                enemy_list.remove(enemy)
            if len(enemy_list) < 4 and random.random() < 0.02:
                    enemy_list.append(sEnemy(random.randint(100, 700), random.randint(60, 160)))
            enemy.draw(screen)
            damag = pygame.sprite.spritecollide(enemy, bullet_list, False)
            for bullet in damag:
                enemy.HP -= 1
                bullet_list.remove(bullet)
                if enemy.HP <= 0:
                    enemy_list.remove(enemy)
                    count += 1
                    if count == 1:
                        return menu_end()
        
        # блок проверки столкновений пуль врагов с танком, базой и всех пуль со стенами     
        damag = pygame.sprite.spritecollide(tank, bullet_list_mob, False)
        for bullet in damag:
            tank.HP -= 1
            bullet_list_mob.remove(bullet)
            if tank.HP <= 0:
                return menu_end()
        damag = pygame.sprite.spritecollide(baza, bullet_list_mob, False)
        for bullet in damag:
            baza.HP -= 1
            bullet_list_mob.remove(bullet)
            if baza.HP <= 0:
                return menu_end()
        for wall in wall_list:
            wall.draw(screen)
            bl = bullet_list + bullet_list_mob
            damag = pygame.sprite.spritecollide(wall, bl, False)
            for bullet in damag:
                wall.HP -= 1
                if bullet in bullet_list:
                    bullet_list.remove(bullet)
                else:
                    bullet_list_mob.remove(bullet)
                if wall.HP <= 0:
                    wall_list.remove(wall)

        # блок отрисовки и движения пуль
        bl = bullet_list + bullet_list_mob
        for bullet in bl:
            bullet.draw(screen)
            bullet.move()
            if bullet.x > SCREEN_WIDTH or bullet.x < 0 or bullet.y > SCREEN_HEIGHT or bullet.y < 0:
                if bullet in bullet_list:
                    bullet_list.remove(bullet)
                else:
                    bullet_list_mob.remove(bullet)
        bl = []
        text_count = font.render(f'Счёт: {count}', True, (0, 255, 0))
        screen.blit(text_count, (800, 0))
        pygame.display.update()


     


if __name__ == '__main__':
    menu()
