import pygame

def Label(screen,coords: tuple, dimensions: tuple, text: str):

    rect_parameters = coords + dimensions
    rect = pygame.Rect(rect_parameters)
    pygame.draw.rect(screen, (0,0,0), rect,0, border_radius=5)

    font = pygame.font.Font("freesansbold.ttf", 15)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (coords[0]+2, coords[1]+2))