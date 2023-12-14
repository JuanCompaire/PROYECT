import pygame.sprite

import assets

WIDTH = 70
HEIGHT = 70
sun_count = 50

class Sun(pygame.sprite.Sprite):
    def __init__(self,*groups,X,Y):
        super().__init__(*groups)

        self.X = X
        self.Y = Y

        original_image = assets.get_image("sol")
        self.image = pygame.transform.scale(original_image,(WIDTH,HEIGHT))
        self.rect = self.image.get_rect(topleft=(X,Y))

