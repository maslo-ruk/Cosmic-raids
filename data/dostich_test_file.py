# Тест меню
import pygame
from data.buttons import *
from data.platformer import *
from data.dostig_funk import dostig
class Dostich:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen
        self.size = self.width, self.height

    def run(self, sound):
        fon = pygame.image.load("images/for_dostiz/fon.png").convert_alpha()
        fon = pygame.transform.scale(fon, (self.width, self.height))
        knopochka = pygame.image.load("images/for_dostiz/knopochka.png").convert_alpha()
        knopochka = pygame.transform.scale(knopochka, (self.width, self.height))
        if "охотник I" in str(dostig):
            oxotnik_1 = pygame.image.load("images/for_dostiz/dst1_2.png").convert_alpha()
        else:
            oxotnik_1 = pygame.image.load("images/for_dostiz/dst1_1.png").convert_alpha()
        if "охотник II" in str(dostig):
            oxotnik_2 = pygame.image.load("images/for_dostiz/dst2_2.png").convert_alpha()
        else:
            oxotnik_2 = pygame.image.load("images/for_dostiz/dst2_1.png").convert_alpha()
        if "охотник III" in str(dostig):
            oxotnik_3 = pygame.image.load("images/for_dostiz/dst3_2.png").convert_alpha()
        else:
            oxotnik_3 = pygame.image.load("images/for_dostiz/dst3_1.png").convert_alpha() #достижения охотников
        if "динь динь" in str(dostig):
            din_din = pygame.image.load("images/for_dostiz/dst4_2.png").convert_alpha()
        else:
            din_din = pygame.image.load("images/for_dostiz/dst4_1.png").convert_alpha()
        if '"не беси"' in str(dostig):
            ne_beci = pygame.image.load("images/for_dostiz/dst5_2.png").convert_alpha()
        else:
            ne_beci = pygame.image.load("images/for_dostiz/dst5_1.png").convert_alpha()
        if "~(o.o)~" in str(dostig):
            morda = pygame.image.load("images/for_dostiz/dst6_2.png").convert_alpha()
        else:
            morda = pygame.image.load("images/for_dostiz/dst6_1.png").convert_alpha()
        if "герой без щита" in str(dostig):
            hero = pygame.image.load("images/for_dostiz/dst9_2.png").convert_alpha()
        else:
            hero = pygame.image.load("images/for_dostiz/dst9_1.png").convert_alpha()
        if "полная команда" in str(dostig):
            all_t = pygame.image.load("images/for_dostiz/dst8_2.png").convert_alpha()
        else:
            all_t = pygame.image.load("images/for_dostiz/dst8_1.png").convert_alpha()
        if "каждый день одно и тоже..." in str(dostig):
            k_d = pygame.image.load("images/for_dostiz/dst7_2.png").convert_alpha()
        else:
            k_d = pygame.image.load("images/for_dostiz/dst7_1.png").convert_alpha()

        self.screen.blit(oxotnik_1, (0, 0))
        self.screen.blit(oxotnik_2, (0, 0))
        self.screen.blit(oxotnik_3, (0, 0))
        self.screen.blit(din_din, (0, 0))
        self.screen.blit(fon, (0, 0))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Достижения")
        running = True
        while running:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if keys[pygame.K_ESCAPE]:
                    return 4
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pass
                if event.type == pygame.MOUSEMOTION:
                    x_pos = event.pos
                    pass
            if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                rule = False
                didnt = False
                    # выход через esc
            self.screen.blit(fon, (0, 0))
            self.screen.blit(oxotnik_1, (0, 0))
            self.screen.blit(oxotnik_2, (0, 0))
            self.screen.blit(oxotnik_3, (0, 0))
            self.screen.blit(din_din, (0, 0))
            self.screen.blit(ne_beci, (0, 0))
            self.screen.blit(morda, (0, 0))
            self.screen.blit(hero, (0, 0))
            self.screen.blit(all_t, (0, 0))
            self.screen.blit(k_d, (0, 0))
            self.screen.blit(knopochka, (0, 0)) #пока что функция недоступна
            # Дальше идут важные кнопки для самой игры
            pygame.display.flip()
            dt = clock.tick(100) / 1000
