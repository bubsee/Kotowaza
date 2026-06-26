import pygame

def run_notebook_screen(screen, book_open, screenshot):
    while book_open:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # bind tab to notebook open
                if event.key == pygame.K_TAB:
                    book_open = not book_open


        screen.blit(screenshot, (0, 0))
        rect = pygame.Surface((1250,700), pygame.SRCALPHA)  # per-pixel alpha
        rect.fill((0,0,0, 128))  # notice the alpha value in the color
        screen.blit(rect, (0, 0))

