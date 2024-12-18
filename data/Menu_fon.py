import pygame
class Menu_Fon:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.increase_w = (weight / 631)
        self.increase_h = (height / 330)
        print(weight, height, self.increase_h, self.increase_w)
    def draw_Menu(self):
        pass



# pygame.init()
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#
# clock = pygame.time.Clock()
# pygame.display.set_caption("Тестовое меню")
# running = True
# lines = pygame.sprite.Group()
# all_b = pygame.sprite.Group()
# # all_b.draw(screen)
rec = Menu_Fon(1000, 1000)