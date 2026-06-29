import pygame

frame = 0

def run_notebook_screen(screen, book_open, screenshot):
        #-------------background-------------------
        screen.blit(screenshot, (0, 0))
        rect = pygame.Surface((1250,700), pygame.SRCALPHA)  # per-pixel alpha
        rect.fill((0,0,0, 128))  # notice the alpha value in the color
        screen.blit(rect, (0, 0))

        #---------------notebook opening animation---------------------
        global frame
        frame += 1