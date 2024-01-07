import pygame.sprite
import assets

WIDTH = 25
HEIGHT = 25

class Pea(pygame.sprite.Sprite):
    def __init__(self, *groups, X, Y):
        super().__init__(*groups)
        self.X = X
        self.Y = Y
        original_image = assets.get_image("guisante")
        self.image = pygame.transform.scale(original_image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect(topleft=(X, Y))

    def move(self):
        self.rect.x += 10

