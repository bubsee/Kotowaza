import pygame
import objects
frame_pointer = 0
notebook = objects.notebook_sheet
frame_width,frame_height = 168,73
frame_width, frame_height = frame_width//6, frame_height//2
array = []
notebook_size = (600,600)

for y in range (2):
        for x in range (6):
                frame = notebook.subsurface(x*frame_width, y * frame_height, frame_width, frame_height)
                frame = pygame.transform.scale(frame, notebook_size)
                array.append(frame)
                x += frame_width
        y += frame_height


def run_notebook_screen(screen, book_open, screenshot):
        #-------------background-------------------
        screen.blit(screenshot, (0, 0))
        rect = pygame.Surface((1250,700), pygame.SRCALPHA)  # per-pixel alpha
        rect.fill((0,0,0, 200))  # notice the alpha value in the color
        screen.blit(rect, (0, 0))

        #---------------notebook opening animation---------------------
        global frame_pointer
        if frame_pointer < 11*30:
                frame_pointer += 20
        screen.blit(array[frame_pointer // 30], (355,20))

