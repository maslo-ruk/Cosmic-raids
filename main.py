import pygame
from data.menu_test_file import menu_ecr


if __name__ == '__main__':
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
    running = True
    while running:
        menu_ecr().run()