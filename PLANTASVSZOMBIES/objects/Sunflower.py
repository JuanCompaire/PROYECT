import pygame.sprite
import assets
from objects.Sun import Sun

WIDTH = 70
HEIGHT = 70

class Sunflower(pygame.sprite.Sprite):

    HP = 20
    COST = 50
    moving = False


    def __init__(self, *groups, X, Y,placed):
        super().__init__(*groups)
        self.X = X
        self.Y = Y
        self.placed = placed
        original_image = assets.get_image("girasol")
        self.image = pygame.transform.scale(original_image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect(topleft=(X, Y))



    def move(self, x, y):
        self.rect.x = x -(WIDTH/2)
        self.rect.y = y -(HEIGHT/2)
       


    def set_moving(self, value):
        self.moving = value

    def generate_suns(self):
        pass
        
    