import pygame
from data.platformer import Platformer

def main():
    pygame.init()
    size = width, height = 900, 600
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("CosmicRaids")
    current_scene = Platformer(size, screen, clock)
    runi = True
    while runi:
        current_scene.run()


