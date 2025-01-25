import pygame
from data.platformer import Platformer


def main():
    pygame.init()
    size = width, height = 1500, 900
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("CosmicRaids")
    current_scene = Platformer((3000, 1200), screen, clock)
    runi = True
    while runi:
        current_scene.run()
    pygame.quit()


if __name__ == '__main__':
    main() 
