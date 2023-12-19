import pygame.sprite

import assets

WIDTH = 45
HEIGHT = 45


class Sun(pygame.sprite.Sprite):
    sun_points = 50
    def __init__(self,*groups,X,Y):
        super().__init__(*groups)

        self.X = X
        self.Y = Y

        original_image = assets.get_image("sol")
        self.image = pygame.transform.scale(original_image,(WIDTH,HEIGHT))
        self.rect = self.image.get_rect(topleft=(X,Y))

