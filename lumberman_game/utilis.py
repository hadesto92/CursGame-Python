import pygame.transform
from pgzero.builtins import Actor

#Funkcja odpowiedzialna za skalowanie
def scale(self, old_size: tuple, new_size: tuple, is_pos_anchor_scale = False):
    #Tworzenie mnożnika który będzie skalował obecną rozdzielczość do nowej rozdzielczości
    multipler_size = new_size[0]/old_size[0], new_size[1]/old_size[1]
    new_width = int(self.width * multipler_size[0])
    new_height = int(self.height * multipler_size[1])

    #Procentowy mnożnik położenia obazka
    multipler_pos = self.pos[0]/old_size[0], self.pos[1]/old_size[1]
    new_pos = new_size[0]*multipler_pos[0], new_size[1]*multipler_pos[1]

    #Tworzenie nowego obiektu który zastąpi stary
    new_actor = Actor(self.image)

    #Skalowanie obrazka
    self._surf = pygame.transform.scale(new_actor._surf, (new_width, new_height))
    self._surf = pygame.transform.flip(self._surf, self._fliped_x, self._fliped_y)  # Sprawdza podczas skalowania czy nie trzeba obrucić obrazka
    if is_pos_anchor_scale:
        self.x = new_pos[0] #linijka odpowiedzialna za to aby obiekty zachowały swoje położenie na ekranie procentowo względem poprzedniego rozmieszczenia
        self.y = new_pos[1]

    #Funkcja która umożliwia odświerzenie danych o obrazku (bez niej skalowanie wygląda jak przybliżenie)
    self._update_pos()

#Funkcja odpowiedzialna za przeskalowanie wsystkich obiektów
def scale_to(object: list, old, new, is_pos_anchor_scale = False):
    for obj in object:
        scale(obj, old, new, is_pos_anchor_scale)

#Funkcja która obraca obrazek lustrzanie
def mirror_flip(self, flip_x, flip_y):
    #Aby utworzyć funkcję w bibliotece actor.py dodałem zmienne: _fliped_x = _fliped_y = False, dzięki temu wiem czy obrazek jest zwórcony w lewo, prawo, góra lub dół
    if flip_x:
        self._fliped_x = not self._fliped_x
    if flip_y:
        self._fliped_y = not self._fliped_y
    self._surf = pygame.transform.flip(self._surf, flip_x, flip_y)
