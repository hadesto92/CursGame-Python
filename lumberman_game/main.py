import time

from static import *
from utilis import scale_to, mirror_flip, bring_back_position
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
score = 0
gravestone.x = lumberjack_hit.x-20
play_time_sound = False

temp_music = ['menu', 'play_game', 'end_game']

#Opcje w grze
start = True
key_bind = False
info = False
highscore = False
play = False
endgame = False
game_over = False
menu_sound = True
game_play_sound = False
end_game_sound = False
stop_music = False

music.set_volume(0.4)
music.play_once(temp_music[0])

def on_music_end():
    global temp_music, stop_music
    if stop_music:
        music.stop()
    else:
        if menu_sound:
            music.play_once(temp_music[0])
        elif game_play_sound:
            music.play_once(temp_music[1])
        elif end_game_sound:
            music.play_once(temp_music[2])
        else:
            pass

#Resetowanie gry
def reset():
    global score, time_left, last_time, collision, endgame, lumberjack_on_left, hit, play, start, key_bind, info, highscore, play, game_over, menu_sound, game_play_sound, end_game_sound

    collision = False
    time_left = 5
    last_time = 0
    endgame = False
    score = 0
    hit = False
    start = True
    key_bind = False
    info = False
    highscore = False
    play = False
    game_over = False
    menu_sound = True
    game_play_sound = False
    end_game_sound = False
    music.stop()
    if not lumberjack_on_left:
        mirror_flip(lumberjack_ready, True, False)
        mirror_flip(lumberjack_hit, True, False)
        lumberjack_on_left = True
        lumberjack_ready.x -= 3.44 * trunk.width
        lumberjack_hit.x -= 2 * trunk.width
        gravestone.x = lumberjack_hit.x - 20

def swich_pos_lumberman(is_left):
    global lumberjack_on_left

    if is_left:
        mirror_flip(lumberjack_ready, True, False)
        mirror_flip(lumberjack_hit, True, False)
        lumberjack_on_left = False
        lumberjack_ready.x += 3.44 * trunk.width
        lumberjack_hit.x += 2 * trunk.width
        gravestone.x = lumberjack_ready.x
    else:
        mirror_flip(lumberjack_ready, True, False)
        mirror_flip(lumberjack_hit, True, False)
        lumberjack_on_left = True
        lumberjack_ready.x -= 3.44 * trunk.width
        lumberjack_hit.x -= 2 * trunk.width
        gravestone.x = lumberjack_hit.x - 20

def score_system():
    global score, time_left, max_time, stop_music

    score += 1
    if time_left < max_time:
        if score < 1000:
            time_left += 2 / score + 0.3
        elif 1000 <= score < 2000:
            time_left += 2 / score + 0.25
        elif 2000 <= score < 4000:
            time_left += 2 / score + 0.2
        elif 4000 <= score < 8000:
            time_left += 2 / score + 0.15
        else:
            time_left += 2 / score + 0.11

        if score % 1000 == 0:
            if not stop_music:
                sounds.powerup.set_volume(0.3)
                sounds.powerup.play()
            if time_left + 5 <= max_time:
                time_left += 5
            else:
                time_left = max_time

