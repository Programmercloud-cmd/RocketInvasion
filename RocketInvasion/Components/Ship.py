"""
Ship class
"""

from Components.PhysicObject import *
from Components.Weapon import *

from abc import ABC, abstractmethod

class Ship(ABC):

    """
    standard first-person ship
    """

    def __init__(self, background_pointer, arsenal=[Default_Gun], speed=100, hp=1000):

        self.arsenal = arsenal
        self.speed = speed
        self.hp = hp

        self.background_pointer = background_pointer

        self.current_weapon = arsenal[0]()

    def move_horizontally(self, amount):

        self.background_pointer.move_horizontally(amount)

    def move_vertically(self, amount):

        self.background_pointer.move_vertically(amount)

    @abstractmethod
    def draw(self, screen):
        pass


class X_Wing(Ship):

    """
    First standard ship
    """
    def __init__(self, background_pointer):

        super().__init__(

        background_pointer,
        [Default_Gun],
        100,
        1000,

        )

    def draw(self, screen):

        pass
