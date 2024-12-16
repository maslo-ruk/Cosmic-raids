import pygame
from data.player import Player
from data.Block import Block
from data.Projectiles import Bullets

pygame.init()


class Scene:
    def __init__(self, size, screen, clock):
        self.size = size
        self.screen = screen
        self.clock = clock


class Platformer(Scene):
    def __init__(self, size, screen, clock):
        super().__init__(size, screen, clock)
        self.player = Player()
        self.map = []
        self.blocks = pygame.sprite.Group()

    def make_map(self):
        self.map = ['------------------------------',
                    '-0000000000000000000000000000-',
                    '-0000000000000000000000000000-',
                    '-0000000-------00000000000000-',
                    '-0000000000000000000000000000-',
                    '-0000000000000000000000000000-',
                    '---00000000000000000000000000-',
                    '-0000000000000000000000000000-',
                    '-0000000000000000000000000000-',
                    '-000000000---0000000000000000-',
                    '-0000000000000000000000000----',
                    '-00000000000000---00000000000-',
                    '-00000000000000000000----0000-',
                    '-0000000000000000000000000000-',
                    '-0000000000000000000000000000-',
                    '-0000000-----0000000000000000-',
                    '-0000000000000000000000000000-',
                    '-0000000000000000000000000000-',
                    '-0000000000000000000000000000-',
                    '------------------------------']
        for i in range(len(self.map)):
            string = self.map[i]
            for j in range(len(string)):
                pos = (j * 30, i * 30)
                if string[j] == '-':
                    block = Block(pos, self.screen)
                    self.blocks.add(block)

    def run(self):
        self.make_map()
        running = True
        all_b = pygame.sprite.Group()
        lines = pygame.sprite.Group()
        right = False
        left = False
        up = False
        while running:
            tick = self.clock.tick(60)
            self.screen.fill('blue')
            self.blocks.draw(self.screen)
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        dx = mouse_x - self.player.rect.x
                        dy = mouse_y - self.player.rect.y
                        angle = (dx, dy)
                        if dx != 0 or dy != 0:  # Проверка для избежания деления на ноль
                            norm = (dx ** 2 + dy ** 2) ** 0.5
                            direction = (dx / norm, dy / norm)
                            line = Bullets(self.player.rect.center, direction)
                            all_b.add(line)
                            lines.add(line)
            if keys[pygame.K_d]:
                right = True
            else:
                right = False
            if keys[pygame.K_a]:
                left = True
            else:
                left = False
            if keys[pygame.K_SPACE]:
                up = True
            else:
                up = False

            all_b.draw(self.screen)
            self.player.update(right, left, up, self.blocks)
            self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
            lines.update(self.blocks)
            pygame.display.flip()
        pygame.quit()
