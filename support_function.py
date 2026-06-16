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
    wall_list, enemy_list = enter_room(current_room, rooms, floor_index)
    return floor_index, rooms, current_room, tank, bullet_list, bullet_list_mob, bounty_list, wall_list, enemy_list

def enter(next_room, current_room, tank, wall_list, enemy_list, rooms, floor_index, bullet_list, bullet_list_mob, bounty_list, direction):
    current_room = next_room
    move_tank_after_transition(tank, direction)
    wall_list, enemy_list = enter_room(current_room, rooms, floor_index)
    bullet_list = []
    bullet_list_mob = []
    bounty_list = []
    return current_room, tank, wall_list, enemy_list, bullet_list, bullet_list_mob, bounty_list