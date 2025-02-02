# Тест меню
import pygame
from data.buttons import *
from data.platformer import *
class Dostich:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen
        self.size = self.width, self.height

    def run(self):
        fon = pygame.image.load("images/for_dostiz/fon.png").convert_alpha()
        fon = pygame.transform.scale(fon, (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Достижения")

        while running:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    exit()
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
            # Дальше идут важные кнопки для самой игры
            pygame.display.flip()
            dt = clock.tick(100) / 1000
