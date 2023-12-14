import pygame
from pygame import font

import assets
import configs
from objects.Background import Background
from objects.Gamestart_message import Gamestart_message
from objects.Grass import Grass
from objects.Purchase_button import Purchase_button
from objects.Sunflower import Sunflower
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
#SUNS COUNT
sun_count = 25
sun_count_image = assets.get_image("sol")
sun_count_image = pygame.transform.scale(sun_count_image, (50, 50))
font_sun_count = pygame.font.Font(None, 36)
sun_count_color = (0,0, 0)  # Color amarillo para los soles

#OBJECTS LIST
sunflower_list = []

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
purchase_button_Peashotter = Purchase_button(sprites, image_name="planta_militar_compra",X=550,Y=20)
purchase_button_Sunflower = Purchase_button(sprites,image_name="sunflower_purchase",X=700,Y=20)
purchase_button_Wallnutt = Purchase_button(sprites,image_name="wallnutt_purchase",X=850,Y=20)
#CREATION OF THE GRASS SQUARES

for row in range(NUM_COLUMN_GRASS):
    for col in range(NUM_ROW_GRASS):
        grass_number = row * NUM_COLUMN_GRASS + col + 1
        grass_x = start_x + col * (grass_width )
        grass_y = start_y + row * (grass_height )
        Grass(sprites, num_grass=grass_number, placed=False, X=grass_x, Y=grass_y)

#FUNCTIONS
def add_new_sunflower(x,y):
    new_sunflower = Sunflower(sprites, X=x, Y=y)
    sunflower_list.append(new_sunflower)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #WHEN WE PRESS A KEY
        if event.type == pygame.KEYDOWN:
            #TO PRESS SPACE KEY TO START THE GAME
            if event.key == pygame.K_SPACE:
                gamestarted = True
                game_start_message.kill()
                show_text_menu = False

        # WHEN THE GAME START
        if gamestarted:
            # WHEN WE CLICK
            if event.type == pygame.MOUSEBUTTONDOWN:
                #TO GENERATE A SUNFLOWE WHEN WE PURCHASE IT
                if event.button == 1 and purchase_button_Sunflower.rect.collidepoint(event.pos):
                    add_new_sunflower(300,300)


    screen.fill("orange")

    sprites.draw(screen)
    #TO SHOW THE SUNS COUNT
    screen.blit(sun_count_image, (1150, 20))

    sun_count_text = font_sun_count.render(str(sun_count), True, sun_count_color)
    screen.blit(sun_count_text, (1120, 35))
    #TO SHOW THE TEXT MENU
    if show_text_menu:
        screen.blit(text_surface, text_rect)


    if not gameover:
        sprites.update()

    pygame.display.flip()
    clock.tick(configs.FPS)



pygame.quit()

