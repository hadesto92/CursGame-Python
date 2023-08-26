from pgzero.builtins import Actor, animate
from random import randint
from map import get_possible_directions, get_distans
from time import time

class Ghost:
    def __init__(self):
        self.ghosts = [Actor(f'ghost{i}', pos=(250+(i*18), 360)) for i in range(1,5)]
        for ghost in self.ghosts:
            ghost.dir = 1
            ghost.last_dir = -100
            ghost.status = 0
            ghost.in_center = True
            ghost.decide_point = 0, 7
            ghost.point = 16
            ghost.ghost_moves= (ghost.point, 0), (0, -ghost.point), (-ghost.point, 0), (0, ghost.point)
            ghost.last_point_index = 0
            ghost.new_point_index = 0
            ghost.new_point = ghost.x, ghost.y
            ghost.move = False
        self.disable_ghost_image = 'ghost5'
        self.enable = True
        self.disable_time = 0
        self.ghost_speed = 100

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

    def ghost_in_center(self, ghost):
        if ghost.in_center:
            if 231 < ghost.x < 370 and 257+60 < ghost.y < 337+60:
                if ghost.x == 300 and ghost.y == 360:
                    ghost.in_center = False
                else:
                    ghost.in_center = True
            else:
                ghost.in_center = False
        else:
            ghost.in_center = False

        return ghost.in_center
        #print(ghost.in_center)

    def draw(self):
        for ghost in self.ghosts:
            ghost.draw()

    def update(self):
        self.move_ghost()

    def is_move(self, ghost):
        if ghost.x == ghost.new_point[0] and ghost.y == ghost.new_point[1]:
            return False
        return True

    def move_ghost(self):
        for ghost in self.ghosts:
            if ghost.move == False:
                ghost.move = True
                if self.ghost_in_center(ghost):
                    ghost.new_point = 300, 360
                    animate(ghost, pos=ghost.new_point, duration=1, tween='linear')
                    ghost.new_point_index = 29
                else:
                    direction = get_possible_directions(ghost)
                    if ghost.new_point_index == 56:
                        ghost.last_point_index = 57
                    elif ghost.new_point_index == 57:
                        ghost.last_point_index = 56
                    else:
                        ghost.last_point_index = ghost.new_point_index
                    ghost.new_point = direction[1]
                    ghost.new_point_index = direction[0]
                    animate(ghost, pos=ghost.new_point, duration=get_distans(ghost)/self.ghost_speed, tween='linear')
            else:
                if not self.is_move(ghost):
                    ghost.move = False
