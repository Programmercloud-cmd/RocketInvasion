"""
class for obstacles
"""

import random

from Components.SpaceObject import *

class obstacle(SpaceObject):

    def __init__(self, x, y, z, w, h, path = None, health = None):

        super().__init__(x, y, z, w, h)

        self.image = (pygame.image.load(path) if path is not None else None)

    def draw(self, screen):

        if self.image is not None:

            screen.blit(self.image, (self.x, self.y))



class meteoroid(obstacle):

    hpStartMeteoroid = 500 #increase with time --> timer
    hpLimitMeteoroid = 750

    def __init__(self):

            super().__init__(0, 0, 0, 0, 0, None, random.randint(hpStartMeteoroid, hpLimitMeteoroid)

class spaceTrash(obstacle):

    hpStartSpaceTrash = 750 #increase with time --> timer
    hpLimitSpaceTrash = 1000

    def __init__(self):

            super().__init__(0, 0, 0, 0, 0, None, random.randint(hpStartSpaceTrash, )