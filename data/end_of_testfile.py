from data.buttons import Button
from data.platformer import *
from data.map_generator import *
class The_end(Scene):
    def __init__(self, size, screen, player):
        self.width = size[0]
        self.height = size[1]
        self.screen = screen
        self.size = self.width, self.height
        self.player = player
        self.font = pygame.font.Font(None, 60)
        self.text1 = self.font.render('Hello Привет', 1, 'purple')
    def run(self, sound):
        fon = pygame.image.load("images/end_of/fon.png").convert()
        fon = pygame.transform.scale(fon, (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        next_to_hub = Button(0, 0, self.width, self.height, '', "images/end_of/next.png",
                              "images/end_of/next.png", '',
                              (810 * (self.width / 1536), 1474 * (self.width / 1536)),
                              (695 * (self.height / 864), 820 * (self.height / 854)))

        clock = pygame.time.Clock()
        pygame.display.set_caption("Тестовое меню")
        running = True
        text1 = self.font.render(str(self.player.total_score), 1, 'purple')
        text2 = self.font.render(str(self.player.shots), 1, 'purple')
        text3 = self.font.render(str(self.player.health_lost), 1, 'purple')
        text4 = self.font.render(str(round(self.player.time / 60)), 1, 'purple')
        self.player.levels_passed = 0
        while running:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    print(event.pos)
                    if next_to_hub.events():
                        return 4
                if event.type == pygame.MOUSEMOTION:
                    x_pos = event.pos
                    next_to_hub.check_mishka(x_pos)
            self.screen.blit(fon, (0, 0))
            self.screen.blit(text1, (1490, 250))
            self.screen.blit(text2, (1490, 370))
            self.screen.blit(text3, (1490, 490))
            self.screen.blit(text4, (1490, 610))
            # Дальше идут важные кнопки для самой игры
            next_to_hub.draw(self.screen)
            pygame.display.flip()
            dt = clock.tick(100) / 1000
