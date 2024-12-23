# Тест меню
import pygame
from data.buttons import Button
from data.banner_test_file import main_banner

def menu_ecr():
    pygame.init()
    screen_info = pygame.display.Info()  # узнаем размеры экрана пользователя
    width = screen_info.current_w  # ширина
    height = screen_info.current_h  # высота

    increase_byx = (width / 631)  # увеличение по x и y
    increase_byy = (height / 330)
    print("Ширина экрана:", width)
    print("Высота экрана:", height)
    screen = pygame.display.set_mode((width, height))
    fon = pygame.image.load("../images/for_menu/Space_sky.png")
    fon = pygame.transform.scale(fon, (width, height))
    screen.blit(fon, (0, 0))
    planet1 = pygame.image.load("../images/for_menu/planet.png")
    planet1 = pygame.transform.scale(planet1, (width, height))
    screen.blit(planet1, (0, 0))
    planet2 = pygame.image.load("../images/for_menu/planet2.png")
    planet2 = pygame.transform.scale(planet2, (width, height))
    screen.blit(planet2, (0, 0))
    galaktika1 = pygame.image.load("../images/for_menu/Galactika1.png")
    galaktika1 = pygame.transform.scale(galaktika1, (width - 50, height - 50))
    screen.blit(galaktika1, (0, 0))
    galaktika2 = pygame.image.load("../images/for_menu/galactika2.png")
    galaktika2 = pygame.transform.scale(galaktika2, (width, height))
    screen.blit(galaktika2, (0, 0))
    planet2 = pygame.image.load("../images/for_menu/planet2.png")
    planet2 = pygame.transform.scale(planet2, (width, height))
    screen.blit(planet2, (0, 0))
    planetka = pygame.image.load("../images/for_menu/mini_planetka.png")
    planetka = pygame.transform.scale(planetka, (width, height))
    screen.blit(planetka, (0, 0))
    exit_esc = pygame.image.load("../images/for_menu/Exit.png")
    exit_esc = pygame.transform.scale(exit_esc, (width, height))
    screen.blit(exit_esc, (0, 0))

    start_button = Button(0, 0, width, height, '', "../images/for_menu/start_textures.png",
                          "../images/for_menu/start_textures2.png", '',
                          (643 * (width / 1536), 893 * (width / 1536)), (307 * (height / 864), 578 * (height / 854)))
    new_game_button = Button(0, 0, width, height, '', "../images/for_menu/newGametextures.png",
                             "../images/for_menu/newGametextures2.png", '',
                             (610 * (width / 1536), 922 * (width / 1536)), (612 * (height / 864), 727 * (height / 864)))
    settings_button = Button(0, 0, width, height, '', "../images/for_menu/menu_textures.png",
                             "../images/for_menu/menu_textures2.png", '',
                             (37 * (width / 1536), 143 * (width / 1536)), (40 * (height / 864), 154 * (height / 864)))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Тестовое меню")
    running = True

    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                start_button.events()
                new_game_button.events()
                settings_button.events()
                if start_button.events():
                    exit()
            if event.type == pygame.MOUSEMOTION:
                x_pos = event.pos
                start_button.check_mishka(x_pos)
                new_game_button.check_mishka(x_pos)
                settings_button.check_mishka(x_pos)

                # выход через esc
        screen.blit(fon, (0, 0))
        screen.blit(planet1, (0, 0))
        screen.blit(planet1, (0, 0))
        screen.blit(planet2, (0, 0))
        screen.blit(galaktika1, (0, 0))
        screen.blit(galaktika2, (0, 0))
        screen.blit(planet2, (0, 0))
        screen.blit(planetka, (0, 0))
        screen.blit(exit_esc, (0, 0))
        # Дальше идут важные кнопки для самой игры
        start_button.draw(screen)
        new_game_button.draw(screen)
        settings_button.draw(screen)
        pygame.display.flip()
        dt = clock.tick(100) / 1000

    pygame.quit()
if __name__ == '__main__':
    menu_ecr()