import pygame
from tank import Tank
from settings import *
from bullet import Bullet
from wall import Wall, Baza
from enemy import sEnemy, BossEnemy
import time
import random

def create_room():
    return {
        'doors': set(), 
        'exit': False,  
        'cleared': False,  
        'enemy_positions': [],
    }


def generate_room_enemy_positions(floor_index, exit_room):
    if not exit_room:
        enemy_positions = []
        enemy_count = random.randint(1, min(3, 1 + floor_index)) 

        while len(enemy_positions) < enemy_count:
            x = random.randint(80, 780)  
            y = random.randint(80, 780)  
            too_close = False
            for px, py in enemy_positions:
                if abs(x - px) < 60 and abs(y - py) < 60:
                    too_close = True
                    break
            if too_close:
                continue  
            enemy_positions.append((x, y))  

        return enemy_positions 
    else:
        enemy_positions = []
        enemy_positions.append((random.randint(80, 780) , random.randint(80, 780)))  
        return enemy_positions

def generate_floor(floor_index):
    rooms = {}
    current_room = (ROOM_GRID_WIDTH // 2, ROOM_GRID_HEIGHT // 2)  
    rooms[current_room] = create_room() 

    path_length = random.randint(ROOM_MIN_LENGTH, ROOM_MAX_LENGTH) 

    for i in range(path_length):
        candidates = []  
        for direction, (dx, dy) in ROOM_STEPS.items():
            next_room = (current_room[0] + dx, current_room[1] + dy)
            if 0 <= next_room[0] < ROOM_GRID_WIDTH and 0 <= next_room[1] < ROOM_GRID_HEIGHT and next_room not in rooms:
                candidates.append((direction, next_room)) 

        if not candidates:
            break  

        direction, next_room = random.choice(candidates) 
        rooms[current_room]['doors'].add(direction)  
        rooms[next_room] = create_room()  
        rooms[next_room]['doors'].add(ROOM_OPPOSITE[direction]) 
        current_room = next_room  

    rooms[current_room]['exit'] = True  

    for room in rooms.values():
        room['enemy_positions'] = generate_room_enemy_positions(floor_index, room['exit'])   
    return rooms, (ROOM_GRID_WIDTH // 2, ROOM_GRID_HEIGHT // 2)


def build_room_walls(room):
    wall_list = []
    exit_door = None
    open_doors = room['doors'] if room['cleared'] else set()
    if room['exit'] and room['cleared'] and len(open_doors) < 2:
        d1 = list(room['doors'])[0]
        all_doors = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        opds = set(open_doors)
        all_doors.remove(opds.pop())
        open_doors.add(random.choice(all_doors))
        doors_set = list(room['doors'])
        doors_set.remove(d1)
        doors_list = list(doors_set)
        exit_door = doors_list[0]
        print("Exit door:", exit_door)
        
    for i in range(0, SCREEN_WIDTH, 40):
        if 'UP' not in open_doors or not (DOOR_START <= i <= DOOR_END):
            wall_list.append(Wall(i, 0, 100000, 'sprites/wall.png'))
        elif exit_door == 'UP' and (DOOR_START <= i <= DOOR_END) and room["exit"]:
            wall_list.append(Baza(i, 0, 1, 'sprites/baza.jpg'))
            print("Baza UP")
        if 'DOWN' not in open_doors or not (DOOR_START <= i <= DOOR_END):
            wall_list.append(Wall(i, 860, 100000, 'sprites/wall.png'))  # нижняя стена
        elif exit_door == 'DOWN' and (DOOR_START <= i <= DOOR_END) and room["exit"]:
            wall_list.append(Baza(i, 860, 1, 'sprites/baza.jpg'))
            print("Baza DOWN")
            
    for i in range(0, SCREEN_HEIGHT, 40):
        if 'LEFT' not in open_doors or not (DOOR_START <= i <= DOOR_END):
            wall_list.append(Wall(0, i, 100000, 'sprites/wall.png'))  # левая стена
        elif exit_door == 'LEFT' and (DOOR_START <= i <= DOOR_END) and room["exit"]:
            wall_list.append(Baza(0, i, 1, 'sprites/baza.jpg'))
            print("Baza LEFT")
        if 'RIGHT' not in open_doors or not (DOOR_START <= i <= DOOR_END):
            wall_list.append(Wall(860, i, 100000, 'sprites/wall.png'))  # правая стена
        elif exit_door == 'RIGHT' and (DOOR_START <= i <= DOOR_END) and room["exit"]:
            wall_list.append(Baza(860, i, 1, 'sprites/baza.jpg'))
            print("Baza RIGHT")

    return wall_list


def spawn_room_enemies(room):
    if room['exit'] == False:
        return [sEnemy(x, y) for x, y in room['enemy_positions']]
    else:
        print(room)
        return [BossEnemy(x, y) for x, y in room['enemy_positions']]
        


def enter_room(room_coord, rooms, floor_index):
    room = rooms[room_coord]
    wall_list = build_room_walls(room)
    print(room)
    enemy_list = [] if room['cleared'] else spawn_room_enemies(room)
    return wall_list, enemy_list


def move_tank_after_transition(tank, direction):                   
    if direction == 'LEFT':
        tank.x = SCREEN_WIDTH - ROOM_EXIT_OFFSET 
    elif direction == 'RIGHT':
        tank.x = ROOM_ENTRY_OFFSET  
    elif direction == 'UP':
        tank.y = SCREEN_HEIGHT - ROOM_EXIT_OFFSET 
    elif direction == 'DOWN':
        tank.y = ROOM_ENTRY_OFFSET  
    tank.rect.topleft = (tank.x, tank.y)