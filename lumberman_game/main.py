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
collision = False
time_left = 5
max_time = 5
last_time = 0
endgame = False
score = 0
gravestone.x = lumberjack_hit.x-20

# Zmiana rozdzielczości ekranu za pomocą klawisza F z pełnoekranowego na okienkowy lub odwrtonie
def on_key_down():
    global hit, hit_time, lumberjack_on_left, collision, endgame, time_left, max_time, score

    if keyboard.F:
        if is_fullscreen():
            surface_size = screen.surface.get_size()
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            scale_to(SCALABLE+branches.left_branch+branches.right_branch, surface_size, (WIDTH, HEIGHT), True)

        else:
            surface_size = screen.surface.get_size()
            screen.surface = pygame.display.set_mode((FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT), pygame.FULLSCREEN)
            scale_to(SCALABLE+branches.left_branch+branches.right_branch, surface_size, (FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT), True)


        change_fullscreen()
        bee_anim.set_screen(screen)
        bee_anim.reset_animation()

    if not collision and not endgame:
        if keyboard.LEFT and not lumberjack_on_left:
            mirror_flip(lumberjack_ready, True, False)
            mirror_flip(lumberjack_hit, True, False)
            lumberjack_on_left = True
            lumberjack_ready.x -= 3.44 * trunk.width
            lumberjack_hit.x -= 2 * trunk.width
            gravestone.x = lumberjack_hit.x-20

        if keyboard.RIGHT and lumberjack_on_left:
            mirror_flip(lumberjack_ready, True, False)
            mirror_flip(lumberjack_hit, True, False)
            lumberjack_on_left = False
            lumberjack_ready.x += 3.44 * trunk.width
            lumberjack_hit.x += 2 * trunk.width
            gravestone.x = lumberjack_ready.x

        if keyboard.LEFT or keyboard.RIGHT:
            hit = True
            hit_time = time.time()
            collision = branches.collision_branch(lumberjack_on_left)
            branches.hit_tree()
            score += 1
            if time_left < max_time:
                if score < 1000:
                    time_left += 2/score + 0.3
                elif 1000 <= score < 2000:
                    time_left += 2 / score + 0.25
                elif 2000 <= score < 4000:
                    time_left += 2 / score + 0.2
                elif 4000 <= score < 8000:
                    time_left += 2 / score + 0.15
                else:
                    time_left += 2 / score + 0.11

                if score % 1000 == 0:
                    if time_left+5 <= max_time:
                        time_left+=5
                    else:
                        time_left = max_time


def update():
    global bee_anim, hit, hit_time, branches, last_time, time_left, collision, endgame
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

    #Mechanika warunku zakończenia gry
    now = time.time()
    if not last_time:
        last_time = now
    delta_time = now - last_time
    time_left -= delta_time
    last_time = now

    if time_left < 0 and not collision:
        time_left = 0
        endgame = True


def draw():
    screen.fill(BLACK)
    backgraound.draw()
    bee.draw()
    #trunk_slice.draw()
    if hit:
        trunk_base.draw()
        trunk.draw()
        if not collision:
            lumberjack_hit.draw()
        else:
            gravestone.draw()
    else:
        wood.draw()
        if not collision:
            lumberjack_ready.draw()
        else:
            gravestone.draw()

    for cloud in clouds:
        cloud.draw()

    for branch in branches.draw_branch():
        branch.draw()

    if collision:
        if is_fullscreen():
            screen.draw.text("Zgnieciony", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0]/2, screen.surface.get_size()[1]/2), align="center", fontname="bungee-regular", fontsize=128)
            screen.draw.text(f'Wynik: {score}', color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0]/2, (screen.surface.get_size()[1]/2)+120), align="center", fontname="bungee-regular", fontsize=64)
        else:
            screen.draw.text("Zgnieciony", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0]/2, screen.surface.get_size()[1]/2), align="center", fontname="bungee-regular", fontsize=64)
            screen.draw.text(f'Wynik: {score}', color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0]/2, (screen.surface.get_size()[1]/2)+50), align="center", fontname="bungee-regular", fontsize=32)
    elif endgame:
        if is_fullscreen():
            screen.draw.text("Koniec czasu", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0]/2, screen.surface.get_size()[1]/2), align="center", fontname="bungee-regular", fontsize=128)
            screen.draw.text(f'Wynik: {score}', color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0]/2, (screen.surface.get_size()[1]/2)+120), align="center", fontname="bungee-regular", fontsize=64)
        else:
            screen.draw.text("Koniec czasu", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0]/2, screen.surface.get_size()[1]/2), align="center", fontname="bungee-regular", fontsize=64)
            screen.draw.text(f'Wynik: {score}', color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0]/2, (screen.surface.get_size()[1]/2)+50), align="center", fontname="bungee-regular", fontsize=32)
    else:
        length = 10 * time_left
        if is_fullscreen():
            screen.draw.text(f'Wynik: {score}', color=ORANGE, center=(120, 30), align="right", fontname="bungee-regular",fontsize=40)
            screen.draw.text('Czas:', color=ORANGE, center=(80, 70), align="right", fontname="bungee-regular",fontsize=40)
            screen.draw.filled_rect(Rect(160, 50, length, 40), RED)
        else:
            screen.draw.text(f'Wynik: {score}', color=ORANGE, center=(60, 20), align="right", fontname="bungee-regular", fontsize=20)
            screen.draw.text('Czas:', color=ORANGE, center=(40, 50), align="right", fontname="bungee-regular", fontsize=20)
            screen.draw.filled_rect(Rect(80, 40, length, 20), RED)



pgzrun.go()
