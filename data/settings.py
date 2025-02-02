# Тест меню
import pygame
from data.buttons import Button
from data.platformer import *
from data.map_generator import *

class Settings(Scene):
    def __init__(self, size, screen, clock):
        self.width = size[0]
        self.height = size[1]
        self.screen = screen
        self.size = self.width, self.height


    def run(self):
        fon = pygame.image.load("images/settings/fon.png").convert()
        fon = pygame.transform.scale(fon, (self.width, self.height))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Настройки")
        running = True


        while running:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    exit()
                # elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #     start_button.events()
                #     new_game_button.events()
                #     settings_button.events()
                #     if start_button.events():
                #         current_scene = Hub(self.size, self.screen, clock)
                #         runi = True
                #         while runi:
                #             current_scene.run()
                #         pygame.quit()
                # if event.type == pygame.MOUSEMOTION:
                #     x_pos = event.pos
                #     start_button.check_mishka(x_pos)
                #     new_game_button.check_mishka(x_pos)
                #     settings_button.check_mishka(x_pos)

                    # выход через esc
            self.screen.blit(fon, (0, 0))
            # Дальше идут важные кнопки для самой игры
            pygame.display.flip()
            dt = clock.tick(100) / 1000
