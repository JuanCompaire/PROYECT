import pygame.sprite

import assets

from objects.Sun import Sun


WIDTH = 70
HEIGHT = 70
cost = 50
HP = 20
placed = False
num_grass = -1
generation_speed = 1
generation_timer = 0


class Sunflower(pygame.sprite.Sprite):
    def __init__(self,*groups,X,Y):
        super().__init__(*groups)

        self.X = X
        self.Y = Y

        original_image = assets.get_image("girasol")
        self.image = pygame.transform.scale(original_image,(WIDTH,HEIGHT))
        self.rect = self.image.get_rect(topleft=(X,Y))


    def produce_sun(self,timer):
        if timer >= 15:
            pass




