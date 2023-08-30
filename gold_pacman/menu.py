from pgzero.builtins import Rect
from best_players import BestPlayers
from pygame import display
import sys

GOLD = 255, 215, 0
RED = 255, 0, 0
BLACK = 0, 0, 0
GREY = 100, 100, 100


class Menu:
    def __init__(self, screen, width, height, mouse_pos, mouse_clicked):
        self.screen = screen
        self.width = width
        self.height = height
        self.mouse_pos = mouse_pos
        self.mouse_clicked = mouse_clicked
        self.main_menu_bool = True
        self.play_bool = False
        self.play_pos = (width/2)-100, 150
        self.option_bool = False
        self.option_pos = (width/2)-100, 200
        self.description_bool = False
        self.description_pos = (width/2)-100, 300
        self.exit_pos = (width/2)-100, 350
        self.highscore_bool = False
        self.highscore_pos = (width/2)-100, 250
        self.best_player = BestPlayers(screen)

    def update(self, screen, width, height, mouse_pos, mouse_clicked):
        self.screen = screen
        self.width = width
        self.height = height
        self.mouse_pos = mouse_pos
        self.mouse_clicked = mouse_clicked

    def main_menu(self):
        if self.main_menu_bool:
            if self.play_pos[0] < self.mouse_pos[0] < self.play_pos[0]+95 and self.play_pos[1] < self.mouse_pos[1] < self.play_pos[1]+35:
                self.screen.draw.rect(Rect((self.play_pos), (95, 35)), RED)
                if self.mouse_clicked:
                    self.play_bool = True
                    self.main_menu_bool = False
            else:
                self.screen.draw.rect(Rect((self.play_pos), (95, 35)), BLACK)
            self.screen.draw.text(f'PLAY', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=(self.play_pos), owidth = 1, ocolor=GREY)


            if self.option_pos[0] < self.mouse_pos[0] < self.option_pos[0]+140 and self.option_pos[1] < self.mouse_pos[1] < self.option_pos[1]+35:
                self.screen.draw.rect(Rect((self.option_pos), (140, 35)), RED)
                if self.mouse_clicked:
                    self.option_bool = True
            else:
                self.screen.draw.rect(Rect((self.option_pos), (140, 35)), BLACK)
            self.screen.draw.text(f'OPTION', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=(self.option_pos), owidth=1, ocolor=GREY)


            if self.highscore_pos[0] < self.mouse_pos[0] < self.highscore_pos[0]+205 and self.highscore_pos[1] < self.mouse_pos[1] < self.highscore_pos[1]+35:
                self.screen.draw.rect(Rect((self.highscore_pos), (205, 35)), RED)
                if self.mouse_clicked:
                    self.highscore_bool = True
            else:
                self.screen.draw.rect(Rect((self.highscore_pos), (205, 35)), BLACK)
            self.screen.draw.text(f'HIGHSCORE', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=(self.highscore_pos), owidth=1, ocolor=GREY)


            if self.description_pos[0] < self.mouse_pos[0] < self.description_pos[0]+245 and self.description_pos[1] < self.mouse_pos[1] < self.description_pos[1]+35:
                self.screen.draw.rect(Rect((self.description_pos), (245, 35)), RED)
                if self.mouse_clicked:
                    self.description_bool = True
            else:
                self.screen.draw.rect(Rect((self.description_pos), (245, 35)), BLACK)
            self.screen.draw.text(f'DESCRIPTION', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=(self.description_pos), owidth=1, ocolor=GREY)


            if self.exit_pos[0] < self.mouse_pos[0] < self.exit_pos[0] + 95 and self.exit_pos[1] < self.mouse_pos[1] < self.exit_pos[1] + 35:
                self.screen.draw.rect(Rect((self.exit_pos), (95, 35)), RED)
                if self.mouse_clicked:
                    self.exit()
            else:
                self.screen.draw.rect(Rect((self.exit_pos), (95, 35)), BLACK)
            self.screen.draw.text(f'EXIT', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=(self.exit_pos), owidth=1, ocolor=GREY)
        else:
            self.main_menu_bool = True
            self.play_bool = False
            self.highscore_bool = False
            self.description_bool = False


    def option(self):
        self.main_menu_bool = False
        self.screen.draw.text(f'IN PROGRESS', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=((self.width/2-100), self.height/2), owidth=1, ocolor=GREY)

    def description(self):
        self.main_menu_bool = False
        self.screen.draw.text(f'IN PROGRESS', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=((self.width / 2 - 100), self.height / 2), owidth=1, ocolor=GREY)

    def exit(self):
        sys.exit()

    def highscore(self):
        self.main_menu_bool = False

        self.best_player.draw()
