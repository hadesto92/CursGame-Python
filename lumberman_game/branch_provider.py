import random

from static import HEIGHT, WIDTH, BASE_HEIGHT, BASE_WIDTH, lumberjack_ready
from pgzero.builtins import Actor
from utilis import scale, scale_to

class BranchProvider:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = self.screen.surface.get_size()[0]
        self.screen_height = self.screen.surface.get_size()[1]
        self.top = 0
        self.tree = []
        self.create_tree(30)

    def scale_branch(self, BASE, Out, bood_scale=False):
        for branch in self.tree:
            if branch is None:
                continue
            else:
                scale(branch[0], BASE, Out, bood_scale)

    def create_place_branch_on_tree(self, branch):
        self.screen_height = self.screen.surface.get_size()[1]

        start_point = (33 / 60) * self.screen_height
        up = (15 / 60) * self.screen_height

        self.top = start_point - len(self.tree) * up

        branch.y = self.top

    def create_branch(self, first=True):
        rand = random.randint(0,5)

        branch_scale_left = 369 / 800
        branch_scale_right = 432 / 800

        branch_left_unused = Actor('konar_lewy')

        if rand == 0 or rand == 3:
            branch = Actor('konar_lewy', pos=(branch_scale_left*WIDTH, -100), anchor=(branch_left_unused.width, 0)), 'left'
            self.create_place_branch_on_tree(branch[0])
        elif rand == 1 or rand == 4:
            branch = Actor('konar_prawy', pos=(branch_scale_right*WIDTH, -100), anchor=(0, 0)), 'left'
            self.create_place_branch_on_tree(branch[0])
        else:
            branch = None

        return branch

    def create_tree(self, number_branch):
        for _ in range(0, number_branch):
            self.tree.append(self.create_branch())


    def draw_branch(self):
        branches = []

        for branch in self.tree:
            if branch is None:
                continue
            else:
                branches.append(branch[0])

        return branches

    def find_pos_branch(self, direction):
        for branch in self.tree:
            if branch is None:
                continue
            else:
                if direction == 'left' and branch[1] == direction:
                    return branch[0].pos
                elif direction == 'right' and branch[1] == direction:
                    return branch[0].pos

    def find_anchor_branch(self, direction):
        for branch in self.tree:
            if branch is None:
                continue
            else:
                if direction == 'left' and branch[1] == direction:
                    return branch[0].anchor
                elif direction == 'right' and branch[1] == direction:
                    return branch[0].anchor



    def hit_tree(self):
        self.screen_height = self.screen.surface.get_size()[1]
        flage = 0
        print('..........................................................................................')
        for branch in self.tree:
            if branch is not None:
                if branch[0].y+((15/60)*self.screen_height) > lumberjack_ready.pos[1]-lumberjack_ready.height:
                    print('True')
                    print('Branch y [', flage, '] = ', branch[0].y + ((15 / 60) * self.screen_height),', lumberjack y: ', lumberjack_ready.pos[1]-lumberjack_ready.height)
                    #self.check_branch_end(branch, flage)
                else:
                    print('False')
                    print('Branch y [', flage, '] = ', branch[0].y + ((15 / 60) * self.screen_height),', lumberjack y: ', lumberjack_ready.pos[1]-lumberjack_ready.height)
                    branch[0].y += (15/60) * self.screen_height
            flage+=1