def on_key_down():
    global hit, hit_time, lumberjack_on_left, collision, endgame, start, key_bind, info, highscore, play, game_over, menu_sound, game_play_sound, end_game_sound, stop_music

    if keyboard.RETURN:
        print(pygame.KEYDOWN)
        if not stop_music:
            sounds.start.set_volume(0.5)
            sounds.start.play()
        if start:
            start = False
            if not play:
                play = True
                menu_sound = False
                game_play_sound = True
                music.stop()
        else:
            if play:
                reset()

    if keyboard.F:
        if is_fullscreen():
            surface_size = screen.surface.get_size()
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            scale_to(SCALABLE + branches.left_branch + branches.right_branch, surface_size, (WIDTH, HEIGHT), True)

        else:
            surface_size = screen.surface.get_size()
            screen.surface = pygame.display.set_mode((FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT), pygame.FULLSCREEN)
            scale_to(SCALABLE + branches.left_branch + branches.right_branch, surface_size, (FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT), True)

        change_fullscreen()
        bee_anim.set_screen(screen)
        bee_anim.reset_animation()

    if keyboard.ESCAPE:
        if info or key_bind or highscore:
            info = False
            key_bind = False
            highscore = False
            start = True
        elif play and not game_over:
            reset()
        else:
            quit()

    if keyboard.M:
        if stop_music:
            stop_music = False
            on_music_end()
        else:
            stop_music = True
            on_music_end()

    if play:
        if not collision and not endgame:
            if keyboard.LEFT:
                animate(trunk_slice, on_finished=bring_back_position(trunk_slice, trunk_slice_old), duration=0.099, pos=(screen.surface.get_size()[0], screen.surface.get_size()[1]/2))
                if not lumberjack_on_left:
                    swich_pos_lumberman(False)

            if keyboard.RIGHT:
                animate(trunk_slice, on_finished=bring_back_position(trunk_slice, trunk_slice_old), duration=0.099, pos=(0, screen.surface.get_size()[1] / 2))
                if lumberjack_on_left:
                    swich_pos_lumberman(True)

            if keyboard.LEFT or keyboard.RIGHT:
                if not stop_music:
                    sounds.hit.set_volume(0.5)
                    sounds.hit.play()
                hit = True
                hit_time = time.time()
                collision = branches.collision_branch(lumberjack_on_left)
                if collision:
                    if not stop_music:
                        sounds.collision.set_volume(0.3)
                        sounds.collision.play()
                    game_over = True
                    game_play_sound = False
                    end_game_sound = True
                    music.stop()
                branches.hit_tree()
                score_system()
    else:
        if keyboard.O:
            if not key_bind:
                key_bind = True
                start = False
            else:
                key_bind = False
                start = True

        if keyboard.I:
            if not info:
                info = True
                start = False
            else:
                info = False
                start = True

        if keyboard.H:
            if not highscore:
                highscore = True
                start = False
            else:
                highscore = False
                start = True

def update():
    global bee_anim, hit, hit_time, branches, last_time, time_left, collision, endgame, play_time_sound, game_over, game_play_sound, end_game_sound, stop_music

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
    if play:
        now = time.time()
        if not last_time:
            last_time = now
        delta_time = now - last_time
        time_left -= delta_time
        last_time = now

        if time_left < 0 and not collision:
            time_left = 0
            endgame = True
            game_over = True
            if end_game_sound == False:
                if not stop_music:
                    sounds.time.set_volume(0.3)
                    sounds.time.play()
                game_play_sound = False
                end_game_sound = True
                music.stop()

def main_menu():
    if start:
        if is_fullscreen():
            screen.draw.text("LUMBERMAN GAME", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1] / 2) - 350), align="center", fontname="bungee-regular", fontsize=128)
            screen.draw.text("ENTER - rozpocznij", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, screen.surface.get_size()[1] / 2), align="center", fontname="bungee-regular", fontsize=64)
            screen.draw.text("O - opcje", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1]/2)+100), align="center", fontname="bungee-regular", fontsize=64)
            screen.draw.text("I - informacje", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1]/2)+200), align="center", fontname="bungee-regular", fontsize=64)
            screen.draw.text("H - wyniki", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1] / 2)+300), align="center", fontname="bungee-regular", fontsize=64)

        else:
            screen.draw.text("LUMBERMAN GAME", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1] / 2) - 150),  align="center", fontname="bungee-regular", fontsize=64)
            screen.draw.text("ENTER - rozpocznij", color=ORANGE, shadow=(1, 1),center=(screen.surface.get_size()[0] / 2, screen.surface.get_size()[1]/2), align="center", fontname="bungee-regular", fontsize=32)
            screen.draw.text("O - opcje", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1]/2)+50), align="center", fontname="bungee-regular", fontsize=32)
            screen.draw.text("I - informacje", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1]/2)+100), align="center", fontname="bungee-regular", fontsize=32)
            screen.draw.text("H - wyniki", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1] / 2)+150),  align="center", fontname="bungee-regular", fontsize=32)

