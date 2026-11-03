import pygame
import hitboxes
import sprites
from Settings import *



# set direction
direction = 'down'

# starting coords
player_x, player_y = PLAYER_START_X, PLAYER_START_Y

# whether idling or not
idling = True

frame = 0
frame_counter = 0

def draw(surface,frame):
    # CUT your sprite selection and blitting lines from main.py and PASTE them here:
    if not idling:
        if direction == "left":
            current_image = sprites.left_run[frame]
        elif direction == "right":
            current_image = sprites.right_run[frame]
        elif direction == "up":
            current_image = sprites.up_run[frame]
        elif direction == "down":
            current_image = sprites.down_run[frame]
    else:
        if direction == "left":
            current_image = sprites.left_idle[frame]
        elif direction == "right":
            current_image = sprites.right_idle[frame]
        elif direction == "up":
            current_image = sprites.up_idle[frame]
        elif direction == "down":
            current_image = sprites.down_idle[frame]

    surface.blit(current_image, (player_x, player_y))
