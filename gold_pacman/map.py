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