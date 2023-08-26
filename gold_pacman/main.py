x = 100
y = 100
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x},{y}'

import pgzrun

from pgzero.screen import Screen
from pgzero.builtins import Actor, keyboard
from pacman_behavior import Pacman
from ghost import Ghost

BLACK = 0, 0, 0

WIDTH = 600
HEIGHT = 660

keys: keyboard
screen: Screen

pacman = Pacman(keys)
ghost = Ghost()

map = Actor("colorful_map", pos=(0, 60), anchor=(0,0))

def draw():
    screen.fill(BLACK)
    map.draw()
    pacman.draw(screen)
    ghost.draw()

def on_key_down(key):
    pacman.on_key_down(key)

def on_key_up(key):
    pacman.on_key_up(key)

def update():
    pacman.update()
    ghost.update(pacman.pacman.pos)

pgzrun.go()