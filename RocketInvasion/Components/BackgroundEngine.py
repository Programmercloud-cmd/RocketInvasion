"""
background engine for game
"""
from Components.Star import *
import random

class BackgroundEngine:

    def __init__(self, x, y, w, h):

        self.x, self.y, self.w, self.h = x, y, w, h

        #layers for background
        self.layer_1 = []
        self.layer_2 = []
        self.layer_3 = []

        self.spawn() #spawning objects

    def act(self):

        #acting for all objects

        for el in self.layer_1:
            el.act()
        for el in self.layer_2:
            el.act()
        for el in self.layer_3:
            el.act()

    def spawn(self):
        """
        spawns objects in 3 layers
        """

        #layer 1
        layer_1_object_count = int((self.w*self.h)/6400)

        for _ in range(layer_1_object_count):

            self.layer_1.append(Star(random.randrange(self.x, self.x+self.w), random.randrange(self.y, self.y+self.h),
                                random.randrange(1, 2), 0)
            )

    def move_up(self, amount):

        #layering objects
        for el in self.layer_1:
            el.move_up(amount)



    def move_down(self, amount):

        for el in self.layer_1:
            el.move_down(amount)

    def move_left(self, amount):

        for el in self.layer_1:
            el.move_left(amount)

    def move_right(self, amount):

        for el in self.layer_1:
            el.move_right(amount)


    def draw(self, screen):
        #drawing all objects

        for el in self.layer_1:

            el.draw(screen)
