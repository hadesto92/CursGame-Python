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
        self.ghosts = [Actor(f'ghost{i}', pos=(250+(i*18), 360)) for i in range(1,5)]
        for ghost in self.ghosts:
            ghost.dir = 1
            ghost.last_dir = -100
            ghost.status = 0
            ghost.in_center = True
            ghost.decide_point = 0, 6
        self.disable_ghost_image = 'ghost5'
        self.enable = True
        self.disable_time = 0
        self.ghost_moves= (16, 0), (0, -16), (-16, 0), (0, 16)
        self.ghost_speed = 3

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

    def ghost_in_center(self):
        for ghost in self.ghosts:
            if 231 < ghost.x < 370 and 257+60 < ghost.y < 337+60:
                ghost.in_center = True
            else:
                ghost.in_center = False
            #print(ghost.in_center)

    def draw(self):
        for ghost in self.ghosts:
            ghost.draw()

    def update(self):
        self.ghost_in_center()
        self.move_ghost()

    def random_dir(self, last_dir, direction):

        new_dir = 0

        if direction.count(1) > 0:
            if last_dir == 0:
                new_dir = randint(0, 3)
                while direction[new_dir] == 0 or new_dir == 2:
                    new_dir = randint(0, 3)
            if last_dir == 1:
                new_dir = randint(0, 3)
                while direction[new_dir] == 0 or new_dir == 3:
                    new_dir = randint(0, 3)
            if last_dir == 2:
                new_dir = randint(0, 3)
                while direction[new_dir] == 0 or new_dir == 0:
                    new_dir = randint(0, 3)
            if last_dir == 3:
                new_dir = randint(0, 3)
                while direction[new_dir] == 0 or new_dir == 1:
                    new_dir = randint(0, 3)
        else:
            if last_dir == 0:
                new_dir = 2
            if last_dir == 1:
                new_dir = 3
            if last_dir == 2:
                new_dir = 0
            if last_dir == 3:
                new_dir = 1

        return new_dir

    def move_ghost(self):
        global ghost_should_move
        if ghost_should_move < 4:
            return
        ghost_shoyld_move = 0
        for ghost in self.ghosts:
            direction = get_possible_directions(ghost)
            if ghost.in_center and direction[1]:
                ghost.dir = 1
            else:
                ghost.dir = self.random_dir(ghost.last_dir, direction)
            #while direction[ghost.dir] == 0 or (abs(ghost.last_dir - ghost.dir) == 2 and direction.count(1) > 1):
                #ghost.dir = self.random_dir(ghost.last_dir, direction)
            animate(ghost, pos=(ghost.x+self.ghost_moves[ghost.dir][0], ghost.y+self.ghost_moves[ghost.dir][1]), duration=1/self.ghost_speed, tween='linear', on_finished=ghost_should_move_up)
            ghost.last_dir = ghost.dir