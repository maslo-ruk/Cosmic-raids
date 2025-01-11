import pygame
from data.platformer import Platformer, Hub


def main():
    pygame.init()
    size = width, height = 1500, 900
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("CosmicRaids")
    current_scene = Hub(size, screen, clock)
    runi = True
    while runi:
        current_scene.run()
    pygame.quit()


if __name__ == '__main__':
    main() 
