# Тест меню
import pygame
from data.buttons import Button
from data.platformer import Hub
class Gildia:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen
        self.size = self.width, self.height

    def run(self):
        fon = pygame.image.load("images/for_gildia/gildia.png")
        fon = pygame.transform.scale(fon, (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        shop_button = Button(0, 0, self.width, self.height, '', "images/for_gildia/shop_button.png",
                              "images/for_gildia/shop_button.png", '',
                              (1050 * (self.width / 1536), 1318 * (self.width / 1536)),
                              (442 * (self.height / 864), 623 * (self.height / 854)))
        zadania_button = Button(0, 0, self.width, self.height, '', "images/for_gildia/zadania_button.png",
                                 "images/for_gildia/zadania_button.png", '',
                                 (1050 * (self.width / 1536), 1318 * (self.width / 1536)),
                                 (169 * (self.height / 864), 348 * (self.height / 864)))
        putish_button = Button(0, 0, self.width, self.height, '', "images/for_gildia/putishestvia_button.png",
                                 "images/for_gildia/putishestvia_button.png", '',
                                 (244 * (self.width / 1536), 511 * (self.width / 1536)),
                                 (442 * (self.height / 864), 623 * (self.height / 864)))
        dostig_button = Button(0, 0, self.width, self.height, '', "images/for_gildia/dostig_button.png",
                               "images/for_gildia/dostig_button.png", '',
                               (244 * (self.width / 1536), 511 * (self.width / 1536)),
                               (169 * (self.height / 864), 348 * (self.height / 864)))
        person_click =
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
                    zadania_button.events()
                    shop_button.events()
                    putish_button.events()
                    dostig_button.events()
                if event.type == pygame.MOUSEMOTION:
                    x_pos = event.pos
                    zadania_button.check_mishka(x_pos)
                    shop_button.check_mishka(x_pos)
                    putish_button.check_mishka(x_pos)
                    dostig_button.check_mishka(x_pos)

                    # выход через esc
            self.screen.blit(fon, (0, 0))
            # Дальше идут важные кнопки для самой игры
            zadania_button.draw(self.screen)
            shop_button.draw(self.screen)
            putish_button.draw(self.screen)
            dostig_button.draw(self.screen)
            pygame.display.flip()
            dt = clock.tick(100) / 1000
