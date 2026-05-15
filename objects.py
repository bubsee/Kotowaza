import pygame
from variables import *

def load(directory:str, dimensions):
    name = pygame.image.load(directory)
    name = pygame.transform.scale(name, (dimensions[0], dimensions[1]))
    return name

#-----------------------------------FLOOR---------------------------------------
#tiles
grass_sheet = pygame.image.load('kotozawa/img/grass.png')
grass1_tile = grass_sheet.subsurface((0, 60, tile_zoom, tile_zoom))
grass1_tile = pygame.transform.scale(grass1_tile, (tile_width,tile_width))
grass2_tile = grass_sheet.subsurface((0, 0, tile_zoom, tile_zoom))
grass2_tile = pygame.transform.scale(grass2_tile, (tile_width,tile_width))

path_tile = pygame.image.load('kotozawa/img/cobble.png')
path_tile = pygame.transform.scale(path_tile, (tile_width, tile_width))

#---------------------------------BUILDINGS-------------------------------------


#-----------------------------------SPRITE--------------------------------------
sprite_sheet = pygame.image.load('kotozawa/img/black_hair_sprite.png')
