import pgzrun
import pygame
from pgzero.builtins import Actor, keyboard
from pgzero.screen import Screen
screen: Screen
keys: keyboard

#Deklaracja wielkości ekranu
FULLSCREEN = False
WIDTH = 800
HEIGHT = 600

BASE_WIDTH = 1920
BASE_HEIGHT = 1080

FULLSCREEN_WIDTH = 1920
FULLSCREEN_HEIGHT = 1080

#Deklaracja asetów
backgraound = Actor('background.png', pos=(0, 0), anchor=(0, 0))

#Deklaracja kolorów:
BLACK = 0, 0, 0

def change_fullscreen():
    global FULLSCREEN
    FULLSCREEN = not FULLSCREEN

def is_fullscreen():
    return FULLSCREEN