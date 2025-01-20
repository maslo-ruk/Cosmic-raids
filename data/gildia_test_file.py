# Тест меню
import pygame
from data.buttons import Button, Block_for_person
from data.platformer import Hub
class Gildia:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen
        self.size = self.width, self.height

    def run(self):
        fon = pygame.image.load("images/for_gildia/gildia.png").convert_alpha()
        fon = pygame.transform.scale(fon, (self.width, self.height))
        rules = pygame.image.load("images/for_gildia/rules.png")
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
        person_click = Block_for_person(0, 0, self.width, self.height, '', "images/for_gildia/calm_Tih.png",
                                 "images/for_gildia/angry_Tih.png", "images/for_gildia/love_Tih.png", '', '',
                                 (544 * (self.width / 1536), 1030 * (self.width / 1536)),
                                 (220 * (self.height / 864), 660 * (self.height / 864)), False)
        back_button = Button(0, 0, self.width, self.height, '', "images/for_gildia/back_plz.png",
                               "images/for_gildia/back_plz.png", '',
                               (1217 * (self.width / 1536), 1478 * (self.width / 1536)),
                               (41 * (self.height / 864), 86 * (self.height / 864)))
        name_button = Button(0, 0, self.width, self.height, '', "images/for_gildia/name_of.png",
                               "images/for_gildia/name_of.png", '',
                               (499 * (self.width / 1536), 1064 * (self.width / 1536)),
                               (33 * (self.height / 864), 97 * (self.height / 864)))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Тестовое меню")
        running = True
        rule = False


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
                    person_click.events()
                    person_click.clicking()
                    back_button.events()
                    if back_button.events():
                        current_scene = Hub(self.size, self.screen, clock)
                        runi = True
                        while runi:
                            current_scene.run()
                        pygame.quit()
                    elif name_button.events():
                        rules = pygame.transform.scale(rules, (self.width, self.height))
                        rule = True
                if event.type == pygame.MOUSEMOTION:
                    x_pos = event.pos
                    zadania_button.check_mishka(x_pos)
                    shop_button.check_mishka(x_pos)
                    putish_button.check_mishka(x_pos)
                    dostig_button.check_mishka(x_pos)
                    person_click.check_mishka(x_pos)
                    back_button.check_mishka(x_pos)
                    name_button.check_mishka(x_pos)
            if keys[pygame.K_SPACE]:
                rule = False
                    # выход через esc
            self.screen.blit(fon, (0, 0))
            # Дальше идут важные кнопки для самой игры
            zadania_button.draw(self.screen)
            shop_button.draw(self.screen)
            putish_button.draw(self.screen)
            dostig_button.draw(self.screen)
            person_click.draw(self.screen)
            back_button.draw(self.screen)
            name_button.draw(self.screen)
            if rule:
                self.screen.blit(rules, (0, 0))
            pygame.display.flip()
            dt = clock.tick(100) / 1000
