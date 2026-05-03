import pygame
from tank import Tank
from settings import *
from bullet import Bullet
from wall import Wall
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
    bullet_list_mob = []
    wall_list = []
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
            if len(enemy_list) < 4 and random.random() < 0.01:
                    enemy_list.append(sEnemy(random.randint(100, 700), random.randint(60, 160)))
            enemy.draw(screen)
            damag = pygame.sprite.spritecollide(enemy, bullet_list, False)
            for bullet in damag:
                enemy.HP -= 1
                bullet_list.remove(bullet)
                if enemy.HP <= 0:
                    enemy_list.remove(enemy)
            damag = pygame.sprite.spritecollide(tank, bullet_list_mob, False)
            for bullet in damag:
                tank.HP -= 1
                bullet_list_mob.remove(bullet)
                if tank.HP <= 0:
                    print('Game Over')

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

        

  

        pygame.display.update()


     

        
if __name__ == '__main__':
    menu()
