import pygame

def load(directory:str, dimensions):
    name = pygame.image.load(directory)
    name = pygame.transform.scale(name, (dimensions[0], dimensions[1]))
    return name

def create(directory: str, dimensions:tuple):
    thing = pygame.image.load(f'img/{directory}.png')
    thing = pygame.transform.scale(thing, dimensions)
    return thing

#-----------------------------------FLOOR---------------------------------------
tile_width = 25  #how big a tile appears on the blitted screen
tile_zoom = 25   #how much of the original tilesheet is cut out to make one tile
#tiles
grass_sheet = pygame.image.load('img/tiles/grass.png')
grass1_tile = grass_sheet.subsurface((0, 60, tile_zoom, tile_zoom))
grass1_tile = pygame.transform.scale(grass1_tile, (tile_width,tile_width))
grass2_tile = grass_sheet.subsurface((0, 0, tile_zoom, tile_zoom))
grass2_tile = pygame.transform.scale(grass2_tile, (tile_width,tile_width))
lake_tile = pygame.image.load('img/tiles/lake.png')
lake_tile = pygame.transform.scale(lake_tile, (tile_width,tile_width))
path_tile = pygame.image.load('img/tiles/cobble.png')
path_tile = pygame.transform.scale(path_tile, (tile_width, tile_width))

#---------------------------------BUILDINGS-------------------------------------
big_house = create('buildings/big_house',(200,180))
main_palace = create('buildings/big_grey_palace',(300,300))
food_shop = create('buildings/food_shop',(80,80))
shop = create('buildings/shop',(80,95))
tall_palace = create('buildings/tall_blue_palace',(180,240))
tall_building = create('buildings/tall_building',(70,160))
wide_house = create('buildings/wide_house', (100,100))
tall_house = create('buildings/tall_house', (70,120))
regular_house = create('buildings/regular_house', (90,100))
dojo = create('buildings/dojo',(150,105))

#---------------------------------DETAILS---------------------------------------
sakura = create('details/sakura', (40,50))
tree = create('details/small_tree',(20,40))
statue = create('details/statue',(20,36))
pond = create('details/pond',(70,70))
gate = create('details/gate',(130,80))
fish_box = create('details/fish_box',(65,30))
bottom_bridge_railing = create('details/bottom_bridge_railing',(100,35))
top_bridge_railing = create('details/top_bridge_railing',(100,35))
bridge_floor = create('tiles/bridge_tile',(33,50))
side_hedge = create('details/sideways_hedge',(40,23))
up_hedge = create('details/up_hedge',(23,40))
single_hedge = create('details/single_hedge',(23,23))
big_tree= create('details/tree',(100,90))
lake_right_edge = create('details/lake_edge',(4,40))
lake_left_edge = pygame.transform.flip(lake_right_edge, True, False)
lake_top_edge = create('details/lake_top_edge',(40,4))
lake_bottom_edge = pygame.transform.flip(lake_top_edge, False, True)
lake_short_bottom_edge = pygame.transform.scale(lake_bottom_edge, (27,4))
lake_short_top_edge = pygame.transform.scale(lake_top_edge, (27,4))
left_flag = create('details/flag',(20,60))
right_flag = pygame.transform.flip(left_flag, True, False)