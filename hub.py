import pygame
from data.gildia_test_file import Gildia
from data.menu_test_file import Menu
from data.end_of_testfile import The_end
from data.settings import Settings
from data.platformer import *
from data.test_file_delite import *
def main():
    pygame.init()
    screen_info = pygame.display.Info()
    width = screen_info.current_w  # ширина
    height = screen_info.current_h
    size = width, height
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("CosmicRaids")
    menu_ecr = Pausa_lol((width, height), screen, clock)
    running = True
    while running:
        menu_ecr.run()


if __name__ == '__main__':
    main()
