import pygame.sprite
import assets

WIDTH = 70
HEIGHT = 70

class Mower(pygame.sprite.Sprite):


    def __init__(self, *groups, X, Y,activated):
        super().__init__(*groups)
        self.X = X
        self.Y = Y
        self.activated = activated
        original_image = assets.get_image("cortadora_cesped")
        self.image = pygame.transform.scale(original_image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect(topleft=(X, Y))

    def activate(self):
        if self.activated:
            self.rect.x += 1



