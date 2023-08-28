GOLD = 255, 215, 0
RED = 255, 0, 0

class BestPlayers:
    def __init__(self, screen):
        self.screen = screen
        self.best_player = []
        self.score = 0
        self.name = ''
        self.new_player_color = RED
        with open('best.txt', 'r') as file:
            for line in file:
                if len(line) < 2:
                    continue
                splitted_line = line.split()
                self.best_player.append((splitted_line[0], int(splitted_line[1])))

    def set_score(self, score):
        self.score = score

    def exit(self):
        self.best_player.append((self.name, self.score))
        self.best_player.sort(key=lambda x: -x[1])
        if len(self.best_player) > 10:
            self.best_player.pop()

        lines = []
        for name, score in self.best_player:
            lines.append(f'{name} {score}\n')
        with open('best.txt', 'w') as file:
            file.writelines(lines)

    def change_color(self):
        if self.new_player_color == RED:
            self.new_player_color = GOLD
            return 'ok'
        else:
            self.exit()
            return 'exit'

    def append_to_name(self, key):
        if key.name == 'BACKSPACE' and self.name:
            self.name = self.name[:-1]
        elif key.name[:2] == 'K_':
            self.name += key.name[-1]
        elif len(key.name) == 1:
            self.name += key.name

    def draw(self):
        better_than = len(self.best_player)
        for i, line in enumerate(self.best_player):
            name, score = line
            if score < self.score:
                better_than = i
                break
            self.screen.draw.text(f'{name}', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=(100, 100+40*i), owidth = 1, ocolor=(100, 100, 100))
            self.screen.draw.text(f'{score}', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=(400, 100 + 40 * i), owidth=1, ocolor=(100, 100, 100))

        if not self.name:
            self.screen.draw.text(f'_', color=self.new_player_color, fontsize=32, fontname='bungee-regular', topleft=(100, 100+40*better_than), owidth = 1, ocolor=(100, 100, 100))
        else:
            self.screen.draw.text(f'{self.name}', color=self.new_player_color, fontsize=32, fontname='bungee-regular', topleft=(100, 100 + 40 * better_than), owidth=1, ocolor=(100, 100, 100))
        self.screen.draw.text(f'{self.score}', color=self.new_player_color, fontsize=32, fontname='bungee-regular', topleft=(400, 100 + 40 * better_than), owidth=1, ocolor=(100, 100, 100))

        for i, line in enumerate(self.best_player[better_than:]):
            name, score = line
            self.screen.draw.text(f'{name}', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=(100, 100 + 40 * (i+better_than+1)), owidth=1, ocolor=(100, 100, 100))
            self.screen.draw.text(f'{score}', color=GOLD, fontsize=32, fontname='bungee-regular', topleft=(400, 100 + 40 * (i+better_than+1)), owidth=1, ocolor=(100, 100, 100))
