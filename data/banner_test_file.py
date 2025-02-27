#тест среда для баннера
import pygame
from data.buttons import Button
from data.test_garant import Wishes, Crutki

class Banner:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen
    def run(self):
        crutki = Crutki()
        fon = pygame.image.load("images/for_banner/fone_for_banner_test.png")
        fon = pygame.transform.scale(fon, (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        banner = pygame.image.load("images/for_banner/place_for_character_test.png")
        banner = pygame.transform.scale(banner, (self.width, self.height))
        self.screen.blit(banner, (0, 0))
        do_it_1 = Button(0, 0, self.width, self.height, '', "images/for_banner/do_it_1_test.png",
                         "images/for_banner/do_it_1_test2.png", '',
                         (486 * (self.width / 1536), 952 * (self.width / 1536)), (707 * (self.height / 864), 794 * (self.height / 854)))
        do_it_10 = Button(0, 0, self.width, self.height, '', "images/for_banner/do_it_10_test.png",
                          "images/for_banner/do_it_10_test2.png", '',
                          (998 * (self.width / 1536), 1462 * (self.width / 1536)), (707 * (self.height / 864), 794 * (self.height / 854)))
        shoping = Button(0, 0, self.width, self.height, '', "images/for_banner/shop_test.png",
                         "images/for_banner/shop_test2.png", '',
                         (65 * (self.width / 1536), 306 * (self.width / 1536)), (707 * (self.height / 864), 794 * (self.height / 854)))
        close = Button(0, 0, self.width, self.height, '', "images/for_banner/close_butn.png",
                       "images/for_banner/close_butn2.png", '',
                       (11 * (self.width / 1536), 63 * (self.width / 1536)), (6 * (self.height / 864), 66 * (self.height / 854)))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Тестовый баннер")
        running = True
        while running:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    close.events()
                    do_it_1.events()
                    if close.events():
                        pass

                    elif do_it_1.events():
                        crutki.do_it_1()
                    elif do_it_10.events():
                        crutki.do_it_10()
                shoping.events()
                close.events()
                # выход через esc
            self.screen.blit(fon, (0, 0))
            self.screen.blit(banner, (0, 0))
            do_it_1.check_mishka(pygame.mouse.get_pos())
            do_it_1.draw(self.screen)
            do_it_10.check_mishka(pygame.mouse.get_pos())
            do_it_10.draw(self.screen)
            shoping.check_mishka(pygame.mouse.get_pos())
            shoping.draw(self.screen)
            close.check_mishka(pygame.mouse.get_pos())
            close.draw(self.screen)
            pygame.display.flip()
            dt = clock.tick(30) / 1000