def end_game():
    if game_over:
        if collision:
            if is_fullscreen():
                screen.draw.text("Zgnieciony", color=ORANGE, shadow=(1, 1),
                                 center=(screen.surface.get_size()[0] / 2, screen.surface.get_size()[1] / 2),
                                 align="center", fontname="bungee-regular", fontsize=128)
                screen.draw.text(f'Wynik: {score}', color=ORANGE, shadow=(1, 1),
                                 center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1] / 2) + 120),
                                 align="center", fontname="bungee-regular", fontsize=64)
                screen.draw.text("ENTER - menu", color=ORANGE, shadow=(1, 1),
                                 center=(screen.surface.get_size()[0] / 2, screen.surface.get_size()[1] / 2 + 200),
                                 align="center", fontname="bungee-regular", fontsize=64)
                screen.draw.text("ESC - wyjście", color=ORANGE, shadow=(1, 1),
                                 center=(screen.surface.get_size()[0] / 2, screen.surface.get_size()[1] / 2 + 280),
                                 align="center", fontname="bungee-regular", fontsize=64)
            else:
                screen.draw.text("Zgnieciony", color=ORANGE, shadow=(1, 1),
                                 center=(screen.surface.get_size()[0] / 2, screen.surface.get_size()[1] / 2),
                                 align="center", fontname="bungee-regular", fontsize=64)
                screen.draw.text(f'Wynik: {score}', color=ORANGE, shadow=(1, 1),
                                 center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1] / 2) + 50),
                                 align="center", fontname="bungee-regular", fontsize=32)
                screen.draw.text("ENTER - menu", color=ORANGE, shadow=(1, 1),
                                 center=(screen.surface.get_size()[0] / 2, screen.surface.get_size()[1] / 2 + 90),
                                 align="center", fontname="bungee-regular", fontsize=32)
                screen.draw.text("ESC - wyjście", color=ORANGE, shadow=(1, 1),
                                 center=(screen.surface.get_size()[0] / 2, screen.surface.get_size()[1] / 2 + 130),
                                 align="center", fontname="bungee-regular", fontsize=32)
        elif endgame:
            if is_fullscreen():
                screen.draw.text("Koniec czasu", color=ORANGE, shadow=(1, 1),
                                 center=(screen.surface.get_size()[0] / 2, screen.surface.get_size()[1] / 2),
                                 align="center", fontname="bungee-regular", fontsize=128)
                screen.draw.text(f'Wynik: {score}', color=ORANGE, shadow=(1, 1),
                                 center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1] / 2) + 120),
                                 align="center", fontname="bungee-regular", fontsize=64)
                screen.draw.text("Naciśnij ENTER aby zresetować", color=ORANGE, shadow=(1, 1),
                                 center=(screen.surface.get_size()[0] / 2, screen.surface.get_size()[1] / 2 + 200),
                                 align="center", fontname="bungee-regular", fontsize=64)
            else:
                screen.draw.text("Koniec czasu", color=ORANGE, shadow=(1, 1),
                                 center=(screen.surface.get_size()[0] / 2, screen.surface.get_size()[1] / 2),
                                 align="center", fontname="bungee-regular", fontsize=64)
                screen.draw.text(f'Wynik: {score}', color=ORANGE, shadow=(1, 1),
                                 center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1] / 2) + 50),
                                 align="center", fontname="bungee-regular", fontsize=32)
                screen.draw.text("Naciśnij ENTER aby zresetować", color=ORANGE, shadow=(1, 1),
                                 center=(screen.surface.get_size()[0] / 2, screen.surface.get_size()[1] / 2 + 90),
                                 align="center", fontname="bungee-regular", fontsize=32)

def option_menu():
    if key_bind:
        if is_fullscreen():
            screen.draw.text("OPCJE", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1] / 2) - 350), align="left", fontname="bungee-regular", fontsize=128)
            screen.draw.text("<- - UDERZENIE Z LEWEJ", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0]/2, (screen.surface.get_size()[1]/2)-100), align="left", fontname="bungee-regular", fontsize=64)
            screen.draw.text("-> - UDERZENIE Z PRAWEJ", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0]/2, screen.surface.get_size()[1]/2), align="left", fontname="bungee-regular", fontsize=64)
            screen.draw.text("F - PEŁNY EKRAN", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1]/2)+100), align="left", fontname="bungee-regular", fontsize=64)
            screen.draw.text("ESC - WYJŚCIE Z GRY/POWRÓT", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1]/2)+200), align="left", fontname="bungee-regular", fontsize=64)
        else:
            screen.draw.text("OPCJE", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1] / 2) - 150), align="left", fontname="bungee-regular", fontsize=64)
            screen.draw.text("<- - UDERZENIE Z LEWEJ", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0]/2, (screen.surface.get_size()[1]/2)-50), align="left", fontname="bungee-regular", fontsize=32)
            screen.draw.text("-> - UDERZENIE Z PRAWEJ", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0]/2, screen.surface.get_size()[1]/2), align="left", fontname="bungee-regular", fontsize=32)
            screen.draw.text("-> - UDERZENIE Z PRAWEJ", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1]/2+50)), align="left", fontname="bungee-regular", fontsize=32)
            screen.draw.text("ESC - WYJŚCIE Z GRY/POWRÓT", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0]/2, (screen.surface.get_size()[1]/2)+100), align="left", fontname="bungee-regular", fontsize=32)

