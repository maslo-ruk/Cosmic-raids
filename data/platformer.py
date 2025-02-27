import random

import pygame, pygame_menu
from data.functions import *
from data.player import Player, CommonEnemy, Hub_Player
from data.Block import *
from data.camera import Camera
from data.level import *
from data.map_generator import *
from data.buttons import *

pygame.init()


class Scene:
    def __init__(self, size, screen, clock, player):
        self.size = size
        self.screen = screen
        self.clock = clock
        self.score = 0
        self.player = player
        screen_info = pygame.display.Info()  # узнаем размеры экрана пользователя
        e_width = screen_info.current_w  # ширина
        e_height = screen_info.current_h
        self.camera = Camera(camera_conf, e_width, e_height, self)
        self.rect = pygame.Rect(0, 0, self.size[0], self.size[1])
        self.all_sprites = pygame.sprite.Group()


class Platformer(Scene):
    def __init__(self, size, screen, clock, player):
        super().__init__(size, screen, clock, player)
        self.all_sprites.add(self.player)
        self.Enemies = pygame.sprite.Group()
        self.CloseEnemies = pygame.sprite.Group()
        self.FlyingEnemies = pygame.sprite.Group()
        self.map = []
        self.spawns = pygame.sprite.Group()
        self.all_collides = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.blocks_map = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.SHOOTEVENT = pygame.USEREVENT + 1
        self.MOVEEVENT = pygame.USEREVENT + 2
        self.RELOADEVENT = pygame.USEREVENT + 3
        self.SPAWNEVENT = pygame.USEREVENT + 4
        self.PUNCHEVENT = pygame.USEREVENT + 5
        self.RELOADEVENT = pygame.USEREVENT + 6
        self.MUSICBGEVENT = pygame.USEREVENT + 7
        self.BABAX = pygame.USEREVENT + 8
        self.score = 0
        self.new_level = False
        self.blocks.add(self.player)
        self.player.set_def()
        self.pause = False

    def make_map(self):
        level = Level(4, (25, 40), self, self.player)
        self.map_x = level.all()
        self.size = (CELL_SIZE * level.total_length, level.rooms_size_y * CELL_SIZE)
        self.rect = pygame.Rect(0, 0, self.size[0], self.size[1])
        self.map = []
        self.map_y = []
        for i in range(level.rooms_size_y):
            if i == 0 or i == level.rooms_size_y - 1:
                self.map_y.append('#' * (level.total_length))
            else:
                self.map_y.append('#' + '0'* (level.total_length - 2) + '#')
        for i in range(len(self.map_x)):
            new_str = ''
            for j in range(len(self.map_x[i])):
                if self.map_x[i][j] == '#':
                    new_str += self.map_x[i][j]
                elif self.map_x[i][j] == 'd' and (j == 0 or j == level.total_length - 1):
                    new_str += 'd'
                else:
                    new_str += self.map_y[i][j]
            self.map.append(new_str)
        self.graph = make_graph(self.map)
        for i in range(len(self.map)):
            string = self.map[i]
            for j in range(len(string)):
                pos = (j * CELL_SIZE, i * CELL_SIZE)
                if string[j] == '-' or string[j] == '#':
                    block = Block(pos, self.screen)
                    self.blocks.add(block)
                    self.blocks_map.add(block)
                    self.all_sprites.add(block)
                elif string[j] == 'd':
                    block = Door(pos, self.screen)
                    self.blocks.add(block)
                    self.blocks_map.add(block)
                    self.all_sprites.add(block)
                    if j == level.total_length - 1:
                        self.doors.add(block)
        self.level = level
    # def make_camera(self):

    def open_doors(self):
        for i in self.doors:
            self.blocks.remove(i)
            self.blocks_map.remove(i)
            self.all_sprites.remove(i)

    def spawn_enemies(self):
        types = [CommonEnemy, Close_Enemy]
        for i in range(self.level.enemies_amount):
            type = random.choice(types)
            sppoint = random.choice(list(self.spawns))
            if type == CommonEnemy:
                enemy = sppoint.spawn(CommonEnemy)
                self.blocks.add(enemy)
                self.Enemies.add(enemy)
                self.all_sprites.add(enemy)
            elif type == Close_Enemy:
                enemy = sppoint.spawn(Close_Enemy)
                self.blocks.add(enemy)
                self.CloseEnemies.add(enemy)
                self.all_sprites.add(enemy)
            # elif type == FlyingEnemy:
            #     enemy = sppoint.spawn(FlyingEnemy)
            #     self.blocks.add(enemy)
            #     self.FlyingEnemies.add(enemy)
            #     self.all_sprites.add(enemy)
            # if type == FlyingEnemy and len(self.FlyingEnemies) >= 5:
            #     types.remove(FlyingEnemy)

    def run(self, sound):
        self.make_map()
        self.spawn_enemies()
        self.player.rect.x = self.level.spawn_pos[0] * CELL_SIZE
        self.player.rect.y = self.level.spawn_pos[1] * CELL_SIZE - self.player.size[1]
        running = True
        all_b = pygame.sprite.Group()
        grenades = pygame.sprite.Group()
        right = False
        left = False
        up = False
        pygame.time.set_timer(self.SHOOTEVENT, 1000)
        pygame.time.set_timer(self.MOVEEVENT, 2000)
        pygame.time.set_timer(self.RELOADEVENT, 1000)
        pygame.time.set_timer(self.SPAWNEVENT, 3000)
        pygame.time.set_timer(self.PUNCHEVENT, 1500)
        pygame.time.set_timer(self.MUSICBGEVENT, 107000)
        count = 0
        fon = pygame.image.load("images/for_hub/fon1.png")
        fon = pygame.transform.scale(fon, (self.level.total_length * CELL_SIZE, self.level.rooms_size_y * CELL_SIZE)).convert_alpha()
        screen_info = pygame.display.Info()  # узнаем размеры экрана пользователя
        e_width = screen_info.current_w  # ширина
        e_height = screen_info.current_h
        print(e_width, e_height)
        fon_p = pygame.image.load("images/pausa/fon.png").convert()
        fon_p = pygame.transform.scale(fon_p, (e_width, e_height))
        continuee = Button(0, 0, e_width, e_height, '', "images/pausa/knopka_snat_s_pausi.png",
                           "images/pausa/knopka_snat_s_pausi.png", '',
                              (800 * (e_width / 1920), 1099 * (e_width / 1920)),
                              ((344 * (e_height / 1080)), 689 * (e_height / 1080)))
        to_hubb = Button(0, 0, e_width, e_height, '', "images/pausa/knopka_to_hub.png",
                           "images/pausa/knopka_to_hub.png", '',
                              (28 * (e_width / 1920), 558 * (e_width / 1920)),
                              ((906 * (e_height / 1080)), 1041 * (e_height / 1080)))
        health_bars = []
        for i in range(6):
            new_photo = pygame.image.load(f'images/for_fight/health_bullets_experience{str(i)}.png')
            new_photo = pygame.transform.scale(new_photo, (e_width//2, e_height//2)).convert_alpha()
            health_bars.append(new_photo)
        if self.player.levels_passed == 0:
            self.player.time = 0
            self.player.total_score = 0
            self.player.shots = 0
            self.player.health_lost = 0
            # pygame.mixer.Sound(sound).play(-1)
            # pygame.mixer.Sound(sound).set_volume(1.0)
        while running:
            if self.pause:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            return 4
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if to_hubb.events():
                            return 4
                        if continuee.events():
                             self.pause = not self.pause
                    elif event.type == pygame.MOUSEMOTION:
                        x_pos = event.pos
                        to_hubb.check_mishka(x_pos)
                        continuee.check_mishka(x_pos)
                self.screen.blit(fon_p, (0, 0))
                continuee.draw(self.screen)
                to_hubb.draw(self.screen)
                pygame.display.flip()
                continue
            tick = self.clock.tick(60)
            self.screen.blit(fon, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pause = not self.pause
                if event.type == self.MUSICBGEVENT:
                    pygame.mixer.music.load('sounds/cosmic_battle.mp3')
                    pygame.mixer.music.play(-1)
                if event.type == pygame.MOUSEBUTTONDOWN and self.player.is_alive:
                    if event.button == 1 and self.player.count > 0:
                        dest_x, dest_y = self.camera.apply_point(pygame.mouse.get_pos())
                        self.player.shoot(dest_x, dest_y, all_b, self.all_sprites)
                        self.player.count -= 1
                        self.player.shots += 1
                        shot = 'sounds/laser-blast-descend_gy7c5deo.mp3'
                        pygame.mixer.Sound(shot).play()
                        pygame.mixer.Sound(shot).set_volume(0.1)
                    elif event.button == 3 and self.player.granat > 0:
                        self.player.granat -= 1
                        dest_x, dest_y = self.camera.apply_point(pygame.mouse.get_pos())
                        self.player.throw(5, dest_x, dest_y, self.all_sprites)
                        pygame.time.set_timer(self.BABAX, 3000)
                if event.type == self.SHOOTEVENT and self.player.is_alive:
                    for i in self.Enemies:
                        if i.see_player:
                            i.shoot(self.player.rect.x, self.player.rect.y, all_b, self.all_sprites)
                            shotv = 'sounds/laser-blast-descend_gy7c5deo.mp3'
                            pygame.mixer.Sound(shotv).play()
                            pygame.mixer.Sound(shotv).set_volume(0.1)
                if event.type == self.PUNCHEVENT and self.player.is_alive:
                    for i in self.CloseEnemies:
                        if i.see_player:
                            i.punch(self.player)
                if event.type == self.MOVEEVENT:
                    for i in self.Enemies:
                        if not i.unseed:
                            i.random_move()
                    for i in self.CloseEnemies:
                        if not i.unseed:
                            i.random_move()
                if event.type == self.RELOADEVENT and self.player.count < self.player.kolvo:
                    self.player.count += 1
                # if event.type == self.SPAWNEVENT and len(self.Enemies) < 6:
                #     sppoint = random.choice(list(self.spawns))
                #     enemy = sppoint.spawn(Close_Enemy)
                #     self.blocks.add(enemy)
                #     self.Enemies.add(enemy)
                #     self.all_sprites.add(enemy)

            keys = pygame.key.get_pressed()
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
            if keys[pygame.K_p]:
                for i in self.Enemies:
                    i.die()
                    self.player.score += 1
                for i in self.CloseEnemies:
                    i.kill()
                    self.player.score += 1
            if keys[pygame.K_o]:
                self.player.die()

            if self.player.is_alive:
                self.player.update(self, self.screen, right, left, up, self.blocks)
            # for i in self.player.grenades:
            #     self.screen.blit(i.image, (self.player.grenade.rect.x, self.player.grenade.rect.y))
            for i in self.Enemies:
                i.update(self, self.screen, self.blocks, self.player)
            for i in self.CloseEnemies:
                i.update(self, self.screen, self.blocks, self.player)
            self.camera.update(self.player)
            for i in self.all_sprites:
                if i.image:
                    self.screen.blit(i.image, self.camera.apply(i))
            if self.player.score == self.level.enemies_amount:
                pygame.mixer.Sound('sounds/zvuk-pobedyi-vyiigryisha.mp3').play()
                self.player.score = 0
                self.player.levels_passed += 1
                self.new_level = True
                self.open_doors()
            if self.new_level:
                for i in self.doors:
                    if self.player.rect.colliderect(i):
                        return 1
            if not self.player.is_alive:
                return 6
            self.screen.blit(health_bars[self.player.hp], (0, 0))
            pygame.display.flip()
        pygame.quit()


class Hub(Scene):
    def __init__(self, size, screen, clock, player):
        super().__init__(size, screen, clock, player)
        self.width = size[0]
        self.height = size[1]
        self.player = Hub_Player((size[0] // 2, size[1] // 2))
        self.blocks = pygame.sprite.Group()
        self.blocks_map = pygame.sprite.Group()
        self.gildia = pygame.Rect(CELL_SIZE * 6, 0, CELL_SIZE * 12, CELL_SIZE * 10)
        self.in_gildia = False
        self.font = pygame.font.Font(None, 60)

    def make_map(self):
        self.map_y = []
        for i in range(self.size[1] // CELL_SIZE):
            if i == 0 or i == self.size[1] // CELL_SIZE - 1:
                self.map_y.append('#' * (self.size[0] // CELL_SIZE))
            else:
                self.map_y.append('#' + '0' * (self.size[0] // CELL_SIZE - 2) + '#')
        self.map = self.map_y[:]
        for i in range(len(self.map)):
            string = self.map[i]
            for j in range(len(string)):
                pos = (j * CELL_SIZE, i * CELL_SIZE)
                if string[j] == '-' or string[j] == '#':
                    block = Block(pos, self.screen)
                    self.blocks.add(block)
                    self.blocks_map.add(block)

    def close_menu(self):
        self.menu.disable()

    def run(self, sound):
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
        # создание окна помощи
        self.menu = pygame_menu.Menu("Помощь", 900, 600, theme=pygame_menu.themes.THEME_SOLARIZED)
        self.menu.add.label('Управление:', 'purple')
        self.menu.add.label("'w', 'a', 's', 'd' - управление")
        self.menu.add.label("ПРОБЕЛ - прыжок")
        self.menu.add.label("ЛКМ - стрельба")
        self.menu.add.label("ПКМ - бросок гранаты")
        self.menu.add.label("-------------------------------------------------------")
        self.menu.add.label('Разработчики:')
        self.menu.add.label('Егор Жаворонков, Кононов Александр, Кульпинская Елена')
        self.menu.add.label('Репозиторий игры:')
        self.menu.add.label('https://github.com/maslo-ruk/Cosmic-raids')
        self.menu.add.button('Выйти', self.close_menu)
        self.menu.disable()
        con = sqlite3.connect('db/characters_and_achievements.sqlite')
        cur = con.cursor()
        level = cur.execute("""SELECT cur_level FROM player WHERE id = 1""").fetchall()[0][0]
        text1 = self.font.render(f'Уровень: {str(level // 10)}', 1, 'red')
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
                pygame.mouse.set_visible(True)
                return 8
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
            if keys[pygame.K_e]:
                if self.in_gildia:
                    pygame.mouse.set_visible(True)
                    return 5
            #Егор, разработай ограничения передвижения в хабе
            if keys[pygame.K_h]:
                pass

            if keys[pygame.K_i]:
                self.menu.enable()
                self.menu.mainloop(self.screen)
            if keys[pygame.K_ESCAPE]:
                self.menu.disable()

            self.player.update(self, self.screen, hor, vert, self.blocks_map, self.gildia)
            self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
            self.screen.blit(text1, (60, 60))
            pygame.display.flip()
            hor = 0
            vert = 0
            a += 1
        pygame.quit()