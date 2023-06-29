import pgzrun
import pygame
import random
from screeninfo import get_monitors
from pgzero.builtins import Actor, keyboard
from pgzero.screen import Screen
screen: Screen
keys: keyboard

#Deklaracja wielkości ekranu
FULLSCREEN = False
WIDTH = 800
HEIGHT = 450

BASE_WIDTH = 1920
BASE_HEIGHT = 1080

#Pobranie wielkości pierwszego monitora
monitor = get_monitors()[0]

FULLSCREEN_WIDTH = monitor.width
FULLSCREEN_HEIGHT = monitor.height

#Deklaracja asetów
backgraound = Actor('background.png', pos=(0, 0), anchor=(0, 0))
clouds = [Actor(f'chmurka_0{i}', pos=(i*100, 0), anchor=(0, 0)) for i in range (1, 5)]
bee = Actor('bee_01', pos=(WIDTH/2, HEIGHT/2), anchor=(0, 0))
trunk_temp = Actor('pien_solo')
trunk = Actor('pien_solo', pos=(WIDTH/2, 0), anchor=(0.5, 0))

#Deklaracja obiektów do skalowania
SCALABLE = [backgraound, bee, trunk] + clouds

#Deklaracja kolorów:
BLACK = 0, 0, 0

#Fizyka poruszania się chmurek
cloud_speed = [random.uniform(0.05, 0.5) for _ in range(4)]


def change_fullscreen():
    global FULLSCREEN
    FULLSCREEN = not FULLSCREEN

def is_fullscreen():
    return FULLSCREEN