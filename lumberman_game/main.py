from static import *
from pgzero.game import PGZeroGame

#Zmiana rozdzielczości ekranu za pomocą klawisza F z pełnoekranowego na okienkowy lub odwrtonie
def on_key_down(key):
    if key == keys.F:
        if is_fullscreen():
            surface_size = screen.surface.get_size()
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        else:
            surface_size = screen.surface.get_size()
            screen.surface = pygame.display.set_mode((FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT), pygame.FULLSCREEN)
        change_fullscreen()


def draw():
    screen.fill(BLACK)
    backgraound.draw()

pgzrun.go()