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

def next_floor(floor_index, rooms, current_room, tank, bullet_list, bullet_list_mob, bounty_list, wall_list, enemy_list):
    floor_index += 1
    rooms, current_room = generate_floor(floor_index)
    tank.x = 350
    tank.y = 800
    tank.rect.topleft = (tank.x, tank.y)
    bullet_list = []
    bullet_list_mob = []
    bounty_list = []
    wall_list, enemy_list = enter_room(current_room, rooms, floor_index, tank)
    return floor_index, rooms, current_room, tank, bullet_list, bullet_list_mob, bounty_list, wall_list, enemy_list

def enter(next_room, current_room, tank, wall_list, enemy_list, rooms, floor_index, bullet_list, bullet_list_mob, bounty_list, direction):
    current_room = next_room
    move_tank_after_transition(tank, direction)
    wall_list, enemy_list = enter_room(current_room, rooms, floor_index, tank)
    bullet_list = []
    bullet_list_mob = []
    bounty_list = []
    return current_room, tank, wall_list, enemy_list, bullet_list, bullet_list_mob, bounty_list


def init_joystick():
    pygame.joystick.init()  # включаем поддержку джойстиков в Pygame
    if pygame.joystick.get_count() == 0:
        return None  # если геймпад не найден, возвращаем None и не ломаем игру

    joystick = pygame.joystick.Joystick(0)  # берём первый подключённый геймпад
    joystick.init()  # активируем его для чтения осей и кнопок
    return joystick  # возвращаем объект геймпада


def get_joystick_direction(joystick, deadzone=0.4):
    if joystick is None:
        return None  # если геймпада нет, направление не читаем

    if joystick.get_numaxes() > 0: # ось X левого стика
        axis_x = joystick.get_axis(0) 
    else: 
        axis_x = 0  

    if joystick.get_numaxes() > 1: # ось Y левого стика
        axis_y = joystick.get_axis(1)  
    else:
        axis_y = 0  

    if abs(axis_x) > abs(axis_y):  # выбираем более сильное отклонение по X
        if axis_x < -deadzone:
            return 'LEFT'  # стик сильно влево
        if axis_x > deadzone:
            return 'RIGHT'  # стик сильно вправо
    else:
        # если по вертикали отклонение сильнее, двигаем по Y
        if axis_y < -deadzone:
            return 'UP'  # стик вверх
        if axis_y > deadzone:
            return 'DOWN'  # стик вниз

    return None  # если стик почти по центру, движение не задаём


def joystick_shoot_pressed(joystick):
    if joystick is None:
        return False  # без геймпада кнопка стрельбы не нажата
    R2_AXIS_INDEX = 5
    THRESHOLD = 0.5
    return joystick.get_axis(R2_AXIS_INDEX) > THRESHOLD #get_axis читает значение оси 



# with open('.txt', 'r', encoding='utf-8') as file:
#     m = file.read()
# with open('.txt', 'w', encoding='utf-8') as file:
#     file.write(new_m)
