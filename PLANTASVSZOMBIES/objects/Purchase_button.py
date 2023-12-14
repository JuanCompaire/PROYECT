import pygame.sprite

import assets

WIDTH = 100
HEIGHT = 100

class Purchase_button(pygame.sprite.Sprite):
    def __init__(self, *groups,image_name,X,Y):
        super().__init__(*groups)

        self.image_name = image_name
        self.X = X
        self.Y = Y


        original_image = assets.get_image(image_name)
        self.image = pygame.transform.scale(original_image,(WIDTH,HEIGHT))
        self.rect = self.image.get_rect(topleft=(X,Y))

