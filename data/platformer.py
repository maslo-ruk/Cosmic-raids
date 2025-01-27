import pygame
from data.player import Player, Enemy
from data.Block import Block
from data.projectiles import Bullets

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
        self.RELOADEVENT = pygame.USEREVENT + 2
        self.MUSICBGEVENT = pygame.USEREVENT + 3
        self.BABAX = pygame.USEREVENT + 4

    def make_map(self):
        self.map = ['------------------------------',
                    '-0000000000000000000000000000-',
                    '-0000000000000000000000000000-',
                    '-0000000000000000000000000000-',
                    '-000000000000-----00000000000-',
                    '-0000000000000000000000000000-',
                    '-----000000000000000000000000-',
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
        count = 0
        sound = 'sounds/DORA_bg.mp3'
        pygame.time.set_timer(self.RELOADEVENT, 2000)
        pygame.time.set_timer(self.SHOOTEVENT, 1000)
        pygame.time.set_timer(self.MUSICBGEVENT, 91000)
        pygame.mixer.Sound(sound).play(-1)
        pygame.mixer.Sound(sound).set_volume(0.3)
        while running:
            self.vzriv = False
            tick = self.clock.tick(60)
            self.screen.fill('blue')
            self.blocks_map.draw(self.screen)
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == self.MUSICBGEVENT:
                    pygame.mixer.Sound(sound).play(-1)
                    pygame.mixer.Sound(sound).set_volume(0.3)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.player.count > 0:
                        dest_x, dest_y = pygame.mouse.get_pos()
                        self.player.shoot(dest_x, dest_y)
                        pygame.mixer.Sound('sounds/laser-blast-descend_gy7c5deo.mp3').play()
                        pygame.mixer.Sound('sounds/laser-blast-descend_gy7c5deo.mp3').set_volume(0.5)
                        self.player.count -= 1
                    elif event.button == 3 and self.player.granat > 0:
                        self.player.granat -= 1
                        self.vzriv = False
                        dest_x, dest_y = pygame.mouse.get_pos()
                        self.player.throw(5, dest_x, dest_y)
                        pygame.time.set_timer(self.BABAX, 3000)
                if event.type == self.SHOOTEVENT and self.player.is_alive:
                    for i in self.Enemies:
                        i.shoot(self.player.rect.x, self.player.rect.y)
                        pygame.mixer.Sound('sounds/laser-blast-descend_gy7c5deo.mp3').play()
                        pygame.mixer.Sound('sounds/laser-blast-descend_gy7c5deo.mp3').set_volume(0.5)
                if event.type == self.RELOADEVENT and self.player.count < self.player.kolvo:
                    self.player.count += 1
                if event.type == self.BABAX:
                    self.vzriv = True
                    pygame.mixer.Sound('sounds/bolshoy-vzryiv.mp3').play()
                    pygame.time.set_timer(self.BABAX, 0)

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

            if self.player.is_alive:
                self.player.update(self.screen, right, left, up, self.blocks, self.vzriv)
                self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
            for i in self.Enemies:
                i.update(self.screen, self.blocks)
                self.screen.blit(i.image, (i.rect.x, i.rect.y))
            pygame.display.flip()
        pygame.quit()