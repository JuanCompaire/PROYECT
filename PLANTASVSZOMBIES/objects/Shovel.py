import pygame.sprite

import assets

WIDTH = 85
HEIGHT = 85

class Shovel(pygame.sprite.Sprite):

    def __init__(self,*groups,X,Y,using):
        super().__init__(*groups)

        self.X = X
        self.Y = Y
        self.using = using
        original_image = assets.get_image("pala_accion")
        self.image = pygame.transform.scale(original_image,(WIDTH,HEIGHT))
        self.rect = self.image.get_rect(topleft=(X,Y))

    def move(self,x,y):
        self.rect.x = x - (WIDTH/2)
        self.rect.y = y - (HEIGHT/2)

    def set_using(self,value):
        self.using = value