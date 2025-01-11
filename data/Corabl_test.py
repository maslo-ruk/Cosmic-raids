# Тест меню
import pygame
from data.buttons import Button
from data.banner_test_file import Banner
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

        banner_button = Button(0, 0, self.width, self.height, '', "images/for_hub/test_button_for_banner.png",
                              "images/for_hub/test_button_for_banner.png", '',
                              (1369 * (self.width / 1536), 1500 * (self.width / 1536)),
                              (16 * (self.height / 864), 77 * (self.height / 854)))
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
                    banner_button.events()
                    if banner_button.events():
                        banner = Banner(self.width, self.height, self.screen)
                        banner.run()
                if event.type == pygame.MOUSEMOTION:
                        x_pos = event.pos
                        banner_button.check_mishka(x_pos)

                    # выход через esc
            self.screen.blit(fon, (0, 0))
            self.screen.blit(pet, (0, 0))
            self.screen.blit(nouneim, (0, 0))
            banner_button.draw(self.screen)
            pygame.display.flip()
            dt = clock.tick(100) / 1000
