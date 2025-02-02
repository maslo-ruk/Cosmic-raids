import pygame
from data.platformer import Platformer, Scene
from data.player import Player, Hub_Player
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
    player = Hub_Player((300, 200))
    menu_ecr = Menu(width, height, screen, player)
    running = True
    while running:
        menu_ecr.run()

def main():
    pygame.init()
    size = width, height = 1500, 900
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("CosmicRaids")
    player = Player((300, 200))
    current_scene = Platformer((3000, 1200), screen, clock, player)
    scenes = []
    scenes.append(current_scene)
    runi = True
    sound = 'sounds/cosmic_battle.mp3'
    pygame.mixer.Sound(sound).play(-1)
    pygame.mixer.Sound(sound).set_volume(1.0)
    while runi:
        a = current_scene.run(sound)
        if a == 1:
            current_scene = Platformer((3000, 1200), screen, clock, player)
            scenes.append(current_scene)
        elif a == 2:
            current_scene = Scene((3000, 1200), screen, clock, player)
    pygame.quit()


if __name__ == '__main__':
    main_lena()
