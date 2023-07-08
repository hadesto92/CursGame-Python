import time

from static import *
from utilis import scale_to, mirror_flip
from typing import Optional
from bee_behaviour import BeeAnimation
from branch_provider import BranchProvider

bee_anim: Optional[BeeAnimation] = None
branches: Optional[BranchProvider] = None

scale_to(SCALABLE, (BASE_WIDTH, BASE_HEIGHT), (WIDTH, HEIGHT))

# Zmienne statyczne
hit = False
hit_time = time.time()
lumberjack_on_left = True


# Zmiana rozdzielczości ekranu za pomocą klawisza F z pełnoekranowego na okienkowy lub odwrtonie
def on_key_down():
    global hit, hit_time, lumberjack_on_left

    if keyboard.F:
        if is_fullscreen():
            surface_size = screen.surface.get_size()
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            scale_to(SCALABLE, surface_size, (WIDTH, HEIGHT), True)
            scale_to(branches.all_branches(), surface_size, (WIDTH, HEIGHT), True)

        else:
            surface_size = screen.surface.get_size()
            screen.surface = pygame.display.set_mode((FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT), pygame.FULLSCREEN)
            scale_to(SCALABLE, surface_size, (FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT), True)
            scale_to(branches.all_branches(), surface_size, (FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT), True)

        change_fullscreen()
        bee_anim.set_screen(screen)
        bee_anim.reset_animation()

    if keyboard.LEFT or keyboard.RIGHT:
        hit = True
        hit_time = time.time()

    if keyboard.LEFT and not lumberjack_on_left:
        mirror_flip(lumberjack_ready, True, False)
        mirror_flip(lumberjack_hit, True, False)
        lumberjack_on_left = True
        lumberjack_ready.x -= 3.44 * trunk.width
        lumberjack_hit.x -= 2 * trunk.width

    if keyboard.RIGHT and lumberjack_on_left:
        mirror_flip(lumberjack_ready, True, False)
        mirror_flip(lumberjack_hit, True, False)
        lumberjack_on_left = False
        lumberjack_ready.x += 3.44 * trunk.width
        lumberjack_hit.x += 2 * trunk.width

    if keyboard.LEFT or keyboard.RIGHT:
        branches.hit()


def update():
    global bee_anim, hit, hit_time, branches
    if not bee_anim:
        bee_anim = BeeAnimation(screen)
        bee_anim.animate_bee()

    if not branches:
        branches = BranchProvider(screen)

    screen_width = screen.surface.get_size()[0]
    for i, cloud in enumerate(clouds):
        cloud.x += cloud_speed[i] * (screen_width / BASE_WIDTH)
        if cloud.x > screen_width:
            cloud.x = -cloud.width

    if hit:
        if time.time() - hit_time > 0.2:
            hit = False


def draw():
    screen.fill(BLACK)
    backgraound.draw()
    bee.draw()
    # trunk_slice.draw()
    if hit:
        trunk_base.draw()
        trunk.draw()
        lumberjack_hit.draw()
    else:
        wood.draw()
        lumberjack_ready.draw()

    # print("Trunk pos: ", trunk.pos, ", trunk anchor: ", trunk.anchor, "Wielkość ekranu: ", screen.width, ' ' ,screen.height)
    for cloud in clouds:
        cloud.draw()

    for branch in branches.branches_to_draw():
        branch.draw()

pgzrun.go()
