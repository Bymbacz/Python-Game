import pygame


class Map:
    def __init__(self, screen, x, y):
        path = "tlo_mapy.png"
        tlo = pygame.image.load(path)
        screen.blit(tlo, (0, 0))
