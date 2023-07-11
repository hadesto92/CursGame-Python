import pgzrun
import pygame
import random
from screeninfo import get_monitors
from pgzero.builtins import Actor, keyboard, Rect, animate, sounds
from pgzero.screen import Screen
screen: Screen

#Deklaracja wielkości ekranu
FULLSCREEN = False
WIDTH = 800
HEIGHT = 450

BASE_WIDTH = 1920
BASE_HEIGHT = 1080

WIDTH_multipler = WIDTH/BASE_WIDTH
HEIGHT_multipler = HEIGHT/BASE_HEIGHT

#Pobranie wielkości pierwszego monitora
monitor = get_monitors()[0]

FULLSCREEN_WIDTH = monitor.width
FULLSCREEN_HEIGHT = monitor.height

#Deklaracja asetów
backgraound = Actor('background.png', pos=(0, 0), anchor=(0, 0))

clouds = [Actor(f'chmurka_0{i}', pos=(i*100, 0), anchor=(0, 0)) for i in range (1, 5)]

bee = Actor('bee_01', pos=(WIDTH/2, HEIGHT/2), anchor=(0, 0))

trunk_temp = Actor('pien_solo')
trunk = Actor('pien_solo', pos=(WIDTH/2, 0), anchor=(trunk_temp.width/2, 0))

trunk_base_temp = Actor('pien_podstawa')
trunk_base = Actor('pien_podstawa', pos=(trunk.x+1.5, trunk.height*HEIGHT_multipler-3), anchor=(trunk_base_temp.width/2, 0))

trunk_slice_temp = Actor('plaster_drewna')
trunk_slice = Actor('plaster_drewna', pos=(trunk.x, trunk.height*HEIGHT_multipler-21), anchor=(trunk_slice_temp.width/2, 0))
trunk_slice_old = Actor('plaster_drewna', pos=(trunk.x, trunk.height*HEIGHT_multipler-21), anchor=(trunk_slice_temp.width/2, 0))

wood_temp = Actor('pien_caly')
wood = Actor('pien_caly', pos=(trunk.x+1.5, trunk.height*HEIGHT_multipler+74), anchor=(wood_temp.width/2, wood_temp.height))

lumberjack_ready_temp = Actor('drwal_01')
lumberjack_ready = Actor('drwal_01', pos=(trunk.x-175, trunk_base.y+(trunk_base.height/2)-20), anchor=(0, lumberjack_ready_temp.height))
lumberjack_ready_old = Actor('drwal_01', pos=(trunk.x-175, trunk_base.y+(trunk_base.height/2)-20), anchor=(0, lumberjack_ready_temp.height))

lumberjack_hit_temp = Actor('drwal_02')
lumberjack_hit = Actor('drwal_02', pos=(trunk.x-160, trunk_base.y+(trunk_base.height/2)-20), anchor=(0, lumberjack_hit_temp.height))
lumberjack_hit_old = Actor('drwal_02', pos=(trunk.x-160, trunk_base.y+(trunk_base.height/2)-20), anchor=(0, lumberjack_hit_temp.height))

gravestone = Actor('rip', pos=(trunk.x-160, trunk_base.y+(trunk_base.height/2)-20), anchor=(0, lumberjack_hit_temp.height))

#print(trunk.x, trunk.y, trunk.height)
#print(trunk_base.x, trunk_base.y, trunk_base.height)
#print(lumberjack_ready.x, lumberjack_ready.y, lumberjack_ready.height)

#Deklaracja obiektów do skalowania
SCALABLE = [backgraound, bee, trunk, trunk_base, trunk_slice, lumberjack_ready, lumberjack_hit, trunk_slice_old, wood, gravestone, lumberjack_ready_old, lumberjack_hit_old] + clouds

#Deklaracja kolorów:
BLACK = 0, 0, 0
ORANGE = 255, 125, 0
RED = 255, 0, 0

#Fizyka poruszania się chmurek
cloud_speed = [random.uniform(0.05, 0.5) for _ in range(4)]


def change_fullscreen():
    global FULLSCREEN
    FULLSCREEN = not FULLSCREEN

def is_fullscreen():
    return FULLSCREEN