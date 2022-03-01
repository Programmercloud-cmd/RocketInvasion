"""
PhysicObject superclass of all objects
"""
from abc import ABC, abstractmethod

class PhysicObject(ABC):

    def __init__(self, x, y, z, w, h):

        self.x, self.y, self.w, self.h = x, y, w, h
        self.z = z
        self.x_vel = self.y_vel = 0

    @abstractmethod
    def draw(self, screen):
        pass

    def move_horizontally(self, amount):

        self.x += amount

    def move_vertically(self, amount):

        self.y += amount

    #method for acting
    def act(self):

        #TODO
        self.x += self.x_vel
        self.y += self.y_vel

        self.x_vel = 0
        self.y_vel = 0
