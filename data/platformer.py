import pygame
from data.functions import *
from data.player import Player, Common_Enemy, Hub_Player
from data.Block import Block
from data.camera import Camera
from data.map_generator import *

pygame.init()


class Scene:
    def __init__(self, size, screen, clock):
        self.size = size
        self.screen = screen
        self.clock = clock
        self.score = 0
        self.player = Player((300, 200))
        self.camera = Camera(camera_conf, WINDOW_SIZE[0], WINDOW_SIZE[1])
        self.rect = pygame.Rect(0, 0, self.size[0], self.size[1])
        self.all_sprites = pygame.sprite.Group()


class Platformer(Scene):
    def __init__(self, size, screen, clock):
        super().__init__(size, screen, clock)
        self.all_sprites.add(self.player)
        self.Enemies = pygame.sprite.Group()
        self.map = []
        self.spawns = pygame.sprite.Group()
        self.all_collides = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.blocks_map = pygame.sprite.Group()
        self.SHOOTEVENT = pygame.USEREVENT + 1
        self.MOVEEVENT = pygame.USEREVENT + 2
        self.RELOADEVENT = pygame.USEREVENT + 3
        self.SPAWNEVENT = pygame.USEREVENT + 4

    def make_map(self):
        self.map_y = []
        for i in range(self.size[1] // 30):
            if i == 0 or i == self.size[1] // 30 - 1:
                self.map_y.append('#' * (self.size[0] // 30))
            else:
                self.map_y.append('#' + '0'* (self.size[0] // 30 - 2) + '#')
        room = Room(self.size[0] // 30, self.size[1] // 30, (0, 20), (self.size[0]//30 - 1, 30))
        strategy = Platforms(room, 10)
        self.map_x = strategy.all(self)
        self.map = []
        for i in range(len(self.map_x)):
            new_str = ''
            for j in range(len(self.map_x[i])):
                if self.map_x[i][j] == '#':
                    new_str += self.map_x[i][j]
                elif self.map_x[i][j] == 'd':
                    new_str += '0'
                else:
                    new_str += self.map_y[i][j]
            self.map.append(new_str)
        self.graph = make_graph(self.map)
        for i in range(len(self.map)):
            string = self.map[i]
            for j in range(len(string)):
                pos = (j * 30, i * 30)
                if string[j] == '-' or string[j] == '#':
                    block = Block(pos, self.screen)
                    self.blocks.add(block)
                    self.blocks_map.add(block)
                    self.all_sprites.add(block)

    # def make_camera(self):

    def run(self):
        self.make_map()
        enemy = Enemy((600, 510))
        self.Enemies.add(enemy)
        self.blocks.add(self.player)
        for i in self.Enemies:
            self.blocks.add(i)
            self.all_sprites.add(i)
        running = True
        all_b = pygame.sprite.Group()
        grenades = pygame.sprite.Group()
        right = False
        left = False
        up = False
        pygame.time.set_timer(self.SHOOTEVENT, 1000)
        pygame.time.set_timer(self.MOVEEVENT, 2000)
        pygame.time.set_timer(self.RELOADEVENT, 1000)
        pygame.time.set_timer(self.SPAWNEVENT, 500)
        while running:
            tick = self.clock.tick(60)
            self.screen.fill('blue')
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.player.count > 0:
                        print(self.camera.apply_point(pygame.mouse.get_pos()))
                        dest_x, dest_y = self.camera.apply_point(pygame.mouse.get_pos())
                        self.player.shoot(dest_x, dest_y, all_b, self.all_sprites)
                        self.player.count -= 1
                    elif event.button == 3:
                        dest_x, dest_y = pygame.mouse.get_pos()
                        self.player.throw(10, dest_x, dest_y)
                if event.type == self.SHOOTEVENT and self.player.is_alive:
                    for i in self.Enemies:
                        if i.see_player:
                            i.shoot(self.player.rect.x, self.player.rect.y, all_b, self.all_sprites)
                if event.type == self.MOVEEVENT:
                    for i in self.Enemies:
                        if not i.unseed:
                            i.random_move()
                if event.type == self.RELOADEVENT and self.player.count < self.player.kolvo:
                    self.player.count += 1
                if event.type == self.SPAWNEVENT and len(self.Enemies) < 6:
                    sppoint = random.choice(list(self.spawns))
                    enemy = sppoint.spawn()
                    self.blocks.add(enemy)
                    self.Enemies.add(enemy)
                    self.all_sprites.add(enemy)
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
                self.player.update(self, self.screen, right, left, up, self.blocks)
            for i in self.Enemies:
                i.update(self, self.screen, self.blocks, self.player)
            self.camera.update(self.player)
            for i in self.all_sprites:
                if i.image:
                    self.screen.blit(i.image, self.camera.apply(i))
            pygame.display.flip()
        pygame.quit()


class Hub(Scene):
    def __init__(self, size, screen, clock):
        super().__init__(size, screen, clock)
        self.width = size[0]
        self.height = size[1]
        self.player = Hub_Player((size[0] // 2, size[1] // 2))
        self.blocks = pygame.sprite.Group()
        self.blocks_map = pygame.sprite.Group()

    def make_map(self):
        self.map_y = []
        for i in range(self.size[1] // 30):
            if i == 0 or i == self.size[1] // 30 - 1:
                self.map_y.append('#' * (self.size[0] // 30))
            else:
                self.map_y.append('#' + '0' * (self.size[0] // 30 - 2) + '#')
        self.map = self.map_y[:]
        for i in range(len(self.map)):
            string = self.map[i]
            for j in range(len(string)):
                pos = (j * 30, i * 30)
                if string[j] == '-' or string[j] == '#':
                    block = Block(pos, self.screen)
                    self.blocks.add(block)
                    self.blocks_map.add(block)

    def run(self):
        fon = pygame.image.load("images/for_hub/hub_pic_test1.png")
        fon = pygame.transform.scale(fon, (self.width, self.height)).convert_alpha()
        self.screen.blit(fon, (0, 0))
        pet = pygame.image.load("images/for_hub/pet_pose_normal.png")
        pet = pygame.transform.scale(pet, (self.width, self.height)).convert_alpha()
        self.screen.blit(pet, (0, 0))
        nouneim = pygame.image.load("images/for_hub/who_normal.png")
        nouneim = pygame.transform.scale(nouneim, (self.width, self.height)).convert_alpha()
        self.screen.blit(nouneim, (0, 0))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Тестовое меню")
        pygame.mouse.set_visible(False)
        self.make_map()
        running = True
        hor = 0
        vert = 0
        a = 0
        while running:
            tick = self.clock.tick(60)
            self.screen.fill('blue')
            self.blocks_map.draw(self.screen)
            self.screen.blit(fon, (0, 0))
            self.screen.blit(pet, (0, 0))
            self.screen.blit(nouneim, (0, 0))
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                exit()
            if keys[pygame.K_d]:
                if hor == 0:
                    hor = 1
                else:
                    hor = 0
            if keys[pygame.K_a]:
                if hor == 0:
                    hor = -1
                else:
                    hor = 0
            if keys[pygame.K_w]:
                if vert == 0:
                    vert = -1
                else:
                    vert = 0
            if keys[pygame.K_s]:
                if vert == 0:
                    vert = 1
                else:
                    vert = 0
            #Егор, разработай ограничения передвижения в хабе
            if keys[pygame.K_h]:
                pass
            self.player.update(self, self.screen, hor,vert, self.blocks_map)
            self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
            pygame.display.flip()
            hor = 0
            vert = 0
            a += 1
            print('yo', a)
        pygame.quit()
