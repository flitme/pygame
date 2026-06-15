import pygame
from tank import Tank
from settings import *
from bullet import Bullet
from wall import Wall
from enemy import sEnemy, BossEnemy
from bounty import BountyEnemy, BountyBoss
from gen_level import generate_floor, build_room_walls, spawn_room_enemies, enter_room, move_tank_after_transition
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
    start_time = time.monotonic()
    tank = Tank()
    bullet_list = []
    bullet_list_mob = []
    bounty_list = []
    count = 0
    floor_index = 1
    rooms, current_room = generate_floor(floor_index)
    wall_list, enemy_list = enter_room(current_room, rooms, floor_index)
    direction_list = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    font = pygame.font.SysFont('Arial', 32)
    bc = 0
    while True:
        clock.tick(SPEED)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # Получаем состояние всех клавиш
        keys = pygame.key.get_pressed()
        # Определяем направление движения на основе зажатых клавиш
        if keys[pygame.K_UP]:
            tank.move('UP', wall_list, enemy_list)
        elif keys[pygame.K_DOWN]:
            tank.move('DOWN', wall_list, enemy_list)
        elif keys[pygame.K_LEFT]:
            tank.move('LEFT', wall_list, enemy_list)
        elif keys[pygame.K_RIGHT]:
            tank.move('RIGHT', wall_list, enemy_list)
        if keys[pygame.K_SPACE]:
            if time.monotonic() - start_time >= 1:
                start_time = time.monotonic()
                bullet_list.append(Bullet(tank.x + 15, tank.y + 15, tank.old_direction))

        current_room_data = rooms[current_room]
        if not current_room_data['cleared'] and len(enemy_list) == 0:
            current_room_data['cleared'] = True
            wall_list = build_room_walls(current_room_data)

        if current_room_data['cleared']:
            if tank.x < 0 and 'LEFT' in current_room_data['doors']:
                next_room = (current_room[0] - 1, current_room[1])
                if next_room in rooms:
                    current_room = next_room
                    move_tank_after_transition(tank, 'LEFT')
                    wall_list, enemy_list = enter_room(current_room, rooms, floor_index)
                    bullet_list = []
                    bullet_list_mob = []
                    bounty_list = []
                elif current_room_data['exit']:
                    floor_index += 1
                    rooms, current_room = generate_floor(floor_index)
                    tank.x = 350
                    tank.y = 800
                    tank.rect.topleft = (tank.x, tank.y)
                    bullet_list = []
                    bullet_list_mob = []
                    bounty_list = []
                    wall_list, enemy_list = enter_room(current_room, rooms, floor_index)
            elif tank.x > SCREEN_WIDTH - 40 and ('RIGHT' in current_room_data['doors'] or current_room_data['exit']):
                next_room = (current_room[0] + 1, current_room[1])
                if next_room in rooms:
                    current_room = next_room
                    move_tank_after_transition(tank, 'RIGHT')
                    wall_list, enemy_list = enter_room(current_room, rooms, floor_index)
                    bullet_list = []
                    bullet_list_mob = []
                    bounty_list = []
                elif current_room_data['exit']:
                    floor_index += 1
                    rooms, current_room = generate_floor(floor_index)
                    tank.x = 350
                    tank.y = 800
                    tank.rect.topleft = (tank.x, tank.y)
                    bullet_list = []
                    bullet_list_mob = []
                    bounty_list = []
                    wall_list, enemy_list = enter_room(current_room, rooms, floor_index)
            elif tank.y < 0 and 'UP' in current_room_data['doors']:
                next_room = (current_room[0], current_room[1] - 1)
                if next_room in rooms:
                    current_room = next_room
                    move_tank_after_transition(tank, 'UP')
                    wall_list, enemy_list = enter_room(current_room, rooms, floor_index)
                    bullet_list = []
                    bullet_list_mob = []
                    bounty_list = []
                elif current_room_data['exit']:
                    floor_index += 1
                    rooms, current_room = generate_floor(floor_index)
                    tank.x = 350
                    tank.y = 800
                    tank.rect.topleft = (tank.x, tank.y)
                    bullet_list = []
                    bullet_list_mob = []
                    bounty_list = []
                    wall_list, enemy_list = enter_room(current_room, rooms, floor_index)
            elif tank.y > SCREEN_HEIGHT - 40 and 'DOWN' in current_room_data['doors']:
                next_room = (current_room[0], current_room[1] + 1)
                if next_room in rooms:
                    current_room = next_room
                    move_tank_after_transition(tank, 'DOWN')
                    wall_list, enemy_list = enter_room(current_room, rooms, floor_index)
                    bullet_list = []
                    bullet_list_mob = []
                    bounty_list = []
                elif current_room_data['exit']:
                    floor_index += 1
                    rooms, current_room = generate_floor(floor_index)
                    tank.x = 350
                    tank.y = 800
                    tank.rect.topleft = (tank.x, tank.y)
                    bullet_list = []
                    bullet_list_mob = []
                    bounty_list = []
                    wall_list, enemy_list = enter_room(current_room, rooms, floor_index)
        

        tank.draw(screen)

        # блок отрисовки и движения врагов, а также их стрельбы и спавна новых врагов
        for enemy in enemy_list:
            if time.monotonic() - enemy.start_time_direction >= 4:
                enemy.start_time_direction = time.monotonic()
                el = enemy_list.copy() + [tank]
                el.remove(enemy)
                enemy.move(random.choice(direction_list), wall_list, el)
            else:
                el = enemy_list.copy() + [tank]
                el.remove(enemy)
                enemy.move(enemy.old_direction, wall_list, el)
            if time.monotonic() - enemy.start_time_bullet >= 5:
                 enemy.start_time_bullet = time.monotonic()
                 bullet_list_mob.append(Bullet(enemy.x + 15, enemy.y + 15, enemy.old_direction))
            if enemy.x > SCREEN_WIDTH or enemy.x < 0 or enemy.y > SCREEN_HEIGHT or enemy.y < 0:
                enemy_list.remove(enemy)
            enemy.draw(screen)
            damag = pygame.sprite.spritecollide(enemy, bullet_list, False)
            for bullet in damag:
                enemy.HP -= 1
                bullet_list.remove(bullet)
                if enemy.HP <= 0:
                    if isinstance(enemy, BossEnemy):
                        bounty_list.append(BountyBoss(enemy.x + 15, enemy.y + 15))
                    else:
                        bounty_list.append(BountyEnemy(enemy.x + 15, enemy.y + 15))
                    enemy_list.remove(enemy)
                    count += 1
        for bounty in bounty_list:
            bounty.draw(screen)
            #print(type(bounty))
            if bounty.rect.colliderect(tank.rect):
                bounty_list.remove(bounty)
                bc += bounty.chip
        
        # блок проверки столкновений пуль врагов с танком и всех пуль со стенами     
        damag = pygame.sprite.spritecollide(tank, bullet_list_mob, False)
        for bullet in damag:
            tank.HP -= 1
            bullet_list_mob.remove(bullet)
            if tank.HP <= 0:
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

        text_count = font.render(f'Уничтожено: {count}', False, (0, 255, 0))
        text_floor = font.render(f'Этаж: {floor_index}', True, (0, 255, 0))
        text_bc = font.render(f'Деньги: {bc}', True, (0, 255, 0))
        text_HP = font.render(f'HP: {tank.HP}', True, (0, 255, 0))
        screen.blit(text_count, (650, 0))
        screen.blit(text_floor, (650, 32))
        screen.blit(text_bc, (650, 64))
        screen.blit(text_HP, (650, 96))
        pygame.display.update()

        screen.fill((0, 0, 0))
     
if __name__ == '__main__':
    menu()
