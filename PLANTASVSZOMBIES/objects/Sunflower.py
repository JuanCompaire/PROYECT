import pygame.sprite
import assets

WIDTH = 70
HEIGHT = 70

class Sunflower(pygame.sprite.Sprite):

    HP = 20
    COST = 50
    moving = False
    generate_sun = False
    generation_time = 5

    def __init__(self, *groups, X, Y, placed):
        super().__init__(*groups)
        self.X = X
        self.Y = Y
        self.placed = placed
        original_image = assets.get_image("girasol")
        self.image = pygame.transform.scale(original_image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect(topleft=(X, Y))
        self.start_time = 0

    def move(self, x, y):
        self.rect.x = x - (WIDTH / 2)
        self.rect.y = y - (HEIGHT / 2)

    def set_moving(self, value):
        self.moving = value

    def generate_suns(self, current_time):
        if self.placed:
            elapsed_time = (current_time - self.start_time) // 1000

            # Verifica si han pasado 5 segundos o más
            if elapsed_time >= self.generation_time:
                self.generate_sun = True
                self.start_time = current_time
