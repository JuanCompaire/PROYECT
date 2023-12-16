import pygame.sprite

import assets

WIDTH = 80
HEIGHT = 95


class Grass(pygame.sprite.Sprite):
    def __init__(self,*groups,num_grass,placed,X,Y):
        super().__init__(*groups)

        self.num_grass = num_grass
        self.placed = placed
        self.X = X
        self.Y = Y

        self.image = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))

        self.rect = self.image.get_rect(topleft=(X, Y))