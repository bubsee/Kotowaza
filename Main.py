import pygame
import sys
import map
import objects
import sprites
import hitboxes
import entries
import NPCs
import time
import Notebook
import village_objects

#-----------sprite-------------
#frame counting
frame = 0          #actual frame
frame_counter = 0  #for the delay
#set direction
direction = 'down'
#starting coords
player_x,player_y = (838,585)
#speed of movement
speed = 3
#whether idling or not
idling = True
ticker = 0

def display_floor():
    x = 0
    y = 0
    for row in map.grid:
        for item in row:
            if item == 0:
                if map.randomlist[int(y/objects.tile_width)][int(x/objects.tile_width)] == 0:
                    screen.blit(objects.grass2_tile,(x,y))
                else:
                    screen.blit(objects.grass1_tile, (x,y))
            elif item == 1:
                screen.blit(objects.path_tile, (x,y))
            elif item == 2:
                screen.blit(objects.lake_tile, (x,y))
            x += objects.tile_width
        x = 0
        y += objects.tile_width

pygame.init()
pygame.display.set_caption('Kotozawa')
pygame.display.set_icon(objects.icon)
screen = pygame.display.set_mode((1250, 700), pygame.RESIZABLE)
clock = pygame.time.Clock()

#event loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #bind tab to notebook open
            if event.key == pygame.K_TAB:
                Notebook.run_notebook_screen(screen)
            #bind escape to close
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    sprite_hitbox = pygame.Rect(player_x+1, player_y+34, sprites.sprite_size_x-2, 8)

    #key binding for movement of sprite and map movement
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        direction = "left"
        if hitboxes.movement_allowed(sprite_hitbox, player_x - speed , player_y):
            player_x -= speed
            idling = False
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        direction = "right"
        if hitboxes.movement_allowed(sprite_hitbox, player_x + speed , player_y):
            player_x += speed
            idling = False
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        direction = "up"
        if hitboxes.movement_allowed(sprite_hitbox, player_x  , player_y - speed):
            player_y -= speed
            idling = False
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        direction = "down"
        if hitboxes.movement_allowed(sprite_hitbox, player_x , player_y + speed):
            player_y += speed
            idling = False
    else:
        idling = True

    display_floor()

    for tile in NPCs.Arthur.route:
        pygame.draw.circle(screen, (255, 0, 0), tile, 5)

    village_objects.show_everything_under_sprite(screen)

    #blitting the sprite
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

    screen.blit(current_image, (player_x, player_y))

    #print(player_x, player_y)  # debugging player coords
    #print(entries.check_entry(player_x, player_y))  # debugging entries of buildings
    #NPCs.show_positions(screen,frame)   #debugging villager idling positions
    #print(NPCs.Arthur.end_point)     #debug NPCs endpoint
    #print(NPCs.Arthur.route)

    if NPCs.Arthur.route == []:
        NPCs.Arthur.find_route()
    else:
        NPCs.Arthur.walk_to_destination(screen, current_image)

    '''if NPCs.Rowan.route == []:
        NPCs.Rowan.reset_route(screen)
    else:
        NPCs.Rowan.walk_to_destination(screen, current_image)'''



    #details to go OVER the sprite
    village_objects.show_everything_over_sprite(screen)


    #frame (for animations) incrementation
    frame_counter += 1

    if frame_counter >= sprites.frame_delay:
        frame += 1
        frame_counter = 0

        frame = frame % 4

    # ticker incrementation
    ticker += 1

    #hitboxes
    if hitboxes.showing == True:
        hitboxes.draw(screen)
        pygame.draw.rect(screen, (255, 0, 0), sprite_hitbox, 2)

    clock.tick(120)
    pygame.display.flip()