"""
class for weapons
"""

from Components.PhysicObject import *

class Weapon(PhysicObject):

    #cooldown in ms

    def __init__(self, x, y, w, h, damage=0, left_path=None, right_path=None, range=800,
                 cooldown=400):

        super().__init__(x, y, w, h)

        self.left_image = (pygame.image.load(left_path) if left_path is not None else None)
        self.right_image = (pygame.image.load(right_path) if right_path is not None else None)

        self.damage = damage
        self.range = range

        self.cooldown = cooldown

    def draw(self, screen):

        if self.left_image is not None:

            screen.blit(self.left_image, (self.x, self.y))

        if self.right_image is not None:

            screen.blit(self.right_image, (self.x+self.w, self.y))





class Default_Gun(Weapon):

    def __init__(self):

        super().__init__(0, 0, 0, 0, 250, None, None, 800, 400)
