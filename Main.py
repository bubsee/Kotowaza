import pygame
import sys
import map
import objects
import sprites
import hitboxes
import entries
import NPCs

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

    #---------------BUILDINGS------------------
    screen.blit(objects.big_house,(750,435))
    screen.blit(objects.main_palace,(474,0))
    screen.blit(objects.food_shop,(328,530))
    screen.blit(objects.shop, (418, 531))
    screen.blit(objects.tall_palace,(46,0))
    screen.blit(objects.tall_building,(864,120))
    screen.blit(objects.wide_house,(1040,62))
    screen.blit(objects.tall_house,(960,43))
    screen.blit(objects.regular_house,(1150,63))
    screen.blit(objects.dojo,(1100,375))

    #----------------DETAILS-------------------
    screen.blit(objects.lake_tile, (275, 400))
    screen.blit(objects.lake_tile, (300, 400))
    screen.blit(objects.lake_tile, (315, 400))
    screen.blit(objects.sakura,(775,90))    #right side sakura
    screen.blit(objects.sakura, (775, 140))
    screen.blit(objects.sakura, (775, 190))
    screen.blit(objects.sakura, (775, 240))
    screen.blit(objects.sakura, (432, 90))  #left side sakura
    screen.blit(objects.sakura, (432, 140))
    screen.blit(objects.sakura, (432, 190))
    screen.blit(objects.sakura, (432, 240))
    screen.blit(objects.pond, (591,360))    #pond
    screen.blit(objects.tree, (854, 245))   #left side trees
    screen.blit(objects.tree, (854, 275))
    screen.blit(objects.tree, (854, 305))
    screen.blit(objects.tree, (854,335))
    screen.blit(objects.tree, (924, 245))   #right side trees
    screen.blit(objects.tree, (924, 275))
    screen.blit(objects.tree, (924, 305))
    screen.blit(objects.tree, (924, 335))
    screen.blit(objects.fish_box,(265,575)) #fix box
        #LAKE EDGES
    screen.blit(objects.lake_right_edge, (374,310)) #top lake
    screen.blit(objects.lake_right_edge, (374,275))
    screen.blit(objects.lake_left_edge, (250,310))
    screen.blit(objects.lake_left_edge, (250,275))
    screen.blit(objects.lake_top_edge, (250,275))
    screen.blit(objects.lake_top_edge, (290,275))
    screen.blit(objects.lake_top_edge, (330,275))
    screen.blit(objects.lake_top_edge, (337,275))
    screen.blit(objects.lake_right_edge, (374,485)) #bottom lake
    screen.blit(objects.lake_right_edge, (374,450))
    screen.blit(objects.lake_left_edge, (250,485))
    screen.blit(objects.lake_left_edge, (250,450))
    screen.blit(objects.lake_bottom_edge, (250, 525))
    screen.blit(objects.lake_bottom_edge, (290, 525))
    screen.blit(objects.lake_bottom_edge, (330, 525))
    screen.blit(objects.lake_bottom_edge, (337, 525))
    screen.blit(objects.lake_short_bottom_edge, (250, 350))   #middle section
    screen.blit(objects.lake_short_bottom_edge, (350, 350))
    screen.blit(objects.lake_short_top_edge, (250, 450))
    screen.blit(objects.lake_short_top_edge, (350, 450))
    screen.blit(objects.lake_left_edge, (275, 350))
    screen.blit(objects.lake_left_edge, (275, 390))
    screen.blit(objects.lake_left_edge, (275, 413))
    screen.blit(objects.lake_right_edge, (350, 350))
    screen.blit(objects.lake_right_edge, (350, 390))
    screen.blit(objects.lake_right_edge, (350, 413))
        #END OF LAKE EDGES
    screen.blit(objects.bridge_floor,(260,370)) #bridge
    screen.blit(objects.bridge_floor, (293, 370))
    screen.blit(objects.bridge_floor, (326, 370))
    screen.blit(objects.top_bridge_railing,(260,345))
    screen.blit(objects.single_hedge, (945, 145)) #hedges
    screen.blit(objects.single_hedge, (1220, 195))
    screen.blit(objects.up_hedge, (1002, 212))
    screen.blit(objects.up_hedge, (1002, 247))
    screen.blit(objects.up_hedge, (1002, 282))
    screen.blit(objects.up_hedge, (1002, 317))
    screen.blit(objects.up_hedge, (1100, 212))
    screen.blit(objects.up_hedge, (1100, 247))
    screen.blit(objects.up_hedge, (1100, 282))
    screen.blit(objects.up_hedge, (1100, 317))
    screen.blit(objects.up_hedge, (1220, 160))
    screen.blit(objects.up_hedge, (945, 160))
    screen.blit(objects.single_hedge, (1220, 195))
    screen.blit(objects.single_hedge, (1002, 352))
    screen.blit(objects.single_hedge, (1100, 352))
    screen.blit(objects.single_hedge, (550,325))   #central single hedges
    screen.blit(objects.single_hedge, (575,300))
    screen.blit(objects.single_hedge, (525,350))
    screen.blit(objects.single_hedge, (677,325))
    screen.blit(objects.single_hedge, (652,300))
    screen.blit(objects.single_hedge, (702,350))
    screen.blit(objects.single_hedge, (677,450))
    screen.blit(objects.single_hedge, (652,475))
    screen.blit(objects.single_hedge, (702,427))
    screen.blit(objects.single_hedge, (550,450))
    screen.blit(objects.single_hedge, (575,475))
    screen.blit(objects.single_hedge, (525,425))
    screen.blit(objects.big_tree,(500,505)) #big trees
    screen.blit(objects.big_tree, (645, 530))
    #screen.blit(objects.big_tree, (949, 530)) #-
    screen.blit(objects.big_tree, (1132, 250))
    screen.blit(objects.big_tree, (263, 150))
    #screen.blit(objects.big_tree, (400,430)) #-
    screen.blit(objects.left_flag,(80,200))
    screen.blit(objects.right_flag,(174,200))
    screen.blit(objects.statue, (804,590))
    screen.blit(objects.statue, (875, 590))

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
    #print(player_x, player_y)  # debugging coords
    print(entries.check_entry(player_x, player_y))  # debugging entries of buildings
    NPCs.show_positions(screen,frame)   #debugging villager idling

    #details to go OVER the sprite
    screen.blit(objects.gate, (72, 280))  # gate
    screen.blit(objects.bottom_bridge_railing, (260, 391))
    screen.blit(objects.side_hedge, (985, 195))
    screen.blit(objects.side_hedge, (1101, 195))
    screen.blit(objects.side_hedge, (1141, 195))
    screen.blit(objects.side_hedge, (1181, 195))
    screen.blit(objects.side_hedge, (945, 195))


    #frame (for animations) incrementation
    frame_counter += 1

    if frame_counter >= sprites.frame_delay:
        frame += 1
        frame_counter = 0

        frame = frame % 4

    #hitboxes
    if hitboxes.showing == True:
        hitboxes.draw(screen)
        pygame.draw.rect(screen, (255, 0, 0), sprite_hitbox, 2)

    clock.tick(120)
    pygame.display.flip()