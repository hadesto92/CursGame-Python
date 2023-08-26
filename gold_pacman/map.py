import random

from pygame import image, Color
from random import randint

moveimage = image.load('images/move_map.png')

#(x,y),(index to move)
map_point=[((35,100),(1,6)),
           ((130,100),(0,2,7)),
           ((270,100),(1,9)),
           ((330,100),(10,4)),
           ((470,100),(3,5,12)),
           ((570,100),(4,13)),
           ((35,180),(0,7,14)),
           ((130,180),(6,1,8,15)),
           ((210,180),(7,9,16)),
           ((270,180),(2,8,10)),
           ((330,180),(9,11,3)),
           ((390,180),(10,12,19)),
           ((470,180),(11,13,20,4)),
           ((570,180),(5,12,21)),
           ((35,260),(6,15)),
           ((130,260),(7,14,27)),
           ((210,240),(8,17)),
           ((270,240),(16,23)),
           ((330,240),(19,25)),
           ((390,240),(18,11)),
           ((470,260),(12,21,31)),
           ((570,260),(20,13)),
           ((210,300),(28,23)),
           ((270,300),(22,24,17)),
           ((300,300),(23,25)),
           ((330,300),(24,26,18)),
           ((390,300),(25,30)),
           ((130,360),(15,28,35,56)),
           ((210,360),(27,22,32)),
           ((300,360),(24)),
           ((390,360),(26,31,33)),
           ((470,360),(20,30,36,57)),
           ((210,420),(28,33,39)),
           ((390,420),(30,32,42)),
           ((35,460),(35,44)),
           ((130,460),(34,27,38)),
           ((470,460),(31,37,43)),
           ((570,460),(36,51)),
           ((130,480),(35,39,45)),
           ((210,480),(38,32,40)),
           ((270,480),(39,47)),
           ((330,480),(42,48)),
           ((390,480),(41,43)),
           ((470,480),(36,42,50)),
           ((35,565),(34,45,52)),
           ((130,565),(38,44,46)),
           ((220,565),(45,47,53)),
           ((270,565),(46,47,40)),
           ((330,565),(47,49,41)),
           ((385,565),(48,50,54)),
           ((470,565),(49,43,51)),
           ((570,565),(37,50,55)),
           ((35,620),(44,53)),
           ((220,620),(46,52,54)),
           ((385,620),(49,53,55)),
           ((570,620),(51,54)),
           ((0, 360),(27)),
           ((580,360),(31))]

def check_move_point(pacman):
    move_x, move_y = 0, 0

    if pacman.keys_active['right']:
        move_x = 5
    elif pacman.keys_active['left']:
        move_x = -5
    elif pacman.keys_active['up']:
        move_y = -5
    elif pacman.keys_active['down']:
        move_y = 5

    if pacman.x+move_x < 0:
        pacman.x = 585
        return True
    elif pacman.x+move_x+pacman.width/2 > 600:
        pacman.x = 0
        return True

    if moveimage.get_at((int(pacman.x+move_x), int(pacman.y+move_y-60))) != Color('black'):
        return False
    return True

def get_possible_directions(ghost):

    last_index  = ghost.new_point_index

    index_move = -1

    if last_index == 29:
        index_move = 24
    elif last_index == 56:
        ghost.x = 580
        ghost.y = 360
        index_move = 31
    elif last_index == 57:
        ghost.x = 0
        ghost.y = 360
        index_move = 27
    else:
        for i, index in enumerate(map_point):
            if last_index == i:
                index_move = index[1][randint(0, len(index[1])-1)]
                while index_move == ghost.last_point_index:
                    index_move = index[1][randint(0, len(index[1]) - 1)]
                #print(map_point[index_move][0])

    return index_move, map_point[index_move][0]

def get_distans(ghost):
    distans = 0

    last_point_x = map_point[ghost.last_point_index][0][0]
    last_point_y = map_point[ghost.last_point_index][0][1]

    new_point_x = map_point[ghost.new_point_index][0][0]
    new_point_y = map_point[ghost.new_point_index][0][1]

    if abs(last_point_x-new_point_x)>0:
        return abs(last_point_x-new_point_x)
    else:
        return abs(last_point_y - new_point_y)

#new_position = get_possible_directions()

#print(new_position[0])
#print(new_position[1])