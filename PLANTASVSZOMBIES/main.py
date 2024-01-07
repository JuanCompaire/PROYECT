import pygame
from pygame import font

import assets
import configs
from objects.Background import Background
from objects.Grass import Grass
from objects.Purchase_button import Purchase_button
from objects.Sunflower import Sunflower
from objects.Peashooter import Peashooter
from objects.Wallnutt import Wallnutt
from objects.Sun import Sun
from objects.Shovel import Shovel
from objects.Mower import Mower
from objects.Zombie import Zombie
from objects.Pea import Pea

# TO RUN THE GAME
pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
gameover = False
show_text_menu = False
not_enough_sun = False

assets.load_images()
assets.load_gif()

sprites = pygame.sprite.LayeredUpdates()

# SUNS COUNT
sun_count = 200
sun_count_image = assets.get_image("sol")
sun_count_image = pygame.transform.scale(sun_count_image, (50, 50))
font_sun_count = pygame.font.Font(None, 36)
sun_count_color = (0, 0, 0)
# NOT ENOUGH SUNS INDICATOR
not_enough_sun_color = (255, 0, 0)

# OBJECTS LIST
sunflower_list = []
peashooter_list = []
wallnutt_list = []
sun_generated_list = []
grass_list = []
mower_list = []
zombie_list = []
pea_list = []

moving_plant = None

# ITERATION VARIABLES
NUM_ROW_GRASS = 9;
NUM_COLUMN_GRASS = 5
grass_width = 80
grass_height = 95
start_x = 518
start_y = 243
num_mower = 5
# BACKGROUND
Background(sprites)
# CREATION OF BUTTONS TO BUY PLANTS
purchase_button_Peashotter = Purchase_button(sprites, image_name="planta_militar_compra", X=550, Y=20)
purchase_button_Sunflower = Purchase_button(sprites, image_name="sunflower_purchase", X=700, Y=20)
purchase_button_Wallnutt = Purchase_button(sprites, image_name="wallnutt_purchase", X=850, Y=20)
# CREATION OF THE GRASS SQUARES

for row in range(NUM_COLUMN_GRASS):
    for col in range(NUM_ROW_GRASS):
        grass_number = row * NUM_ROW_GRASS + col + 1
        grass_x = start_x + col * grass_width
        grass_y = start_y + row * grass_height
        new_grass = Grass(sprites, num_grass=grass_number, occupied=False, X=grass_x, Y=grass_y)
        grass_list.append(new_grass)

# CREATION OF THE SHOVEL
shovel_game = Shovel(sprites, X=1290, Y=780, using=False)

# CREATION OF THE MOWERS
for i in range(num_mower):
    new_mower = Mower(sprites, X=450, Y=243 + i * 95, activated=False)
    mower_list.append(new_mower)

# CREATION OF THE ZOMBIES
zombie_spawn = [200, 300, 400, 500, 600]
#CREATE LOGIC TO MAKE ZOMBIES WAVES

zombie_move_counter = 0
zombie_move_frequency = 5

#CREATION OF PEA MUNITION
pea_trial = Pea(sprites, X=600, Y=300)

# FUNCTIONS

# GENERATE SUNFLOWER
def generate_sunflower():
    new_sunflower = Sunflower(sprites, X=720, Y=130, placed=False)
    sunflower_list.append(new_sunflower)

# GENERATE PEASHOOTER
def generate_peashooter():
    new_peashooter = Peashooter(sprites, X=570, Y=130, placed=False)
    peashooter_list.append(new_peashooter)

# GENERATE WALLNUTT
def generate_wallnutt():
    new_wallnutt = Wallnutt(sprites, X=870, Y=130, placed=False)
    wallnutt_list.append(new_wallnutt)

# GENERATE SUNS FROM SUNFLOWERS
def generate_sun():
    for sunflower in sunflower_list:
        if sunflower.generate_sun:
            new_sun = Sun(sprites, X=sunflower.rect.x + 50, Y=sunflower.rect.y - 30)
            sun_generated_list.append(new_sun)
            sunflower.generate_sun = False

