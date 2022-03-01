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

factor = 2


x_vel = 0
y_vel = 0


moving_forward = False
moving_backwards = False

max_speed = 0.01
move_factor = 0.0005
move_fast_factor = 2

f_vel = 0
b_vel = 0

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
        if event.type == JOYBUTTONDOWN:

            if event.button == 4:

                moving_backwards = False
                moving_forward = True

                f_vel = move_factor
                b_vel = 0

            if event.button == 5:

                moving_backwards = True
                moving_forward = False

                b_vel = move_factor
                f_vel = 0
            if event.button == 0:

                f_vel = b_vel = 0

            if event.button == 2:

                if f_vel < max_speed and b_vel < max_speed:
                    f_vel *= move_fast_factor
                    b_vel *= move_fast_factor

            if event.button == 1:

                f_vel /= move_fast_factor
                b_vel /= move_fast_factor

    if moving_left or moving_right:
        BACKGROUND_ENGINE.move_horizontally(x_vel)
        BACKGROUND_ENGINE.move_vertically(y_vel)


    BACKGROUND_ENGINE.engine.move_in(f_vel)
    BACKGROUND_ENGINE.engine.move_out(b_vel)
    redraw()


pygame.quit()
