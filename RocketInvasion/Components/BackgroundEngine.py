"""
background engine for game
"""
from Components.Star import *
import random

class BackgroundEngine:

    def __init__(self, x, y, w, h, screen_w, screen_h):

        self.x, self.y, self.w, self.h = x, y, w, h
        self.screen_w, self.screen_h = screen_w, screen_h
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
        layer_1_object_count = 100

        for _ in range(layer_1_object_count):

            self.layer_1.append(Star(random.randrange(self.x, self.x+self.w), random.randrange(self.y, self.y+self.h),
                                random.randrange(1, 4), 0)
            )

    def move_in(self, amount):

        for el in self.layer_1:

            el.w += (el.w*amount/10)

            el.x += (el.x-(self.screen_w/2))*amount
            el.y += (el.y-(self.screen_h/2))*amount


        for el in self.layer_1:

            if (el.x+el.w < 0) or (el.x > self.screen_w) or (el.y > self.screen_h) or (el.y+el.h < 0):

                self.layer_1.pop(self.layer_1.index(el))
                self.layer_1.append(Star(random.randrange(0, self.screen_w), random.randrange(0, self.screen_h),
                                    random.randrange(1, 4), 0)
                )

    def move_out(self, amount):

        for el in self.layer_1:

            el.w -= (el.w*amount/1)

            el.x -= (el.x-(self.screen_w/2))*amount
            el.y -= (el.y-(self.screen_h/2))*amount


        for el in self.layer_1:

            if el.w < 0.1:

                self.layer_1.pop(self.layer_1.index(el))
                self.layer_1.append(Star(random.randrange(0, self.screen_w), random.randrange(0, self.screen_h),
                                    random.randrange(1, 4), 0)
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
