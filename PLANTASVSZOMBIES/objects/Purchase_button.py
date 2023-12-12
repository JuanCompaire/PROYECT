import pygame.sprite

import assets

class Purchase_button(pygame.sprite.Sprite):
    def __init__(self, *groups,image_name,X,Y,width,height):
        super().__init__(*groups)

        self.image_name = image_name
        self.X = X
        self.Y = Y
        self.width = width
        self.height = height

        original_image = assets.get_image(image_name)
        self.image = pygame.transform.scale(original_image,(width,height))
        self.rect = self.image.get_rect(topleft=(X,Y))

