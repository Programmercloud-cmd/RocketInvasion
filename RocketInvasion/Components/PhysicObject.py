"""
PhysicObject superclass of all objects
"""
from abc import ABC, abstractmethod

class PhysicObject(ABC):

    def __init__(self, x, y, w, h):

        self.x, self.y, self.w, self.h = x, y, w, h
        self.x_vel = self.y_vel = 0

    @abstractmethod
    def draw(self, screen):
        pass

    #method for acting
    def act(self):

        #TODO
        pass
