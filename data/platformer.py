import pygame
from data.player import Player, Enemy
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
        self.player = Player((300, 200))
        self.Enemies = pygame.sprite.Group()
        self.map = []
        self.all_collides = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.blocks_map = pygame.sprite.Group()
        self.SHOOTEVENT = pygame.USEREVENT + 1

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
                    self.blocks_map.add(block)

    def run(self):
        self.make_map()
        enemy = Enemy((600, 510))
        self.Enemies.add(enemy)
        self.blocks.add(self.player)
        for i in self.Enemies:
            self.blocks.add(i)
        running = True
        all_b = pygame.sprite.Group()
        lines = pygame.sprite.Group()
        right = False
        left = False
        up = False
        pygame.time.set_timer(self.SHOOTEVENT, 1000)
        while running:
            tick = self.clock.tick(60)
            self.screen.fill('blue')
            self.blocks_map.draw(self.screen)
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # mouse_x, mouse_y = pygame.mouse.get_pos()
                        # dx = mouse_x - self.player.rect.x
                        # dy = mouse_y - self.player.rect.y
                        # angle = (dx, dy)
                        # if dx != 0 or dy != 0:  # Проверка для избежания деления на ноль
                        #     norm = (dx ** 2 + dy ** 2) ** 0.5
                        #     direction = (dx / norm, dy / norm)
                        #     line = Bullets(self.player.rect.center, direction)
                        #     all_b.add(line)
                        #     lines.add(line)
                        dest_x, dest_y = pygame.mouse.get_pos()
                        self.player.shoot(dest_x, dest_y)
                if event.type == self.SHOOTEVENT:
                    for i in self.Enemies:
                        i.shoot(self.player.rect.x, self.player.rect.y)
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

            self.player.update(self.screen, right, left, up, self.blocks)
            for i in self.Enemies:
                i.update(self.screen, self.blocks)
                self.screen.blit(i.image, (i.rect.x, i.rect.y))
            self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
            pygame.display.flip()
            print(self.player.hp)
            for i in self.Enemies:
                print(i.hp)
        pygame.quit()
