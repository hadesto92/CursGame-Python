from pygame import image, Color

moveimage = image.load('images/move_map.png')

def check_move_point(pacman):
    move_x, move_y = 0, 0

    if pacman.keys_active['right']:
        move_x = 5
    elif pacman.keys_active['left']:
        move_x = -5
    elif pacman.keys_active['up']:
        move_y = -5
    elif pacman.keys_active['down']:
        move_y = 5

    if pacman.x+move_x < 0:
        pacman.x = 585
        return True
    elif pacman.x+move_x+pacman.width/2 > 600:
        pacman.x = 0
        return True

    if moveimage.get_at((int(pacman.x+move_x), int(pacman.y+move_y-60))) != Color('black'):
        return False
    return True

def get_possible_directions(ghost):
    bw = 18 #black width
    if ghost.in_center:
        bw = 20
    directions = [0, 0, 0, 0]   #right, up, left, down
    if ghost.x - bw < 0:
        ghost.x = 585
    elif ghost.x + bw > 600:
        ghost.x = bw

    move_x, move_y = ghost.decide_point
    dpx = ghost.x + move_x
    dpy = ghost.y + move_y

    if moveimage.get_at((int(dpx+bw), int(dpy-60))) == Color('black'):
        directions[0] = 1
    if moveimage.get_at((int(dpx), int(dpy-60-bw))) == Color('black'):
        directions[1] = 1
    if moveimage.get_at((int(dpx-bw), int(dpy-60))) == Color('black'):
        directions[2] = 1
    if moveimage.get_at((int(dpx), int(dpy-60+bw))) == Color('black'):
        directions[3] = 1
    return directions