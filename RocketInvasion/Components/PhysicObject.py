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

    def move_up(self, amount):

        self.y_vel -= amount

    def move_down(self, amount):

        self.y_vel += amount

    def move_left(self, amount):

        self.x_vel -= amount

    def move_right(self, amount):

        self.x_vel += amount

    #method for acting
    def act(self):

        #TODO
        self.x += self.x_vel
        self.y += self.y_vel

        self.x_vel = 0
        self.y_vel = 0
