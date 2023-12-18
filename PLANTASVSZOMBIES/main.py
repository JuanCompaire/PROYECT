import pygame
from pygame import font

import assets
import configs
from objects.Background import Background
from objects.Gamestart_message import Gamestart_message
from objects.Grass import Grass
from objects.Purchase_button import Purchase_button
from objects.Sunflower import Sunflower
from objects.Peashooter import Peashooter
from objects.Wallnutt import Wallnutt
#TO RUN THE GAME
pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH,configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
gameover = False
gamestarted = False
show_text_menu = False
not_enough_sun = False

assets.load_images()
assets.load_gif()

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
sun_count = 200
sun_count_image = assets.get_image("sol")
sun_count_image = pygame.transform.scale(sun_count_image, (50, 50))
font_sun_count = pygame.font.Font(None, 36)
sun_count_color = (0,0, 0)
#NOT ENOUGH SUNS INDICATOR
not_enough_sun_color = (255, 0, 0)

#OBJECTS LIST
sunflower_list = []
peashooter_list = []
wallnutt_list = []
grass_list = []

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
        grass_number = row * NUM_ROW_GRASS + col + 1
        grass_x = start_x + col * grass_width
        grass_y = start_y + row * grass_height
        new_grass = Grass(sprites, num_grass=grass_number, occupied=False, X=grass_x, Y=grass_y)
        grass_list.append(new_grass)




#FUNCTIONS

def generate_sunflower():
    new_sunflower = Sunflower(sprites, X=720, Y=130, placed=False)
    sunflower_list.append(new_sunflower)

def generate_peashooter():
    new_peashooter = Peashooter(sprites, X=570, Y=130, placed=False)
    peashooter_list.append(new_peashooter)

def generate_wallnutt():
    new_wallnutt = Wallnutt(sprites, X=870, Y=130, placed=False)
    wallnutt_list.append(new_wallnutt)

#GAME LOOP
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
                #WHEN WE LEFT CLICK
                if event.button == 1:
                    #TO GET INFO ABOUT GRASS BLOCK
                    for grass in grass_list:
                        if grass.rect.collidepoint(event.pos):
                            print(grass.num_grass)
                    

                    #TO GENERATE A SUNFLOWER WHEN WE PURCHASE IT
                    if  purchase_button_Sunflower.rect.collidepoint(event.pos) and sun_count >= Sunflower.COST:
                        generate_sunflower()
                        sun_count -= Sunflower.COST
                        not_enough_sun = False
                    #TO GENERATE A PEASHOOTER WHEN WE PURCHASE IT
                    elif purchase_button_Peashotter.rect.collidepoint(event.pos) and sun_count >= Peashooter.COST:
                        generate_peashooter()
                        sun_count -= Peashooter.COST
                        not_enough_sun = False
                    #TO GENERATE A WALLNUTT WHEN WE PURCHASE IT
                    elif purchase_button_Wallnutt.rect.collidepoint(event.pos) and sun_count >= Wallnutt.COST:
                        generate_wallnutt()
                        sun_count -= Wallnutt.COST
                        not_enough_sun = False
                    #WHEN YOU DONT HAVE ENOUGH SUNS
                    elif purchase_button_Sunflower.rect.collidepoint(event.pos) and sun_count < Sunflower.COST or purchase_button_Peashotter.rect.collidepoint(event.pos) and sun_count < Peashooter.COST or purchase_button_Wallnutt.rect.collidepoint(event.pos) and sun_count < Wallnutt.COST:
                        not_enough_sun = True
                    #TO MOVE A SUNFLOWER
                    for sunflower in sunflower_list:
                        if sunflower.rect.collidepoint(event.pos) and sunflower.placed == False:
                            sunflower.set_moving(True)
                    #TO MOVE A PEASHOOTER
                    for peashooter in peashooter_list:
                        if peashooter.rect.collidepoint(event.pos) and peashooter.placed == False:
                            peashooter.set_moving(True)
                    #TO MOVE A WALLNUTT
                    for wallnutt in wallnutt_list:
                        if wallnutt.rect.collidepoint(event.pos) and wallnutt.placed == False:
                            wallnutt.set_moving(True)
            # WHEN DRAG
            elif event.type == pygame.MOUSEMOTION:
                #TO MOVE A SUNFLOWER
                for sunflower in sunflower_list:
                    if sunflower.moving:
                        sunflower.move(event.pos[0], event.pos[1])
                #TO MOVE A PEASHOOTER
                for peashooter in peashooter_list:
                    if peashooter.moving:
                        peashooter.move(event.pos[0], event.pos[1])
                #TO MOVE A WALLNUTT
                for wallnutt in wallnutt_list:
                    if wallnutt.moving:
                        wallnutt.move(event.pos[0], event.pos[1])

            #WHEN WE RELEASE THE CLICK
            elif event.type == pygame.MOUSEBUTTONUP:
                for grass in grass_list:
                    #TO MOVE A SUNFLOWER
                    for sunflower in sunflower_list:
                            if sunflower.rect.colliderect(grass.rect):
                                sunflower.rect.x = grass.rect.x
                                sunflower.rect.y = grass.rect.y
                                sunflower.placed = True
                                sunflower.set_moving(False)
                                grass.occupied = True

                    #TO MOVE A PEASHOOTER
                    for peashooter in peashooter_list:
                            if peashooter.rect.colliderect(grass.rect):
                                peashooter.rect.x = grass.rect.x
                                peashooter.rect.y = grass.rect.y
                                peashooter.placed = True
                                peashooter.set_moving(False)
                                grass.occupied = True
                    #TO MOVE A WALLNUTT
                    for wallnutt in wallnutt_list:
                        if wallnutt.moving:
                            wallnutt.set_moving(False)



    screen.fill("orange")

    sprites.draw(screen)
    #TO SHOW THE SUNS COUNT
    screen.blit(sun_count_image, (1150, 20))


    sun_count_text = font_sun_count.render(str(sun_count), True, sun_count_color)
    screen.blit(sun_count_text, (1100, 35))
    #TO SHOW THE TEXT MENU
    if show_text_menu:
        screen.blit(text_surface, text_rect)

    if not_enough_sun:
        not_enough_sun_text = font_sun_count.render("NOT ENOUGH SUNS", True, not_enough_sun_color)
        screen.blit(not_enough_sun_text, (1050, 85))

    if not gameover:
        sprites.update()

    pygame.display.flip()
    clock.tick(configs.FPS)








pygame.quit()

