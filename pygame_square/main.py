import time
import pygame
import random

#Zainicjowanie startu gry
pygame.init()
pygame.font.init()

#Ustawienie czcionki
myFont = pygame.font.SysFont('Tahoma', 50)

#Ustawienie wielkości okienka
screen_x = 800
screen_y = 600
screen = pygame.display.set_mode((screen_x, screen_y))

#Załadowanie obrazka do obiektu (zmiennej)
cloud = pygame.image.load('chmurka_01.png')
#Położenie obrazka chmurki
cloud_x, cloud_y = 0, 0
#Kolor czarny
BLACK = 0, 0, 0
#Kolor czerwony
RED = 255, 0, 0
#Kolor biały
WHITE = 255, 255, 255

#Miejsca losowe kwadracików
enemy_num = 10
rects = [[random.randint(20, 770), 0, True] for _ in range(enemy_num)]

#Ustawienie prędkości animacji poprzez zliczanie czasu
start = time.time()
delta = 0
speed_cloud = 100 #Przesunięcie o 100 px na jedno odświerzenie ekranu
speed_animation = 0

#Można przypisać prędkość animacji do FPS ale ograniczamy przez to słabe komputery ponieważ mogą nie wykręcić zadeklarowanych klatek lub ograniczać mocne komputery
#clock = pygame.time.Clock()

running = True
end_game = 0
#Pętla gry (nieskończona)
while running:
    #Ustawienie tła okienka na kolor czarny
    screen.fill(BLACK)

    #ZADARZENIA

    #Pętla wywołująca eventy aby sprawdzała co gracz robi na ekranie gry
    for event in pygame.event.get():
        #Jeśli gracz naciśnie X od okienka Windows gra ma się zakończyć (kończy nieskończoną pętlę)
        if event.type == pygame.QUIT:
            running = False
        #Wykrywanie zdarzenie pozycji myszki oraz czy został wciśnięty klawisz
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = event.pos[0], event.pos[1]
            hit = False
            #Porównanie pozycji myszki po kliknięciu z pozycją kwadracika jeśli są takie same jest "HIT"
            for rect in rects:
                if rect[0] <= pos_x <= rect[0] + 20 and rect[0] <= pos_x <= rect[0] + 20:
                    rect[2]=False
                    enemy_num-=1
                    break

    #LOGIKA

    #Obsługa klikniętych kwadracików
    if enemy_num <= 0:
        textsurface = myFont.render('WIN', True, WHITE)
        screen.blit(textsurface, (screen_x/2, screen_y/2))
        end_game+=delta

    if enemy_num > 0:
        for rect in rects:
            if rect[1] > 600:
                textsurface = myFont.render('GAME OVER', True, WHITE)
                screen.blit(textsurface,(screen_x/2, screen_y/2))
                end_game+=delta

    #Umieszczenie obrazka na ekranie
    speed_animation = speed_cloud * delta
    screen.blit(cloud, (cloud_x,cloud_y))
    cloud_x += speed_animation
    #Dla clock:
    #cloud_x += 1

    for rect in rects:
        if rect[2]==True:
            pygame.draw.rect(screen, RED, (rect[0], rect[1], 20, 20))
            rect[0] += random.randint(-1, 1)*speed_animation
            if(rect[0] >= 770):
                rect[0] -= 1*speed_animation
            if(rect[0] <= 20):
                rect[0] += 1*speed_animation
            rect[1] += speed_animation

    #Zakończenie gry

    if end_game>15:
        running = False

    #UPDATE

    #Zmierzenie czasu wykonywania pętli który będzie zmienną aby przemnorzyć prędkość animacji
    stop = time.time()
    delta = stop - start
    start = stop

    #Jeśli korzystamy z clock zamiast delta
    #clock.tick(60) #Ustawienie 60 FPS

    #Wyświetlenie okienka ustawionego wcześniej w pętli nieskończonej
    pygame.display.update()

#Inicjacja zakończenia gry
pygame.quit()