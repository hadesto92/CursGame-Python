import random

from static import HEIGHT, WIDTH, BASE_HEIGHT, BASE_WIDTH
from pgzero.builtins import Actor
from utilis import scale_to

class BranchProvider:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = self.screen.surface.get_size()[0]
        self.screen_height = self.screen.surface.get_size()[1]
        self.branch_count = 20
        self.left_branch = [self.create_branch() for _ in range(self.branch_count)]
        self.right_branch = [self.create_branch(left=False) for _ in range(self.branch_count)]
        scale_to(self.all_branches(), (BASE_WIDTH, BASE_HEIGHT), (WIDTH, HEIGHT))
        self.branches_in_game = []
        self.last_taken_left = 0
        self.last_taken_right = 0
        self.top = 0
        self.create_in_game()

    def all_branches(self):
        return self.left_branch + self.right_branch

    def create_in_game(self):
        start_point = (33/60)*self.screen_height
        up = (15/60)*self.screen_height

        for _ in range(self.branch_count):
            rand = random.randint(0, 2)
            if rand == 0:
                self.branches_in_game.append(None)
            elif rand == 1:
                self.branches_in_game.append((self.left_branch[self.last_taken_left], 'left'))
                self.last_taken_left+=1
            elif rand == 2:
                self.branches_in_game.append((self.right_branch[self.last_taken_left], 'right'))
                self.last_taken_right+=1

        for i, branch in enumerate(self.branches_in_game):
            self.top = start_point - i*up
            if branch is None:
                continue
            else:
                branch[0].y = self.top

        self.top = start_point - len(self.branches_in_game)*up


    def create_branch(self, left=True):
        branch_scale_left = 369/800
        branch_scale_right = 432/800

        branch_left_unused = Actor('konar_lewy')

        if left:
            branch = Actor('konar_lewy', pos=(branch_scale_left*WIDTH, -100), anchor=(branch_left_unused.width, 0))
        else:
            branch = Actor('konar_prawy', pos=(branch_scale_right*WIDTH, -100), anchor=(0, 0))

        return branch

    def branches_to_draw(self):
        branches = []
        for branch in self.branches_in_game:
            if branch is None:
                continue
            else:
                branches.append(branch[0])
        return branches