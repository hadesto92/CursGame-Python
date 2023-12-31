from pgzero.builtins import Actor
from time import time

from map import check_move_point


class Pacman:
    def __init__(self, keys, lives=3):
        self.keys = keys
        self.images = ["pacman_o", "pacman_or", "pacman_c", "pacman_cr"]
        self.pacman = Actor("pacman_o")
        self.pacman.keys_active = {'left': False, 'right': False, 'down': False, 'up': False}
        self.pacman.x = 290
        self.pacman.y = 560
        self.lives = lives
        self.animation_time = 0.1
        self.animation = False
        self.dt = None
        self.start_pos = self.pacman.x, self.pacman.y

    def on_key_down(self, key):

        options_key = []

        with open('conf.txt', 'r') as file:
            for line in file:
                splitted_line = line.split()
                options_key.append((splitted_line[0], splitted_line[1]))

        for name, keys in options_key:
            #print(key.name, name, keys)
            if name == 'RIGHT:' and key.name == keys:
                self.pacman.keys_active['right'] = True
            if name == 'LEFT:' and key.name == keys:
                self.pacman.keys_active['left'] = True
            if name == 'UP:' and key.name == keys:
                self.pacman.keys_active['up'] = True
            if name == 'DOWN:' and key.name == keys:
                self.pacman.keys_active['down'] = True

    def on_key_up(self, key):

        options_key = []

        with open('conf.txt', 'r') as file:
            for line in file:
                splitted_line = line.split()
                options_key.append((splitted_line[0], splitted_line[1]))

        for name, keys in options_key:
            if name == 'RIGHT:' and key.name == keys:
                self.pacman.keys_active['right'] = False
            if name == 'LEFT:' and key.name == keys:
                self.pacman.keys_active['left'] = False
            if name == 'UP:' and key.name == keys:
                self.pacman.keys_active['up'] = False
            if name == 'DOWN:' and key.name == keys:
                self.pacman.keys_active['down'] = False

    def draw(self, screen):
        self.pacman.draw()
        for live in range(self.lives):
            screen.blit("pacman_l", (10 + live * 20, 30))

    def move_pressed(self):
        pressed = any(value for value in self.pacman.keys_active.values())
        if not pressed:
            self.animation = False
            self.dt = None
        return pressed

    def update(self):
        move_pressed = self.move_pressed()

        #print(self.pacman.x, self.pacman.y)

        if not move_pressed:
            return

        can_move = check_move_point(self.pacman)

        if not can_move:
            return

        if move_pressed and self.dt is None:
            self.animation = True
            self.dt = time()
        if self.dt is not None:
            now = time()
            if now - self.dt > self.animation_time:
                self.animation = not self.animation
                self.dt = now

        straight_pacman_image = "pacman_c" if self.animation else "pacman_o"
        flipped_pacman_image = "pacman_cr" if self.animation else "pacman_or"

        if self.pacman.keys_active['right']:
            self.pacman.x += 3
            self.pacman.image = straight_pacman_image
            self.pacman.angle = 0
        elif self.pacman.keys_active['left']:
            self.pacman.x -= 3
            self.pacman.image = flipped_pacman_image
            self.pacman.angle = 180
        elif self.pacman.keys_active['up']:
            self.pacman.y -= 3
            self.pacman.image = straight_pacman_image
            self.pacman.angle = 90
        elif self.pacman.keys_active['down']:
            self.pacman.y += 3
            self.pacman.image = flipped_pacman_image
            self.pacman.angle = 270