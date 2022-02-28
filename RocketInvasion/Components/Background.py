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

    def move_up(self, amount):

        if self.curr_y - amount > self.x:
            self.curr_y -= amount
            self.engine.move_up(amount)

    def move_down(self, amount):

        if self.curr_y + amount < self.y+self.h:
            self.curr_y += amount
            self.engine.move_down(amount)

    def move_left(self, amount):

        if self.curr_x - amount > self.x:
            self.curr_x -= amount
            self.engine.move_left(amount)

    def move_right(self, amount):

        if self.curr_x + amount < self.x+self.w:
            self.curr_x += amount
            self.engine.move_right(amount)

    def act(self):

        #method for acting
        self.engine.act()

    def draw(self, screen):

        screen.fill(BLACK)
        self.engine.draw(screen)
