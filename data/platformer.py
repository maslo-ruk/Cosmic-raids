import pygame
from data.player import Player, Enemy
from data.Block import Block
from data.Projectiles import Bullets
from data.map_generator import *

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
        self.MOVEEVENT = pygame.USEREVENT + 1
        self.RELOADEVENT = pygame.USEREVENT + 1

    def make_map(self):
        self.map_y = []
        for i in range(self.size[1] // 30):
            if i == 0 or i == self.size[1] // 30 - 1:
                self.map_y.append('#' * (self.size[0] // 30))
            else:
                self.map_y.append('#' + '0'* (self.size[0] // 30 - 2) + '#')
        room = Room(self.size[0] // 30, self.size[1] // 30, (0, 0), (25, 25))
        strategy = Platforms(room, 5)
        self.map_x = strategy.all()
        self.map = []
        for i in self.map_y:
            print(i)
        for i in range(len(self.map_x)):
            new_str = ''
            for j in range(len(self.map_x[i])):
                if self.map_x[i][j] == '#':
                    new_str += self.map_x[i][j]
                else:
                    new_str += self.map_y[i][j]
            self.map.append(new_str)
        for i in range(len(self.map)):
            string = self.map[i]
            for j in range(len(string)):
                pos = (j * 30, i * 30)
                if string[j] == '-' or string[j] == '#':
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
        pygame.time.set_timer(self.MOVEEVENT, 2000)
        pygame.time.set_timer(self.RELOADEVENT, 2000)
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
                    if event.button == 1 and self.player.count > 0:
                        dest_x, dest_y = pygame.mouse.get_pos()
                        self.player.shoot(dest_x, dest_y)
                        self.player.count -= 1
                if event.type == self.SHOOTEVENT and self.player.is_alive:
                    for i in self.Enemies:
                        if i.see_player:
                            i.shoot(self.player.rect.x, self.player.rect.y)
                if event.type == self.MOVEEVENT:
                    for i in self.Enemies:
                        if not i.unseed:
                            i.random_move()
                if event.type == self.RELOADEVENT and self.player.count < self.player.kolvo:
                    self.player.count += 1
                    print(self.player.count)
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
            # if keys[pygame.K_r]:
            #     self.player.count = self.player.kolvo


            if self.player.is_alive:
                self.player.update(self.screen, right, left, up, self.blocks)
                self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
            for i in self.Enemies:
                i.update(self.screen, self.blocks, self.player.rect)
                self.screen.blit(i.image, (i.rect.x, i.rect.y))
            pygame.display.flip()
        pygame.quit()
