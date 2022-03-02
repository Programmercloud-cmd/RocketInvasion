"""
class for items
"""
from Components.SpaceObject import *

class item(SpaceObject):

def __init__(self, x, y, z, w, h, path):

        super().__init__(x, y, z, w, h)

        self.image = (pygame.image.load(path) if path is not None else None)