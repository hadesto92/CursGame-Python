from static import *
from utilis import scale_to
from typing import Optional
from bee_behaviour import BeeAnimation
from pgzero.game import PGZeroGame

scale_to(SCALABLE, (BASE_WIDTH, BASE_HEIGHT), (WIDTH, HEIGHT))

bee_anim: Optional[BeeAnimation] = None

#Zmiana rozdzielczości ekranu za pomocą klawisza F z pełnoekranowego na okienkowy lub odwrtonie
def on_key_down(key):
    if key == keys.F:
        if is_fullscreen():
            surface_size = screen.surface.get_size()
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            scale_to(SCALABLE, surface_size, (WIDTH, HEIGHT), True)
        else:
            surface_size = screen.surface.get_size()
            screen.surface = pygame.display.set_mode((FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT), pygame.FULLSCREEN)
            scale_to(SCALABLE, surface_size, (FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT), True)
        change_fullscreen()
        bee_anim.set_screen(screen)
        bee_anim.reset_animation()

def update():
    global bee_anim
    if not bee_anim:
        bee_anim = BeeAnimation(screen)
        bee_anim.animate_bee()

    screen_width = screen.surface.get_size()[0]
    for i, cloud in enumerate(clouds):
        cloud.x += cloud_speed[i]*(screen_width/BASE_WIDTH)
        if cloud.x > screen_width:
            cloud.x = -cloud.width

def draw():
    screen.fill(BLACK)
    backgraound.draw()
    bee.draw()
    trunk.draw()
    print("Trunk pos: ", trunk.pos, ", trunk anchor: ", trunk.anchor, "Wielkość ekranu: ", screen.width, ' ' ,screen.height)
    for cloud in clouds:
        cloud.draw()

pgzrun.go()