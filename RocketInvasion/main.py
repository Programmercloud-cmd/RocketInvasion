"""

RocketInvasion

-Version: 1.0
-Date:    28.2.2022
-Authors: @pycppdel, @thassi-droid
"""

#import sector
import pygame
from stdafx import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def redraw():

    screen.fill((0, 0, 0))

    pygame.display.flip()

quit = False

while not quit:

    pressed = pygame.mouse.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            quit = True

    redraw()

    if pressed[0]:

        quit = True

pygame.quit()
