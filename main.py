import pygame
from data.platformer import Platformer, Scene, Hub
from data.player import Player, Hub_Player
from data.menu_test_file import Menu
from data.sound_function import sound
from data.end_of_testfile import The_end
from data.platformer import Platformer
from data.functions import *
from data.gildia_test_file import Gildia
from data.settings import Settings
from data.dostich_test_file import Dostich
from data.config import *

def main():
    pygame.init()
    size = width, height = 1500, 900
    screen_info = pygame.display.Info()
    # узнаем размеры экрана пользователя
    e_width = screen_info.current_w  # ширина
    e_height = screen_info.current_h
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
    settings = Settings((e_width, e_height), screen, player)
    current_scene = menu
    scenes = []
    scenes.append(current_scene)
    runi = True
    pygame.mixer.music.load('sounds/DORA_bg.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1.0)
    while runi:
        # if current_scene == settings:

        a = current_scene.run(sound)
        if a == 1:
            player.is_alive = True
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds/cosmic_battle.mp3')
            pygame.mixer.music.play(-1)
            current_scene = Platformer((width, height), screen, clock, player)
            scenes.append(current_scene)
            # screen = pygame.display.set_mode(size)
        elif a == 2:
            current_scene = Scene((3000, 800), screen, clock, player)
        elif a == 3:
            continue
        elif a == 4:
            current_scene = hub
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds/DORA_bg.mp3')
            pygame.mixer.music.play(-1)
        elif a == 5:
            current_scene = gildia
        elif a == 6:
            current_scene = The_end((e_width, e_height), screen, player)
        elif a == 7:
            current_scene = settings
        elif a == 8:
            current_scene = menu
        elif a == 9:
            current_scene = Dostich(e_width, e_height, screen, player)
    pygame.quit()

try:
    if __name__ == '__main__':
        main()
except Exception as e:
    print(e)
