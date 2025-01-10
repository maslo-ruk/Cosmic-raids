# Тест меню
import pygame
from data.buttons import Button
from data.sound_function import sound
from data.Corabl_test import Hub
class Menu:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen

    def run(self):
        fon = pygame.image.load("images/for_menu/Space_sky.png")
        fon = pygame.transform.scale(fon, (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        planet1 = pygame.image.load("images/for_menu/planet.png")
        planet1 = pygame.transform.scale(planet1, (self.width, self.height))
        self.screen.blit(planet1, (0, 0))
        planet2 = pygame.image.load("images/for_menu/planet2.png")
        planet2 = pygame.transform.scale(planet2, (self.width, self.height))
        self.screen.blit(planet2, (0, 0))
        galaktika1 = pygame.image.load("images/for_menu/Galactika1.png")
        galaktika1 = pygame.transform.scale(galaktika1, (self.width - 50, self.height - 50))
        self.screen.blit(galaktika1, (0, 0))
        galaktika2 = pygame.image.load("images/for_menu/galactika2.png")
        galaktika2 = pygame.transform.scale(galaktika2, (self.width, self.height))
        self.screen.blit(galaktika2, (0, 0))
        planet2 = pygame.image.load("images/for_menu/planet2.png")
        planet2 = pygame.transform.scale(planet2, (self.width, self.height))
        self.screen.blit(planet2, (0, 0))
        planetka = pygame.image.load("images/for_menu/mini_planetka.png")
        planetka = pygame.transform.scale(planetka, (self.width, self.height))
        self.screen.blit(planetka, (0, 0))
        exit_esc = pygame.image.load("images/for_menu/Exit.png")
        exit_esc = pygame.transform.scale(exit_esc, (self.width, self.height))
        self.screen.blit(exit_esc, (0, 0))

        start_button = Button(0, 0, self.width, self.height, '', "images/for_menu/start_textures.png",
                              "images/for_menu/start_textures2.png", '',
                              (643 * (self.width / 1536), 893 * (self.width / 1536)),
                              (307 * (self.height / 864), 578 * (self.height / 854)))
        new_game_button = Button(0, 0, self.width, self.height, '', "images/for_menu/newGametextures.png",
                                 "images/for_menu/newGametextures2.png", '',
                                 (610 * (self.width / 1536), 922 * (self.width / 1536)),
                                 (612 * (self.height / 864), 727 * (self.height / 864)))
        settings_button = Button(0, 0, self.width, self.height, '', "images/for_menu/menu_textures.png",
                                 "images/for_menu/menu_textures2.png", '',
                                 (37 * (self.width / 1536), 143 * (self.width / 1536)),
                                 (40 * (self.height / 864), 154 * (self.height / 864)))
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
                        swe = Hub(self.width, self.height, self.screen)
                        swe.run()
                if event.type == pygame.MOUSEMOTION:
                    x_pos = event.pos
                    start_button.check_mishka(x_pos)
                    new_game_button.check_mishka(x_pos)
                    settings_button.check_mishka(x_pos)

                    # выход через esc
            self.screen.blit(fon, (0, 0))
            self.screen.blit(planet1, (0, 0))
            self.screen.blit(planet1, (0, 0))
            self.screen.blit(planet2, (0, 0))
            self.screen.blit(galaktika1, (0, 0))
            self.screen.blit(galaktika2, (0, 0))
            self.screen.blit(planet2, (0, 0))
            self.screen.blit(planetka, (0, 0))
            self.screen.blit(exit_esc, (0, 0))
            # Дальше идут важные кнопки для самой игры
            start_button.draw(self.screen)
            new_game_button.draw(self.screen)
            settings_button.draw(self.screen)
            pygame.display.flip()
            dt = clock.tick(100) / 1000
