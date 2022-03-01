"""
Background class for engine
"""
from Components.BackgroundEngine import *
from Components.colors import *

class Background:

    """
    class for drawing background
    """

    def __init__(self, x, y, w, h, screen_w, screen_h):

        self.x, self.y, self.w, self.h = x, y, w, h
        self.screen_w = screen_w
        self.screen_h = screen_h

        self.curr_x = 0
        self.curr_y = 0

        self.engine = BackgroundEngine(x, y, w, h, screen_w, screen_h)

    def move_horizontally(self, amount):

        self.x += amount
        self.engine.move_horizontally(amount)

    def move_vertically(self, amount):

        self.y += amount
        self.engine.move_vertically(amount)

    def act(self):

        #method for acting
        self.engine.act()

    def draw(self, screen):

        screen.fill(BLACK)
        self.engine.draw(screen)
