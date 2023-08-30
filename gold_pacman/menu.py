from pgzero.builtins import Rect
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
        self.exit_bool = False
        self.exit_pos = (width/2)-100, 350
        self.highscore_bool = False
        self.highscore_pos = (width/2)-100, 250

    def main_menu(self):

        if self.play_pos[0] < self.mouse_pos[0] < self.play_pos[0]+95 and self.play_pos[1] < self.mouse_pos[1] < self.play_pos[1]+35:
            self.screen.draw.rect(Rect((self.play_pos), (95, 35)), RED)
            if self.mouse_clicked:
                print("PLAY")
        else:
            self.screen.draw.rect(Rect((self.play_pos), (95, 35)), BLACK)
        self.screen.draw.text(f'PLAY', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=(self.play_pos), owidth = 1, ocolor=GREY)


        if self.option_pos[0] < self.mouse_pos[0] < self.option_pos[0]+140 and self.option_pos[1] < self.mouse_pos[1] < self.option_pos[1]+35:
            self.screen.draw.rect(Rect((self.option_pos), (140, 35)), RED)
            if self.mouse_clicked:
                print("OPTION")
        else:
            self.screen.draw.rect(Rect((self.option_pos), (140, 35)), BLACK)
        self.screen.draw.text(f'OPTION', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=(self.option_pos), owidth=1, ocolor=GREY)


        if self.highscore_pos[0] < self.mouse_pos[0] < self.highscore_pos[0]+205 and self.highscore_pos[1] < self.mouse_pos[1] < self.highscore_pos[1]+35:
            self.screen.draw.rect(Rect((self.highscore_pos), (205, 35)), RED)
            if self.mouse_clicked:
                print("HIGHSCORE")
        else:
            self.screen.draw.rect(Rect((self.highscore_pos), (205, 35)), BLACK)
        self.screen.draw.text(f'HIGHSCORE', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=(self.highscore_pos), owidth=1, ocolor=GREY)


        if self.description_pos[0] < self.mouse_pos[0] < self.description_pos[0]+245 and self.description_pos[1] < self.mouse_pos[1] < self.description_pos[1]+35:
            self.screen.draw.rect(Rect((self.description_pos), (245, 35)), RED)
            if self.mouse_clicked:
                print("DESCRIPTIOPN")
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



    def option(self):
        pass

    def description(self):
        pass

    def exit(self):
        sys.exit()

    def highscore(self):
        pass