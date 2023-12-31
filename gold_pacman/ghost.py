from pgzero.builtins import Actor, animate, Rect
from random import randint
from math import sqrt
from map import get_possible_directions, get_distans, get_possible_directions_near_pacman, serch_direction
from time import time

class Ghost:
    def __init__(self, level=1):
        self.ghosts = [Actor(f'ghost{i}', pos=(250+(i*18), 360)) for i in range(1,5)]
        for ghost in self.ghosts:
            ghost.status = 0
            ghost.in_center = True
            ghost.start_pos = ghost.pos
            ghost.last_point_index = 0
            ghost.new_point_index = 0
            ghost.new_point = ghost.x, ghost.y
            ghost.move = False
            ghost.run_pacman = False
            ghost.current_animation = None
        self.disable_ghost_image = 'ghost5'
        self.enable = True
        self.disable_time = 0
        self.ghost_speed = 150
        self.disable_max_time = 15

    def disable_ghost(self):
        self.enable = False
        self.disable_time = time()
        for ghost in self.ghosts:
            ghost.image = self.disable_ghost_image

    def enable_ghost(self):
        self.enable = True
        self.disable_time = 0
        for i, ghost in enumerate(self.ghosts):
            ghost.image = f'ghost{i+1}'

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

    def update(self, pacman_pos):
        if not self.enable:
            left = self.disable_max_time - (time() - self.disable_time)
            if 0 < left < 2:
                if str(left)[:3][-1] in ['1', '3', '5', '7', '9']:
                    for i, ghost in enumerate(self.ghosts):
                        ghost.image = f'ghost{i+1}'
                else:
                    for ghost in self.ghosts:
                        ghost.image = self.disable_ghost_image
            elif left < 0:
                self.enable_ghost()
        self.move_ghost(pacman_pos)

    def is_move(self, ghost):
        if ghost.x == ghost.new_point[0] and ghost.y == ghost.new_point[1]:
            return False
        return True

    def check_pacman_pos(self, ghost, pacman_pos):
        distance = sqrt(pow(ghost.x - pacman_pos[0], 2) + pow(ghost.y - pacman_pos[1], 2))
        return distance

    def move_ghost(self, pacman_pos):
        for ghost in self.ghosts:
            if ghost.move == False:
                ghost.move = True
                if self.ghost_in_center(ghost):
                    ghost.new_point = 300, 360
                    ghost.current_animation = animate(ghost, pos=ghost.new_point, duration=1/10, tween='linear')
                    ghost.new_point_index = 29
                else:
                    if self.check_pacman_pos(ghost, pacman_pos) < 122:
                        if self.check_pacman_pos(ghost, pacman_pos) < 50:
                            ghost.current_animation = animate(ghost, pos=pacman_pos, duration=1/3, tween='linear')
                            ghost.run_pacman = True
                            ghost.move = False
                            continue
                        else:
                            if ghost.run_pacman == True:
                                direction = serch_direction(pacman_pos)
                                ghost.new_point = direction[1]
                                ghost.last_point_index = ghost.new_point_index
                                ghost.new_point_index = direction[0]
                                ghost.current_animation = animate(ghost, pos=ghost.new_point, duration=1/10, tween='linear')
                                ghost.run_pacman = False
                                ghost.move = False
                                continue
                            else:
                                if randint(1, 10) % 10 == 0:
                                    direction = get_possible_directions(ghost)
                                else:
                                    direction = get_possible_directions_near_pacman(ghost, pacman_pos)
                    else:
                        direction = get_possible_directions(ghost)

                    ghost.new_point = direction[1]

                    if ghost.new_point_index == 56:
                        ghost.last_point_index = 57
                    elif ghost.new_point_index == 57:
                        ghost.last_point_index = 56
                    else:
                        ghost.last_point_index = ghost.new_point_index
                    ghost.new_point_index = direction[0]
                    speed = get_distans(ghost)/self.ghost_speed
                    if speed == 0:
                        speed = 1/10
                    ghost.current_animation = animate(ghost, pos=ghost.new_point, duration=speed, tween='linear')
            else:
                if not self.is_move(ghost):
                    ghost.move = False

    def check_collision(self, pacman):
        x, y, width, height = pacman.x, pacman.y, pacman.width, pacman.height
        rect = Rect(x - width / 2, y - height / 2, width, height)
        for ghost in self.ghosts:
            if ghost.colliderect(rect):
                if self.enable:
                    return "pacman_busted", "None"
                else:
                    return "ghost_busted", ghost
        return "None", "None"