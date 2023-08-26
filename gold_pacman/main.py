x = 100
y = 100
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x},{y}'

import pgzrun
import sys

from pgzero.screen import Screen
from pgzero.builtins import Actor, keyboard, sounds
from pacman_behavior import Pacman
from ghost import Ghost
from coins import Coins

BLACK = 0, 0, 0
GOLD = 255, 215, 0

WIDTH = 600
HEIGHT = 660

keys: keyboard
screen: Screen

pacman = Pacman(keys)
ghost = Ghost()
coins = Coins()

POINTS = 0

map = Actor("colorful_map", pos=(0, 60), anchor=(0,0))

def draw():
    screen.fill(BLACK)
    map.draw()
    coins.draw_coins()
    pacman.draw(screen)
    ghost.draw()
    screen.draw.text(f'{POINTS}', color=GOLD, fontsize=50, fontname='bungee-regular', topright=(WIDTH-10, 5), owidth = 1, ocolor=(100, 100, 100))

def on_key_down(key):
    pacman.on_key_down(key)

def on_key_up(key):
    pacman.on_key_up(key)

def update_by_coin():
    global POINTS
    if pacman.move_pressed():
        coin_type = coins.check_collision(pacman.pacman)
        if coin_type == "coin":
            POINTS += 10
            sounds.eating.play()
        elif coin_type == "powerup":
            POINTS += 100
            sounds.eating.play()
            ghost.disable_ghost()
        elif coin_type == "won":
            pass
        else:
            pass

def update_by_ghost():
    global POINTS
    coll_type, optional_ghost = ghost.check_collision(pacman.pacman)
    if coll_type == 'ghost_busted':
        POINTS += 100
        optional_ghost.pos = optional_ghost.start_pos
        optional_ghost.current_animation.stop()
        optional_ghost.in_center = True
        optional_ghost.move = False
    elif coll_type == 'pacman_busted':
        for some_ghost in ghost.ghosts:
            some_ghost.pos = some_ghost.start_pos
            some_ghost.current_animation.stop()
            some_ghost.in_center = True
            some_ghost.move = False
        pacman.pacman.pos = pacman.start_pos
        pacman.lives -= 1
        if not pacman.lives:
            sys.exit(0)

    else:
        pass

def update():
    pacman.update()
    ghost.update(pacman.pacman.pos)
    update_by_coin()
    update_by_ghost()

pgzrun.go()