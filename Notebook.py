import pygame

def run_notebook_screen(screen):
    book_open = True
    while book_open:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # bind tab to notebook open
                if event.key == pygame.K_TAB:
                    book_open = False
        pygame.draw.circle(screen, (0,0,255), (500,500), 100)
        pygame.display.flip()
        #print('hello')
