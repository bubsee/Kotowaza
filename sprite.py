import pygame

def take_row(row:int,file:str,file_dimensions:tuple):
    frame_height, frame_width = file_dimensions[1] // 4, file_dimensions[0] // 4
    sprite_sheet = pygame.image.load(f'img/sprites/sprite_{file}_sheet.png')
    array = []
    x = float(0.0)
    y = float(row * frame_height)

    for i in range(4):
        frame = sprite_sheet.subsurface(x,y,frame_width,frame_height)
        frame = pygame.transform.scale(frame, (sprite_size_x, sprite_size_y))
        array.append(frame)
        x += frame_width
    return array

#------------------VARIABLES------------------------
sprite_size_x, sprite_size_y = (27,48)
frame_delay = 6  #how fast the sprite animation will play

#-----------------DEFINITIONS
down_run = take_row(0,'walking',(311,601))
up_run = take_row(1,'walking',(311,601))
left_run = take_row(2,'walking',(311,601))
right_run = take_row(3,'walking',(311,601))

down_idle = take_row(0,'idle',(316,643))
up_idle = take_row(1,'idle',(316,643))
left_idle = take_row(2,'idle',(316,643))
right_idle = take_row(3,'idle',(316,643))