#CHECK IF ZOMBIES TOUCH GRASS
def check_zombies_in_grass():
    for grass in grass_list:
        for zombie in zombie_list:
            if grass.rect.colliderect(zombie.rect):
                print("ZOMBIE IN GRASS")

# GAME LOOP
while running:
    if not gameover:
        current_time = pygame.time.get_ticks()

        pea_trial.move()
        check_zombies_in_grass()
        # GENERATE SUN FROM SUNFLOWERS
        for sunflower in sunflower_list:
            sunflower.generate_suns(current_time)
            if sunflower.generate_sun:
                generate_sun()
                sunflower.generate_sun = False
        #ZOMBIES
        zombie_move_counter += 1
        if zombie_move_counter >= zombie_move_frequency:
            for zombie in zombie_list:
                # ALLOW ZOMBIES TO MOVE
                zombie.move()
                #TO CHECK IF ZOMBIE REACH A MOWER
                for mower in mower_list:
                    zombie_rect_collision = pygame.Rect(zombie.rect.x + 10, zombie.rect.y + 15, 115, 115)
                    #hay que modificar donde colisiona con el cortacesped porque la imagen no es el borde como tal
                    if zombie_rect_collision.colliderect(mower.rect):
                        mower.activated = True
                        zombie.kill()
                        zombie_list.remove(zombie)
                        break
            #zombie_move_counter = 0

        #MOWERS
        for mower in mower_list:
            mower.activate()


        # EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # TO GET THE SHOVEL CLICKING ON SHOVEL BUTTON
                    if shovel_button.get_rect(topleft=(1290, 780)).collidepoint(
                            event.pos) and shovel_game.using == False:
                        shovel_game.rect.x = 1290
                        shovel_game.rect.y = 780
                        shovel_game.set_using(True)
                    # TO GET INFO ABOUT GRASS BLOCK
                    for grass in grass_list:
                        if grass.rect.collidepoint(event.pos):
                            print(grass.num_grass)
                            print(grass.occupied)
                    # TO BUY A PLANT
                    # TO GENERATE A SUNFLOWER WHEN WE PURCHASE IT
                    if purchase_button_Sunflower.rect.collidepoint(event.pos) and sun_count >= Sunflower.COST:
                        generate_sunflower()
                        sun_count -= Sunflower.COST
                        not_enough_sun = False
                        # TO GENERATE A PEASHOOTER WHEN WE PURCHASE IT
                    elif purchase_button_Peashotter.rect.collidepoint(event.pos) and sun_count >= Peashooter.COST:
                        generate_peashooter()
                        sun_count -= Peashooter.COST
                        not_enough_sun = False
                    # TO GENERATE A WALLNUTT WHEN WE PURCHASE IT
                    elif purchase_button_Wallnutt.rect.collidepoint(event.pos) and sun_count >= Wallnutt.COST:
                        generate_wallnutt()
                        sun_count -= Wallnutt.COST
                        not_enough_sun = False
                    # WHEN YOU DON´T HAVE ENOUGH SUNS
                    elif purchase_button_Sunflower.rect.collidepoint(
                            event.pos) and sun_count < Sunflower.COST or purchase_button_Peashotter.rect.collidepoint(
                            event.pos) and sun_count < Peashooter.COST or purchase_button_Wallnutt.rect.collidepoint(
                            event.pos) and sun_count < Wallnutt.COST:
                        not_enough_sun = True
                    # TO MOVE PLANTS
                    # TO MOVE A SUNFLOWER
                    for sunflower in sunflower_list:
                        if sunflower.rect.collidepoint(event.pos) and sunflower.placed == False:
                            sunflower.set_moving(True)
                            moving_plant = sunflower
                    # TO MOVE A PEASHOOTER
                    for peashooter in peashooter_list:
                        if peashooter.rect.collidepoint(event.pos) and peashooter.placed == False:
                            peashooter.set_moving(True)
                            moving_plant = peashooter
                    # TO MOVE A WALLNUTT
                    for wallnutt in wallnutt_list:
                        if wallnutt.rect.collidepoint(event.pos) and wallnutt.placed == False:
                            wallnutt.set_moving(True)
                            moving_plant = wallnutt
            # WHEN DRAG
            elif event.type == pygame.MOUSEMOTION:
                # TO MOVE THE SHOVEL
                if shovel_game.using:
                    shovel_game.move(event.pos[0], event.pos[1])
                # TO MOVE A SUNFLOWER
                for sunflower in sunflower_list:
                    if sunflower.moving:
                        sunflower.move(event.pos[0], event.pos[1])
                # TO MOVE A PEASHOOTER
                for peashooter in peashooter_list:
                    if peashooter.moving:
                        peashooter.move(event.pos[0], event.pos[1])
                # TO MOVE A WALLNUTT
                for wallnutt in wallnutt_list:
                    if wallnutt.moving:
                        wallnutt.move(event.pos[0], event.pos[1])
            # WHEN WE RELEASE THE CLICK
            elif event.type == pygame.MOUSEBUTTONUP:
                shovel_collision_rect = pygame.Rect(shovel_game.rect.x + 10, shovel_game.rect.y + 50, 65, 30)
                for grass in grass_list:
                    # TO MOVE A PLANT
                    if moving_plant:
                        if moving_plant.rect.colliderect(grass.rect) and grass.occupied == False:
                            moving_plant.rect.x = grass.rect.x
                            moving_plant.rect.y = grass.rect.y
                            moving_plant.placed = True
                            moving_plant.set_moving(False)
                            grass.occupied = True
                            moving_plant.num_grass = grass.num_grass

                            shovel_game.set_using(False)
                            shovel_game.rect.x = 1290
                            shovel_game.rect.y = 780
                            break
                    #TO REMOVE A PLANT
                    if (shovel_collision_rect.colliderect(grass.rect) and grass.occupied == True):
                        for sunflower in sunflower_list:
                            if sunflower.num_grass == grass.num_grass:
                                sunflower.kill()
                                sunflower_list.remove(sunflower)
                                sun_count += (Sunflower.COST/2)
                                grass.occupied = False
                                break
                        for peashooter in peashooter_list:
                            if peashooter.num_grass == grass.num_grass:
                                peashooter.kill()
                                peashooter_list.remove(peashooter)
                                sun_count += (Peashooter.COST/2)
                                grass.occupied = False
                                break
                        for wallnutt in wallnutt_list:
                            if wallnutt.num_grass == grass.num_grass:
                                wallnutt.kill()
                                wallnutt_list.remove(wallnutt)
                                sun_count += (Wallnutt.COST/2)
                                grass.occupied = False
                                break

                # TO TAKE A SUN WHEN WE CLICK IT
                for sun in sun_generated_list:
                    if sun.rect.collidepoint(event.pos):
                        sun.kill()
                        sun_count += Sun.sun_points
                        sun_generated_list.remove(sun)

                # TO STOP USING THE SHOVEL
                if shovel_game.using:
                    shovel_game.rect.x = 1290
                    shovel_game.rect.y = 780
                    shovel_game.set_using(False)

    # TO SHOW THE BACKGROUND
    screen.fill("orange")

    sprites.draw(screen)
    # TO SHOW THE SUNS COUNT
    screen.blit(sun_count_image, (1150, 20))

    # TO SHOW THE SHOVEL BUTTON
    shovel_button = assets.get_image("pala")
    shovel_button = pygame.transform.scale(shovel_button, (85, 85))
    screen.blit(shovel_button, (1290, 780))

    sun_count_text = font_sun_count.render(str(sun_count), True, sun_count_color)
    screen.blit(sun_count_text, (1100, 35))

    # TO SHOW NOT ENOUGH SUNS
    if not_enough_sun:
        not_enough_sun_text = font_sun_count.render("NOT ENOUGH SUNS", True, not_enough_sun_color)
        screen.blit(not_enough_sun_text, (1050, 85))

    if not gameover:
        sprites.update()

    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()
