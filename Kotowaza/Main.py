import pygame
import sys
import map
import objects
import hitboxes
import NPCs
import Notebook
import village_objects
import Text_popups
import entries
import sprites
import Player
from Settings import *

frame = 0
frame_counter = 0
frozen_NPC = None

#-----game loops------
notebook_open = False
conversation_open = False

f_has_been_pressed = False

interactable_villager = None

pygame.init()
pygame.display.set_caption('Kotowaza')
pygame.display.set_icon(objects.icon)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.RESIZABLE)

background_surface = pygame.Surface(screen.get_size())

clock = pygame.time.Clock()

#event loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #bind tab to notebook open
            if event.key == pygame.K_TAB:
                notebook_open = not notebook_open
                Notebook.frame_pointer = 0
            #bind escape to close
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_h:
                HITBOXES_SHOWINGf = not HITBOXES_SHOWINGf

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_f:
                f_has_been_pressed = False

        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    sprite_hitbox = pygame.Rect(Player.player_x+1, Player.player_y+34, SPRITE_WIDTH-2, 8)

    if not notebook_open:
        if not conversation_open:
            #key binding for movement of sprite and map movement
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                Player.direction = "left"
                if hitboxes.movement_allowed(sprite_hitbox, Player.player_x - Player.PLAYER_SPEED , Player.player_y):
                    Player.player_x -= Player.PLAYER_SPEED
                    Player.idling = False
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                Player.direction = "right"
                if hitboxes.movement_allowed(sprite_hitbox, Player.player_x + Player.PLAYER_SPEED , Player.player_y):
                    Player.player_x += Player.PLAYER_SPEED
                    Player.idling = False
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                Player.direction = "up"
                if hitboxes.movement_allowed(sprite_hitbox, Player.player_x  , Player.player_y - Player.PLAYER_SPEED):
                    Player.player_y -= Player.PLAYER_SPEED
                    Player.idling = False
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                Player.direction = "down"
                if hitboxes.movement_allowed(sprite_hitbox, Player.player_x , Player.player_y + Player.PLAYER_SPEED):
                    Player.player_y += Player.PLAYER_SPEED
                    Player.idling = False
            else:
                Player.idling = True

        #villager interact
        if keys[pygame.K_f] :
            if interactable_villager:
                if not f_has_been_pressed:
                    print(f'interacted with {interactable_villager}')

                    Player.direction = interactable_villager.turn_to_face(Player.player_x, Player.player_y)
                    print(Player.direction)
                    print(interactable_villager.direction)

                    conversation_open = not conversation_open                        #flip on and off conversation when f is pressed

                    f_has_been_pressed = True                                        #to make it only run once even when button is held
                    frozen_NPC = None if frozen_NPC else interactable_villager       #toggle frozen npc between None and the villager in conversation


        if keys[pygame.K_e] and entries.check_entry(Player.player_x,Player.player_y):
            print('Home entrance triggered but no functionality...')

    else:
        Player.idling = True

    map.display_floor(background_surface)

    '''for tile in NPCs.Arthur.route:
        pygame.draw.circle(screen, (255, 0, 0), tile, 5)'''  # debug route being followed by Villager: Arthur

    village_objects.show_everything_under_sprite(background_surface)

    Player.draw(background_surface,frame)

    #print(f'{Player.player_x},{Player.player_y}')  # debugging player coords
    #print(entries.check_entry(Player.player_x, Player.player_y))  # debugging entries of buildings
    #NPCs.show_positions(background_surface,frame)   #debugging villager Player.idling positions
    #print(NPCs.Arthur.end_point)     #debug NPCs endpoint
    #print(NPCs.Arthur.route)

    if not interactable_villager:
        direction_of_conversationalist = 'down'
    else:
        direction_of_conversationalist = interactable_villager.direction

    NPCs.update(background_surface, notebook_open, sprite_hitbox, frozen_NPC, direction_of_conversationalist)

    #details to go OVER the sprite
    village_objects.show_everything_over_sprite(background_surface)

    screen.blit(background_surface, (0, 0))

    screenshot = screen.copy()
    if notebook_open:
        Notebook.run_notebook_screen(screen, notebook_open, screenshot)

    if not notebook_open:
        #frame (for animations) incrementation
        frame_counter += 1

    if frame_counter >= FRAME_DELAY:
        frame += 1
        frame_counter = 0

        frame = frame % 4

    building = entries.check_entry(Player.player_x, Player.player_y)
    if building:
        Text_popups.Label(screen, (Player.player_x+30, Player.player_y+40),  f'[E] Enter {building}')

    #hitboxes
    if HITBOXES_SHOWING and not notebook_open:
        hitboxes.draw(screen)
        pygame.draw.rect(screen, (255, 0, 0), sprite_hitbox, 2)

    for villager in NPCs.NPCs:
        if villager.close_by((Player.player_x, Player.player_y)):
            interactable_villager = villager
            Text_popups.Label(screen,(villager.x, villager.y),'[F] interact')
    NPCs.update_villager_hitboxes(screen)

    clock.tick(FPS_CAP)
    pygame.display.flip()