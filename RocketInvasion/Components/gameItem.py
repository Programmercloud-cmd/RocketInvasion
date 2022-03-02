"""
class for items
"""
from Components.SpaceObject import *

class gameItem(SpaceObject):

    def __init__(self, x, y, z, w, h, path):

        super().__init__(x, y, z, w, h)

        self.image = (pygame.image.load(path) if path is not None else None)

    def draw(self, screen):

        if self.image is not None:

            screen.blit(self.image, (self.x, self.y))




class decreasedCoolDown(gameItem):

    def __init__(self):

        super().__init__(0, 0, 0, 0, 0, None)

class healthPointBoost(gameItem):

    def __init__(self):

        super().__init__(0, 0, 0, 0, 0, None)

class damageBoost(gameItem):

    def __init__(self):

        super().__init__(0, 0, 0, 0, 0, None)

class temporaryTimeDilation(gameItem):

    def __init__(self):

        super().__init__(0, 0, 0, 0, 0, None)