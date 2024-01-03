import pygame.sprite
import assets

WIDTH = 115
HEIGHT = 115
class Zombie(pygame.sprite.Sprite):
    HP = 100
    COST = 50
    attack = False
    def __init__(self, *groups, X, Y):
        super().__init__(*groups)
        self.X = X
        self.Y = Y

        original_image = assets.get_image("zombie")
        self.image = pygame.transform.scale(original_image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect(topleft=(X, Y))

    def move(self):
        self.rect.x -= 1

