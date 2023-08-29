GOLD = 255, 215, 0
RED = 255, 0, 0


class Menu:
    def __init__(self, screen, width, height, mouse_pos):
        self.screen = screen
        self.width = width
        self.height = height
        self.mouse_pos = mouse_pos
        self.main_menu = True
        self.main_menu_pos = 0, 0
        self.play = False
        self.play_pos = 0, 0
        self.option = False
        self.option_pos = 0, 0
        self.description = False
        self.description_pos = 0, 0
        self.exit = False
        self.exit_pos = 0, 0
        self.highscore = False
        self.highscore_pos = 0, 0

    def main_menu(self):
        self.screen.draw.text(f'PLAY', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=(self.main_menu_pos[0], self.main_menu_pos[1]), owidth = 1, ocolor=(100, 100, 100))
        self.screen.draw.text(f'OPTION', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=(self.width/2, 100), owidth=1, ocolor=(100, 100, 100))
        self.screen.draw.text(f'HIGHSCORE', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=(self.width/2, 100), owidth=1, ocolor=(100, 100, 100))
        self.screen.draw.text(f'DESCRIPTION', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=(self.width/2, 100), owidth=1, ocolor=(100, 100, 100))
        self.screen.draw.text(f'EXIT', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=(self.width/2, 100), owidth=1, ocolor=(100, 100, 100))



    def option(self):
        pass

    def description(self):
        pass

    def exit(self):
        pass

    def highscore(self):
        pass