from pgzero.builtins import Actor, animate
from random import randint
from map import get_possible_directions
from time import time

ghost_should_move = 4
def ghost_should_move_up():
    global ghost_should_move
    ghost_should_move += 1

class Ghost:
    def __init__(self):
        self.ghosts = [Actor(f'ghost{i}', pos=(250+(i*20), 360)) for i in range(1,5)]
        for ghost in self.ghosts:
            ghost.dir = randint(0, 3)
            ghost.status = 0
        self.disable_ghost_image = 'ghost5'
        self.enable = True
        self.disable_time = 0
        self.ghost_moves= (1, 0), (0, -1), (-1, 0), (0, 1)
        self.ghost_speed = 5.5

    def disable_ghost(self):
        self.enable = False
        self.disable_time = time()
        for ghost in self.ghosts:
            ghost.image = self.disable_ghost_image

    def enable_ghost(self):
        self.enable = True
        self.disable_time = 0
        for i, ghost in enumerate(self.ghosts):
            ghost.image = f'ghost{i}'

    def draw(self):
        for ghost in self.ghosts:
            ghost.draw()

    def update(self):
        self.move_ghost()

    def move_ghost(self):
        global ghost_should_move
        if ghost_should_move < 4:
            return
        ghost_shoyld_move = 0
        for ghost in self.ghosts:
            direction = get_possible_directions(ghost)
            ghost.dir = randint(0, 3)
            while direction[ghost.dir] == 0:
                ghost.dir = randint(0, 3)
            animate(ghost, pos=(ghost.x+self.ghost_moves[ghost.dir][0]*20, ghost.y+self.ghost_moves[ghost.dir][1]*20), duration=1/self.ghost_speed, tween='linear', on_finished=ghost_should_move_up)
