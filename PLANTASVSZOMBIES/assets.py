import os
import pygame

images = {}

def load_images():
    path = os.path.join("assets", "images")
    for file in os.listdir(path):
        images[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))
        
def get_image(name):
    return images[name]