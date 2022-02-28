"""
Direct class Star for drawing
"""

import pygame
from Components.SpaceObject import *

class Star(SpaceObject):

    """
    main class used for background
    """

    def __init__(self, x, y, w, h):

        super().__init__(x, y, w, h)

    def draw(self, screen):

        pygame.draw.circle(screen, (0xFF, 0xFF, 0xFF), (round(self.x), round(self.y)), round(self.w))
