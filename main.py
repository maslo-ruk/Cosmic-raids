import pygame
from data.platformer import Platformer, Scene, Hub
from data.player import Player, Hub_Player
from data.menu_test_file import Menu
from data.sound_function import sound
from data.end_of_testfile import The_end
from data.platformer import Platformer
from data.functions import *
from data.gildia_test_file import Gildia
from data.config import *


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
    player = Hub_Player((300, 200))
    menu_ecr = Menu(width, height, screen, player)
    running = True
    while running:
        menu_ecr.run()

def main():
    pygame.init()
    size = width, height = 1500, 900
    screen_info = pygame.display.Info()  # узнаем размеры экрана пользователя
    e_width = screen_info.current_w - 30  # ширина
    e_height = screen_info.current_h - 30
    screen = pygame.display.set_mode((e_width, e_height))
    # screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("CosmicRaids")
    player = Player((300, 200))
    player.level = get_level()
    hub_player = Hub_Player((300, 200))
    menu = Menu(e_width, e_height, screen, hub_player)
    hub = Hub(menu.size, screen, clock, hub_player)
    gildia = Gildia(e_width, e_height, screen)
    current_scene = menu
    scenes = []
    scenes.append(current_scene)
    runi = True
    sound = 'sounds/cosmic_battle.mp3'
    pygame.mixer.Sound(sound).play(-1)
    pygame.mixer.Sound(sound).set_volume(1.0)
    while runi:
        a = current_scene.run(sound)
        if a == 1:
            current_scene = Platformer((width, height), screen, clock, player)
            scenes.append(current_scene)
            # screen = pygame.display.set_mode(size)
        elif a == 2:
            current_scene = Scene((3000, 1200), screen, clock, player)
        elif a == 3:
            continue
        elif a == 4:
            current_scene = hub
        elif a == 5:
            current_scene = gildia
        elif a == 6:
            current_scene = The_end((width, height), screen, player)
    pygame.quit()


if __name__ == '__main__':
    main()
