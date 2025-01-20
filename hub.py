import pygame
from data.platformer import Platformer
from data.gildia_test_file import Gildia
from data.menu_test_file import Menu


def main():
    pygame.init()
    screen_info = pygame.display.Info()
    width = screen_info.current_w  # ширина
    height = screen_info.current_h
    size = width, height
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("CosmicRaids")
    menu_ecr = Menu(width, height, screen)
    running = True
    while running:
        menu_ecr.run()


if __name__ == '__main__':
    main()
