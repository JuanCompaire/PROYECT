import pygame.sprite
import assets

class Mower(pygame.sprite.Sprite):


    def __init__(self, *groups, X, Y,activated):
        super().__init__(*groups)
        self.X = X
        self.Y = Y
        self.activated = activated
        original_image = assets.get_image("cortadora_cesped")
        self.image = pygame.transform.scale(original_image, (70, 70))
        self.rect = self.image.get_rect(topleft=(X, Y))

