"""
Direct class Star for drawing
"""

import pygame
from Components.SpaceObject import *

class Star(SpaceObject):

    """
    main class used for background
    """

    def __init__(self, x, y, z, w, h):
        super().__init__(x, y, z, w, h)

        self.factor = 1/800

    def draw(self, screen):



        if self.z > 0:

            pygame.draw.circle(screen, (0xFF, 0xFF, 0xFF), (round(self.x), round(self.y)), round(self.w*self.factor*self.z)+1)

        elif self.z == 0:

            pygame.draw.circle(screen, (0xFF, 0xFF, 0xFF), (round(self.x), round(self.y)), round(self.w)+1)
