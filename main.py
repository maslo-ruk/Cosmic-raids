import pygame
from data.menu_test_file import Menu
from data.sound_function import sound
from data.platformer import Platformer


def main_lena():
    pygame.init()
    screen_info = pygame.display.Info()  # узнаем размеры экрана пользователя
    width = screen_info.current_w  # ширина
    height = screen_info.current_h  # высота
    increase_byx = (width / 631)  # увеличение по x и y
    increase_byy = (height / 330)
    # print("Ширина экрана:", width)
    # print("Высота экрана:", height)
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Тестовое меню")
    menu_ecr = Menu(width, height, screen)
    running = True
    while running:
        menu_ecr.run()

def main():
    pygame.init()
    size = width, height = 2500, 900
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("CosmicRaids")
    current_scene = Platformer(size, screen, clock)
    runi = True
    while runi:
        current_scene.run()
    pygame.quit()
#у меня другой мейн, я оставил твой, позже договоримся

if __name__ == '__main__':
    main_lena()
