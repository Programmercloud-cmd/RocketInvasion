"""
Ship class
"""

from Components.PhysicObject import *
from Components.Weapon import *

class Ship(PhysicObject):

    """
    standard first-person ship
    """

    def __init__(self, arsenal=[Default_Gun], speed=100, hp=1000, background_pointer):

        self.arsenal = arsenal
        self.speed = speed
        self.hp = hp

        self.background_pointer = background_pointer

    def move_horizontally(self, amount):

        self.background_pointer.move_horizontally(amount)

    def move_vertically(self, amount):

        self.background_pointer.move_vertically(amount)


class X_Wing(Ship):

    """
    First standard ship
    """
    def __init__(self, background_pointer):

        super().__init__(

        [Default_Gun],
        100,
        1000,
        background_pointer

        )
