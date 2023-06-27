import pgzrun
from pgzero.builtins import Actor, mouse, Rect
from pgzero.screen import Screen
import random
import sys
import time
screen: Screen

#Standardowo pygame zero nadaje rozmiar okna ale możemy go zmienić poprzez
WIDTH = 800
HEIGTH = 600

#Jako aktora podajemy obiekt chmurka
cloud = Actor('chmurka_01.png')

#Definiowanie koloru czarnego, czerwonego, białego
BLACK = 0, 0, 0
RED = 255, 0, 0
WHITE = 255, 255, 255

#Tworzenie kwadracików i losowanie ich miejsc na ekranie
enemy_num = 10 #liczba kwadracików
rects = [[Rect(random.randint(20, WIDTH-20), 0, 20, 20), True] for _ in range(enemy_num)] #Pozycja x, y; Wielkość x, y; Czy istnieje?

#Wyłączenie gry po 3 sekundach od momentu przegrania lub wygrania
start: float = 0
def close_game_after_seconds(now, time_to_close):
    global start
    if not start:
        start = now
    elif abs(start - now) > time_to_close:
      sys.exit(0)

#Logika gry
LOST = False

def on_mouse_down(pos, button):
    global enemy_num

    #Sprawdzenie czy kliknięty został lewy przycisk myszki
    if button != mouse.LEFT:
        return

    #Sprawdzenie czy położenie kwadracika zgadza się położeniem myszki po kliknięciu
    for rect in rects:
        if rect[0].x <= pos[0] <= rect[0].x + 20 and rect[0].y <= pos[1] <= rect[0].y + 20 and rect[1]:
            rect[1] = False
            enemy_num -= 1
            break


#Funkcja wbudowana słóżąca do aktualizacji informacji w grze
def update():
    global LOST

    #Przesunięcie chmurki o 1 px przez ... czas
    cloud.x += 1

    #Przesuwanie kwadracików
    for rect in rects:
        if not rect[1]:
            continue
        #Przesunięcie w lewo, prawo
        rect[0].x += random.randint(-1, 1)
        #Przesunięcie w dół
        rect[0].y += 1
        #Sprawdzenie czy kwadracik nie wyjechał za ekran
        if rect[0].x <= -1:
            rect[0].x += 1
        if rect[0].x >= WIDTH-20:
            rect[0].x -=1
        #Sprawdzenie czy kwadacik doszedł do końca
        if rect[0].y >= HEIGTH:
            LOST = True

#Funkcja wbudowana słóżąca do rysowania elementów na ekranie
def draw():
    #Rysowanie czarnego tła
    screen.fill(BLACK)
    #Rysowanie kwadracików
    for rect in rects:
        if rect[1]:
            screen.draw.filled_rect(rect[0], RED)
    #Rysowanie chmurki
    cloud.draw()
    #Wypisanie napisu "WYGRALES" po zakończeniu gry
    if enemy_num==0:
        screen.draw.text('Wygrałeś', (WIDTH/2, HEIGTH/2), color=WHITE, fontsize=50, sysfontname='Tahoma')
    #Wypisanie napisu "PRZEGRALES" po zakończeniu gry
    if LOST:
        screen.draw.text('Przegrałeś', (WIDTH/2, HEIGTH/2), color=WHITE, fontsize=50, sysfontname='Tahoma')
    #Wykonanie zdarzenia zamknięcia gry po przegraniej lub wygranej
    if enemy_num==0 or LOST:
        close_game_after_seconds(time.time(), 3)


pgzrun.go()