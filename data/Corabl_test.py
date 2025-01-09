# Тест меню
import pygame
from data.buttons import Button
from data.sound_function import sound
class Hub:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen

    def run(self):
        fon = pygame.image.load("images/for_hub/hub_pic_test1.png")
        fon = pygame.transform.scale(fon, (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        pet = pygame.image.load("images/for_hub/pet_pose_normal.png")
        pet = pygame.transform.scale(pet, (self.width, self.height))
        self.screen.blit(pet, (0, 0))
        nouneim = pygame.image.load("images/for_hub/who_normal.png")
        nouneim = pygame.transform.scale(nouneim, (self.width, self.height))
        self.screen.blit(nouneim, (0, 0))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Тестовое меню")
        running = True
        while running:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    exit()
                    # выход через esc
            self.screen.blit(fon, (0, 0))
            self.screen.blit(pet, (0, 0))
            self.screen.blit(nouneim, (0, 0))
            pygame.display.flip()
            dt = clock.tick(100) / 1000
