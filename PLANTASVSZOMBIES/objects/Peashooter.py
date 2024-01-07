import pygame.sprite
import assets


WIDTH = 70
HEIGHT = 70


class Peashooter(pygame.sprite.Sprite):
    HP = 100
    COST = 100
    moving = False
    def __init__(self, *groups, X, Y,placed):
        super().__init__(*groups)
        self.X = X
        self.Y = Y
        self.placed = placed
        original_image = assets.get_image("planta_militar")
        self.image = pygame.transform.scale(original_image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect(topleft=(X, Y))

    def move(self, x, y):
        self.rect.x = x -(WIDTH/2)
        self.rect.y = y -(HEIGHT/2)

    def set_moving(self, value):
        self.moving = value

    def attack(self):
        pass


