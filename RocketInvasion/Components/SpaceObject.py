"""
SpaceObject for instanciatable objects
"""
import sys
import os

from Components.PhysicObject import *


class SpaceObject(PhysicObject):

    def __init__(self, x, y, w, h):

        super().__init__(x, y, w, h)
