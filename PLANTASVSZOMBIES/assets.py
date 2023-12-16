import os
import pygame

images = {}
gifs = {}

def load_images():
    path = os.path.join("assets", "images")
    for file in os.listdir(path):
        images[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))
        
def get_image(name):
    return images[name]

def load_gif():
    path = os.path.join("assets", "gif")
    for file in os.listdir(path):
        gifs[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))

def get_gif(name):
    return gifs[name]