import pygame.transform
from pgzero.builtins import Actor

#Funkcja odpowiedzialna za skalowanie
def scale(self, old_size: tuple, new_size: tuple):
    #Tworzenie mnożnika który będzie skalował obecną rozdzielczość do nowej rozdzielczości
    multipler_x = new_size[0]/old_size[0]
    multipler_y = new_size[1]/old_size[1]

    #Nadanie nowej pozycji
    multipler_pos = self.pos[0]/old_size[0]
    new_pos = new_size[0]*multipler_pos, self.pos[1]

    print('Pozycja początkowa',self.pos)
    print('Nowa pozycja',new_pos)

    #Tworzenie nowego obiektu który zastąpi stary posiadając tą samą pozycję o nowej skali
    new_actor = Actor(self.image, pos=new_pos, anchor=self.anchor)
    new_width = int(self.width * multipler_x)
    new_height = int(self.height * multipler_y)

    self._surf = pygame.transform.scale(new_actor._surf, (new_width, new_height))
    self._update_pos()

#Funkcja odpowiedzialna za przeskalowanie wsystkich obiektów
def scale_to(object: list, old, new):
    for obj in object:
        scale(obj, old, new)