import pygame
from variables import *

def load(directory:str, dimensions):
    name = pygame.image.load(directory)
    name = pygame.transform.scale(name, (dimensions[0], dimensions[1]))
    return name

#-----------------------------------FLOOR---------------------------------------
#tiles
tile_sheet = pygame.image.load('img/grassy_tileset_sheet.png')

grass1_tile = tile_sheet.subsurface((0, 50, tile_zoom, tile_zoom))
grass1_tile = pygame.transform.scale(grass1_tile, (tile_width,tile_width))
grass2_tile = tile_sheet.subsurface((0, 0, tile_zoom, tile_zoom))
grass2_tile = pygame.transform.scale(grass2_tile, (tile_width,tile_width))
path_tile = tile_sheet.subsurface((0, 100, 2*tile_zoom, 2*tile_zoom))
path_tile = pygame.transform.scale(path_tile, (tile_width, tile_width))

#objects
house_front = load('img/japanese_house_front.png',(80,90))
shop_front = load('img/japanese_shop_front.png',(80,90))
temple = load('img/temple_3.png',(250,250))

#-----------------------------------SPRITE--------------------------------------
sprite_sheet = pygame.image.load('img/black_hair_sprite.png')
