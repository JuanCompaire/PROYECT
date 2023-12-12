import pygame.sprite

import assets
import configs


class Gamestart_message(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = 1
        self.image = assets.get_image("menu")
        self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH/2,configs.SCREEN_HEIGHT/2))
        super().__init__(*groups)