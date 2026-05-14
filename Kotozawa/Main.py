import pygame
import sys
import map
import objects
from variables import *
import random

def display_floor():
    x = 0
    y = 0
    for row in map.grid:
        for item in row:
            if item == 1:
                if map.randomlist[int(y/tile_width)][int(x/tile_width)] == 0:
                    screen.blit(objects.grass1_tile,(x,y))
                else:
                    screen.blit(objects.grass2_tile, (x,y))
            elif item == 0:
                screen.blit(objects.path_tile, (x,y))
            x += tile_width
        x = 0
        y += tile_width

pygame.init()
pygame.display.set_caption('Kotozawa  |  ことわざ')
screen = pygame.display.set_mode((1250, 700), pygame.RESIZABLE)
clock = pygame.time.Clock()

#event loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #bind escape to close
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    #key binding for movement of sprite and map movement
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        ...
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        ...
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        ...
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        ...

    display_floor()
    screen.blit(objects.house_front,(407,270))
    screen.blit(objects.shop_front,(431,422))
    screen.blit(objects.temple,(463,20))
    clock.tick(120)
    pygame.display.flip()