import pygame
from pygame import font

import assets
import configs
from objects.Background import Background
from objects.Gamestart_message import Gamestart_message
from objects.Grass import Grass
from objects.Purchase_button import Purchase_button
#TO RUN THE GAME
pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH,configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
gameover = False
gamestarted = False
show_text_menu = False

assets.load_images()

sprites = pygame.sprite.LayeredUpdates()
#MENU PRE_GAME
game_start_message = Gamestart_message(sprites)
text_content = "PRESS SPACE TO START"
font = pygame.font.Font(None, 66)
text_color = (0, 0, 0)
text_surface = font.render(text_content, True, text_color)
text_rect = text_surface.get_rect()
text_rect.center = (configs.SCREEN_WIDTH // 2, configs.SCREEN_HEIGHT // 2+300)
show_text_menu = True

# ITERATION VARIABLES
NUM_ROW_GRASS = 9;
NUM_COLUMN_GRASS = 5
grass_width = 80
grass_height = 95
start_x = 518
start_y = 243
#BACKGROUND
Background(sprites)
#CREATION OF BUTTONS TO BUY PLANTS
purchase_button_Peashotter = Purchase_button(sprites, image_name="planta_militar_compra",X=700,Y=20,width=100,height=100)
purchase_button_Sunflower = Purchase_button(sprites,image_name="sunflower_purchase",X=850,Y=20,width=100,height=100)
purchase_button_Wallnutt = Purchase_button(sprites,image_name="wallnutt_purchase",X=1000,Y=20,width=100,height=100)
#CREATION OF THE GRASS SQUARES

for row in range(NUM_COLUMN_GRASS):
    for col in range(NUM_ROW_GRASS):
        grass_number = row * NUM_COLUMN_GRASS + col + 1
        grass_x = start_x + col * (grass_width )
        grass_y = start_y + row * (grass_height )
        Grass(sprites, num_grass=grass_number, placed=False, X=grass_x, Y=grass_y)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gamestarted = True
                game_start_message.kill()
                show_text_menu = False


    screen.fill("orange")

    sprites.draw(screen)
    if show_text_menu:
        screen.blit(text_surface, text_rect)


    if not gameover:
        sprites.update()

    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()

