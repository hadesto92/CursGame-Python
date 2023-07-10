import random

from static import HEIGHT, WIDTH, BASE_HEIGHT, BASE_WIDTH, lumberjack_ready
from pgzero.builtins import Actor
from utilis import scale_to

class BranchProvider:
    def __init__(self, screen):
        self.screen = screen
        self.screen_height = self.screen.surface.get_size()[1]
        self.branch_count = 10
        self.left_branch = [self.create_branch() for _ in range(self.branch_count)]
        self.right_branch = [self.create_branch(False) for _ in range(self.branch_count)]
        scale_to(self.left_branch + self.right_branch, (BASE_WIDTH, BASE_HEIGHT), (WIDTH, HEIGHT))
        self.tree = []
        self.last_taken_left = 0
        self.last_taken_right = 0
        self.create_tree()

    def new_place(self):
        self.screen_height = self.screen.surface.get_size()[1]
        start_point = (33 / 60) * self.screen_height
        up = (15 / 60) * self.screen_height
        return start_point - len(self.tree) * up

    def create_branch(self, left=True):
        branch_scale_left = 369 / 800
        branch_scale_right = 432 / 800

        branch_left_unused = Actor('konar_lewy')

        if left:
            branch = Actor('konar_lewy', pos=(branch_scale_left*WIDTH, -100), anchor=(branch_left_unused.width, 0))
        else:
            branch = Actor('konar_prawy', pos=(branch_scale_right*WIDTH, -100), anchor=(0, 0))

        return branch

    def add_new_branch(self, first=False):
        rand = random.randint(0, 5)
        if rand == 0 or rand == 2:
            if first == False:
                if self.last_taken_left == self.branch_count:
                    self.last_taken_left = 0
                self.left_branch[self.last_taken_left].y = self.new_place()
            self.tree.append((self.left_branch[self.last_taken_left], 'left'))
            self.last_taken_left += 1
        elif rand == 1 or rand == 3:
            if first == False:
                if self.last_taken_right == self.branch_count:
                    self.last_taken_right = 0
                self.right_branch[self.last_taken_right].y = self.new_place()
            self.tree.append((self.right_branch[self.last_taken_right], 'right'))
            self.last_taken_right += 1
        else:
            self.tree.append(None)

    def create_tree(self):
        for _ in range(self.branch_count):
            self.add_new_branch(True)

        start_point = (33 / 60) * self.screen_height
        up = (15/60) * self.screen_height

        for i, branch in enumerate(self.tree):
            self.top = start_point - i * up
            if branch is None:
                continue
            else:
                branch[0].y = self.top

    def draw_branch(self):
        branches = []
        for branch in self.tree:
            if branch is not None:
                branches.append(branch[0])
        return branches

    def collision_branch(self, lumberjack_direction):
        if self.tree[0] is not None:
            if self.tree[0][1] == 'left' and lumberjack_direction == True:
                return True
            elif self.tree[0][1] == 'right' and lumberjack_direction == False:
                return True
            else:
                return False
        return False


    def hit_tree(self):
        self.screen_height = self.screen.surface.get_size()[1]
        self.add_new_branch()
        for branch in self.tree:
            if branch is not None:
                branch[0].y += (15 / 60) * self.screen_height
        self.tree.pop(0)

