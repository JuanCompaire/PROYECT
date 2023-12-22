import pygame.sprite

import assets

WIDTH = 80
HEIGHT = 95


class Grass(pygame.sprite.Sprite):
    WIDTH = 80
    HEIGHT = 95
    def __init__(self,*groups,num_grass,occupied,X,Y):
        super().__init__(*groups)

        self.num_grass = num_grass
        self.occupied = occupied
        self.X = X
        self.Y = Y


        self.image = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))

        self.rect = self.image.get_rect(topleft=(X, Y))