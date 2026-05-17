import pygame
import objects
showing = True

#fucntion to add in details hitboxes
def add(x, y, object):
    rect = pygame.Rect(x, y, object.get_width(), object.get_height())
    walls.append(rect)

#buildings have to be (more) manual
walls = [
    #add in the buildings
    pygame.Rect(46, 0, 178, 238),   # tall palace
    pygame.Rect(474, 0, 300, 296),  # main palace
    pygame.Rect(328,530,80,80),  # fish shop
    pygame.Rect(418,531,80,76),  # normal shop
    pygame.Rect(418,531,48,96),  # normal shop
    pygame.Rect(750,435,190,164),  # house (above doorway)
    pygame.Rect(750,435,81,180),
    pygame.Rect(870,435,81,180),
    pygame.Rect(1100,375,150,102),  # dojo
    pygame.Rect(864,120,70,149),  # bell tower
    pygame.Rect(864,120,20,160),
    pygame.Rect(916,120,20,160),
    pygame.Rect(960,41,70,120),  # left_house
    pygame.Rect(1040,62,100,100),  # middle_house
    pygame.Rect(1150,63,90,100),  # right_house
    #pool
    pygame.Rect(600, 366, 50, 58),  # vertical
    pygame.Rect(594, 376, 62, 40),  # horizontal
    #pygame.Rect(601, 368, 44, 54),  # middle fill
]


#add in the details
add(804,590,objects.statue)  #left statue
add(875,590,objects.statue)  #right statue
add(265,575,objects.fish_box) #fish box
add(80,200,objects.left_flag) #left flag
add(174,200,objects.right_flag) #right flag



def draw(screen):
    for wall in walls:
        pygame.draw.rect(screen, (255, 0, 0), wall, 2)

def movement_allowed(hitbox, new_x, new_y):
    future_hitbox = pygame.Rect(new_x-1, new_y+34, hitbox.width, hitbox.height)
    for wall in walls:
        if future_hitbox.colliderect(wall):
            return False
    return True


    return True
