# Тест меню
import pygame
from data.buttons import *
from data.platformer import *
from data.map_generator import *

class Settings(Scene):
    def __init__(self, size, screen, clock):
        self.width = size[0]
        self.height = size[1]
        self.screen = screen
        self.size = self.width, self.height
        self.zvuk = False


    def run(self, sound):
        fon = pygame.image.load("images/settings/fon.png").convert()
        fon = pygame.transform.scale(fon, (self.width, self.height))
        print(self.zvuk, 'adad')
        zvuk_button = Buttton_for_settings(0, 0, self.width, self.height, '', "images/settings/zvuk_3.png",
                                           "images/settings/zvuk_4.png","images/settings/zvuk_1.png",
                                           "images/settings/zvuk_2.png",
                                           '', '', (251 * (self.width / 1536), 384 * (self.width / 1536)),
                                           (248 * (self.height / 864), 382 * (self.height / 854)))
        if not self.zvuk:
            zvuk_button.clicked = 1
        chiti = Button(0, 0, self.width, self.height, '', "images/settings/chit_kod.png",
                                 "images/settings/chit_kod.png", '',
                                 (610 * (self.width / 1536), 922 * (self.width / 1536)),
                                 (612 * (self.height / 864), 727 * (self.height / 864)))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Настройки")
        running = True
        while running:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 8
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    zvuk_button.events()
                    self.zvuk = zvuk_button.clicking()
                    print(self.zvuk)
                    if chiti.events():
                        raise Exception("читы - бан (ошибка вызвана специально)")
                    if not self.zvuk:
                        pygame.mixer.music.stop()
                    if self.zvuk:
                        pygame.mixer.music.load('sounds/DORA_bg.mp3')
                        pygame.mixer.music.play(-1)
                if event.type == pygame.MOUSEMOTION:
                    x_pos = event.pos
                    zvuk_button.check_mishka(x_pos)
                    chiti.check_mishka(x_pos)
                    # выход через esc
            self.screen.blit(fon, (0, 0))
            zvuk_button.draw(self.screen)
            chiti.draw(self.screen)
            # Дальше идут важные кнопки для самой игры
            pygame.display.flip()
            dt = clock.tick(100) / 1000
