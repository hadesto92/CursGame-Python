x = 100
y = 100
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x},{y}'

import pgzrun

from pgzero.screen import Screen
from pgzero.builtins import Actor, keyboard, sounds, music
from pacman_behavior import Pacman
from ghost import Ghost
from coins import Coins
from time import time
from best_players import BestPlayers
from typing import Optional
from menu import Menu

BLACK = 0, 0, 0
GOLD = 255, 215, 0

WIDTH = 600
HEIGHT = 660

keys: keyboard
screen: Screen
mouse_pos = 0, 0
mouse_left_button = False
key_name = ''
key_clicked = False

pacman = Pacman(keys)
ghost = Ghost()
coins = Coins()
best_players: Optional[BestPlayers] = None
main_menu: Optional[Menu] = None

POINTS = 0
LEVEL = 3

map = Actor("colorful_map", pos=(0, 60), anchor=(0,0))

def draw():
    global LEVEL
    #print('Menu: ', main_menu.main_menu_bool, ', play: ', main_menu.play_bool)
    if main_menu.play_bool:
        screen.fill(BLACK)
        if not pacman.lives:
            best_players.draw()
            return
        map.draw()
        coins.draw_coins()
        pacman.draw(screen)
        ghost.draw()
        screen.draw.text(f'{POINTS}', color=GOLD, fontsize=50, fontname='bungee-regular', topright=(WIDTH-10, 5), owidth = 1, ocolor=(100, 100, 100))
        screen.draw.text(f'GOLD', color=GOLD, fontsize=30, fontname='bungee-regular', center=((WIDTH/2)+20, 15), owidth=1, ocolor=(100, 100, 100))
        screen.draw.text(f'PACMAN', color=GOLD, fontsize=30, fontname='bungee-regular', center=((WIDTH/2)+20, 45), owidth=1, ocolor=(100, 100, 100))
        screen.draw.text(f'Poziom {LEVEL}', color=GOLD, fontsize=20, fontname='bungee-regular', topleft=(8, 4), owidth=1, ocolor=(100, 100, 100))

        if not ghost.enable:
            time_left = time() - ghost.disable_time
            screen.draw.text(f'POWER: {int(ghost.disable_max_time-time_left)}', color=(188, 19, 254), fontsize=20, fontname='bungee-regular', center=((WIDTH/2)-110, 15), owidth=1, ocolor=(100, 100, 100))
    else:
        if main_menu.main_menu_bool:
            screen.fill(BLACK)
            main_menu.main_menu()
        if main_menu.highscore_bool:
            screen.fill(BLACK)
            main_menu.highscore()
        if main_menu.option_bool:
            screen.fill(BLACK)
            main_menu.option()
        if main_menu.description_bool:
            screen.fill(BLACK)
            main_menu.description()



def on_key_down(key):

    global key_name, key_clicked

    if not pacman.lives:
        best_players.append_to_name(key)
        if key.name == 'RETURN':
            answer = best_players.change_color()
            if answer == 'exit':
                main_menu.main_menu_bool = True
                main_menu.play_bool = False
        return
    pacman.on_key_down(key)

    key_name = key.name
    key_clicked = True

def on_key_up(key):
    global key_clicked

    if not pacman.lives:
        return
    pacman.on_key_up(key)
    key_clicked = False

def add_points(some_points):
    global POINTS
    POINTS += some_points
    if POINTS % 15000 == 0:
        pacman.lives += 1
        sounds.new_live.play()
        return 'sound'
    return None

def update_by_coin():
    global LEVEL, coins
    if pacman.move_pressed():
        sounds.walk.play()
        coin_type = coins.check_collision(pacman.pacman)
        if coin_type == "coin":
            add_points(10)
            sounds.eating.play()
        elif coin_type == "powerup":
            add_points(100)
            sounds.powerup.play()
            ghost.disable_ghost()
        elif coin_type == "won":
            LEVEL += 1
            add_points(1000)
            sounds.level_up.play()
            pacman.pacman.pos = pacman.start_pos
            ghost.disable_max_time = max(3, 15 - (LEVEL-1))
            ghost.enable_ghost()
            for some_ghost in ghost.ghosts:
                some_ghost.pos = some_ghost.start_pos
                some_ghost.current_animation.stop()
                some_ghost.in_center = True
                some_ghost.move = False
            coins = Coins()
        else:
            pass

def update_by_ghost():
    if not pacman.lives:
        best_players.set_score(POINTS)
        return
    coll_type, optional_ghost = ghost.check_collision(pacman.pacman)
    if coll_type == 'ghost_busted':
        add_points(100)
        if not sounds:
            sounds.eating.play()
        optional_ghost.pos = optional_ghost.start_pos
        optional_ghost.current_animation.stop()
        optional_ghost.in_center = True
        optional_ghost.move = False
    elif coll_type == 'pacman_busted':
        sounds.lost_life.play()
        for some_ghost in ghost.ghosts:
            some_ghost.pos = some_ghost.start_pos
            some_ghost.current_animation.stop()
            some_ghost.in_center = True
            some_ghost.move = False
        pacman.pacman.pos = pacman.start_pos
        pacman.lives -= 1
    else:
        pass

def on_mouse_move(pos):
    global mouse_pos
    mouse_pos = pos

def on_mouse_down(button):
    global mouse_left_button
    if button == 1:
        mouse_left_button = True

def on_mouse_up(button):
    global mouse_left_button
    if button == 1:
        mouse_left_button = False


def update():
    global best_players, main_menu
    if not best_players:
        best_players = BestPlayers(screen)
    if not main_menu:
        main_menu = Menu(screen, WIDTH, HEIGHT, mouse_pos, mouse_left_button, key_name, key_clicked)

    if main_menu.play_bool:
        pacman.update()
        ghost.update(pacman.pacman.pos)
        update_by_coin()
        update_by_ghost()
    else:
        main_menu.update(screen, WIDTH, HEIGHT, mouse_pos, mouse_left_button, key_name, key_clicked)

music.play('music')
music.set_volume(0.2)
pgzrun.go()