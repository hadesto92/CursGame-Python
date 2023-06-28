from pgzero.builtins import animate
from static import bee
from random import uniform, randint

class BeeAnimation:
    def __init__(self, screen):
        self.screen = screen
        self.first_animation = True
        self.overflow = 200
        self.last_animation_x = None

    @staticmethod
    def get_speed():
        return uniform(3, 20)

    def set_screen(self, screen):
        self.screen = screen

    def animate_bee(self):
        bee.y = randint(100, self.screen.surface.get_size()[1] - 100)
        screen_width = self.screen.surface.get_size()[0]
        if self.first_animation:
            animate(bee, duration=3, on_finished=self.animate_bee, pos=(-2*self.overflow, bee.y))
            self.last_animation_x = -2*self.overflow
            self.first_animation = False
        speed = self.get_speed()
        if bee.x < -self.overflow:
            animate(bee, duration=speed, on_finished=self.animate_bee, pos=(screen_width+2*self.overflow, bee.y))
            self.last_animation_x = screen_width+2*self.overflow
        if bee.x > screen_width+2*self.overflow:
            animate(bee, duration=speed, on_finished=self.animate_bee, pos=(-2*self.overflow, bee.y))
            self.last_animation_x = -2*self.overflow

    def reset_animation(self):
        speed = self.get_speed()
        left = None
        if left:
            animate(bee, duration=speed, on_finished=self.animate_bee, pos=())
        else:
            animate(bee, duration=speed, on_finished=self.animate_bee, pos=())