def high_score():
    if highscore:
        if is_fullscreen():
            screen.draw.text("WYNIKI", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1]/2)-350), align="left", fontname="bungee-regular", fontsize=128)
        else:
            screen.draw.text("WYNIKI", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1]/2)-150), align="left", fontname="bungee-regular", fontsize=64)

def information_menu():
    if info:
        if is_fullscreen():
            screen.draw.text("INFORMACJE", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1] / 2) - 350), align="left", fontname="bungee-regular", fontsize=128)
            screen.draw.text("Autor: Karol 'Hadesto' Lach", color=ORANGE, shadow=(1, 1), center=((screen.surface.get_size()[0]/2), (screen.surface.get_size()[1] / 2)-100), align="left", fontname="bungee-regular", fontsize=64)
            screen.draw.text("Gra zaprojektowana na podstawie kursu.", color=ORANGE, shadow=(1, 1), center=((screen.surface.get_size()[0] / 2), (screen.surface.get_size()[1] / 2)+20), align="left", fontname="bungee-regular", fontsize=64)
        else:
            screen.draw.text("INFORMACJE", color=ORANGE, shadow=(1, 1), center=(screen.surface.get_size()[0] / 2, (screen.surface.get_size()[1] / 2) - 150), align="left", fontname="bungee-regular", fontsize=64)
            screen.draw.text("Autor: Karol 'Hadesto' Lach", color=ORANGE, shadow=(1, 1), center=((screen.surface.get_size()[0] / 2), (screen.surface.get_size()[1] / 2)-50), align="left", fontname="bungee-regular", fontsize=20)
            screen.draw.text("Gra zaprojektowana na podstawie kursu.", color=ORANGE, shadow=(1, 1), center=((screen.surface.get_size()[0] / 2), (screen.surface.get_size()[1] / 2)), align="left", fontname="bungee-regular", fontsize=20)

def game_play():
    screen.fill(BLACK)
    backgraound.draw()
    bee.draw()
    if hit:
        trunk_base.draw()
        trunk_slice.draw()
        trunk.draw()
        if play:
            if not collision:
                lumberjack_hit.draw()
            else:
                gravestone.draw()
    else:
        wood.draw()
        if play:
            if not collision:
                lumberjack_ready.draw()
            else:
                gravestone.draw()

    for cloud in clouds:
        cloud.draw()

    for branch in branches.draw_branch():
        branch.draw()

    if play:
        length = 10 * time_left
        if is_fullscreen():
            screen.draw.text(f'Wynik: {score}', color=ORANGE, center=(120, 30), align="right",
                             fontname="bungee-regular", fontsize=40)
            screen.draw.text('Czas:', color=ORANGE, center=(80, 70), align="right", fontname="bungee-regular",
                             fontsize=40)
            screen.draw.filled_rect(Rect(160, 50, length, 40), RED)
        else:
            screen.draw.text(f'Wynik: {score}', color=ORANGE, center=(60, 20), align="right",
                             fontname="bungee-regular", fontsize=20)
            screen.draw.text('Czas:', color=ORANGE, center=(40, 50), align="right", fontname="bungee-regular",
                             fontsize=20)
            screen.draw.filled_rect(Rect(80, 40, length, 20), RED)

def draw():
    global stop_music

    game_play()
    main_menu()
    end_game()
    information_menu()
    option_menu()
    high_score()

    if stop_music:
        stop_music_img.draw()

pgzrun.go()