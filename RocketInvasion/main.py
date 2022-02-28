"""

RocketInvasion

-Version: 1.0
-Date:    28.2.2022
-Authors: @pycppdel, @thassi-droid
"""

#import sector
import pygame
from pygame.locals import *
from stdafx import *

pygame.init()

joysticks = []

for i in range(pygame.joystick.get_count()):

    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()



screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

BACKGROUND_ENGINE = Background(BACKGROUND_SPAWN_X, BACKGROUND_SPAWN_Y, BACKGROUND_WIDTH, BACKGROUND_HEIGHT, WIDTH, HEIGHT)


moving_right = False
moving_left = False

moving_up = False
moving_down = False

factor = 1


x_vel = 0

def redraw():

    BACKGROUND_ENGINE.act()
    BACKGROUND_ENGINE.draw(screen)


    pygame.display.flip()

quit = False

while not quit:

    keys = pygame.key.get_pressed()

    pressed = pygame.mouse.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            quit = True

        if event.type == JOYAXISMOTION:

            if event.axis == 0:

                if event.value > 0.1:
                    moving_right = True
                    moving_left = False
                    x_vel = int(event.value*factor)

                if event.value < 0.1:

                    moving_left = True
                    moving_right = False
                    x_vel = int(event.value*factor)

            elif event.axis == 1:

                if event.value > 0.1:
                    moving_up = True
                    moving_down = False
                    y_vel = int(event.value*factor)

                if event.value < 0.1:

                    moving_down = True
                    moving_up = False
                    y_vel = int(event.value*factor)

    if moving_left or moving_right:
        BACKGROUND_ENGINE.move_left(x_vel)
        BACKGROUND_ENGINE.move_up(y_vel)

    redraw()


pygame.quit()
