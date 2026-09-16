import pygame
import objects
import map
showing = True
import list_of_hitboxes

#fucntion to add in details hitboxes
def add(x, y, object):
    rect = pygame.Rect(x, y, object.get_width(), object.get_height())
    list_of_hitboxes.all_hitboxes.append(rect)






#add in the details
add(804,590,objects.statue)  #left statue
add(875,590,objects.statue)  #right statue
add(265,575,objects.fish_box) #fish box
add(80,200,objects.left_flag) #left flag
add(174,200,objects.right_flag) #right flag


def draw(screen):
    for wall in list_of_hitboxes.all_hitboxes:
        pygame.draw.rect(screen, (255, 0, 0), wall, 2)

    #NPCs_hitboxes.show_NPC_hitboxes()

def movement_allowed(hitbox, new_x, new_y):
    future_hitbox = pygame.Rect(new_x-1, new_y+34, hitbox.width, hitbox.height)

    corners = [[future_hitbox.left, future_hitbox.top],
               [future_hitbox.right, future_hitbox.top],
               [future_hitbox.left, future_hitbox.bottom],
               [future_hitbox.right, future_hitbox.bottom]
               ]

    for vertice in corners:
        col, row = vertice[0] // objects.tile_width, vertice[1] // objects.tile_width
        if map.grid[row][col] != 1:
            return False

    for wall in list_of_hitboxes.all_hitboxes:
        if future_hitbox.colliderect(wall):
            return False
    return True

