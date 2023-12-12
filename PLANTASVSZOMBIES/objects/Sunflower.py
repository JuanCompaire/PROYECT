import pygame.sprite

import assets

cost = 50
HP = 20
placed = False
num_grass = -1
generation_speed = 1


class Sunflower(pygame.sprite.Sprite):
    def __init__(self,*groups,X,Y):
        super().__init__(*groups)

        self.X = X
        self.Y = Y

        self.image = assets.get_image("girasol")
        self.rect = self.image.get_rect(topleft=(X,Y))



