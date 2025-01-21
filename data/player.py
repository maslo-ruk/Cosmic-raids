import pygame
from data.Block import Block
from data.config import *
from data.functions import *
import networkx as nx

WIDTH = CELL_SIZE
HEIGHT = CELL_SIZE * 1.5
SIZE = (WIDTH, HEIGHT)
SPEED = 6
HUB_SPEED = 4
JUMPSPEED = 14
GRAVI = 0.8
COLOR = 'red'
POS = (250, 200)


class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, speed):
        super().__init__()
        self.hp = 10
        self.x_speed = speed
        self.xvel = 0
        self.y_speed = 0
        self.inair = True
        self.size = SIZE
        self.pos = pos
        self.rect = pygame.Rect(self.pos, self.size)
        self.image = pygame.Surface(self.size)
        self.image.fill(COLOR)
        self.col1 = False
        self.col2 = False
        self.all_b = pygame.sprite.Group()
        self.grenades = pygame.sprite.Group()
        self.lines = pygame.sprite.Group()
        self.is_alive = True


    def update(self, *args, **kwargs):
        if self.hp <= 0:
            self.die()
        a = args[0]
        if not a.rect.contains(self.rect):
            self.die()


    def shoot(self, dest_x, dest_y, all_b, all_sp):
        from data.projectiles import Bullets
        dx = dest_x - self.rect.x
        dy = dest_y - self.rect.y
        angle = (dx, dy)
        if dx != 0 or dy != 0:  # Проверка для избежания деления на ноль
            norm = (dx ** 2 + dy ** 2) ** 0.5
            direction = (dx / norm, dy / norm)
            line = Bullets(self.rect.center, direction)
            self.all_b.add(line)
            all_sp.add(line)

    def die(self):
        self.is_alive = False
        self.kill()

    def throw(self, velocity, dest_x, dest_y):
        from data.projectiles import Grenade
        dx = dest_x - self.rect.centerx
        dy = dest_y - self.rect.centery
        norm = (dx ** 2 + dy ** 2) ** 0.5

        if norm != 0:  # Проверка для избежания деления на ноль
            direction = (dx / norm, dy / norm)
            grenade = Grenade(self.rect.center, direction)
            grenade.velocity_x = velocity * dx / norm #делим общую скорость на косинус
            grenade.velocity_y = velocity * dy / norm #делим общую скорость на синус
            grenade.is_launched = True
            grenade.time = 0  # сброс времени для нового броска
            self.grenades.add(grenade)

    def collides(self, rects: list[Block]):
        for i in rects:
            if self.rect.colliderect(i.rect) and i.rect != self.rect:
                return i.rect
        return False


class Hub_Player(Entity):
    def __init__(self, pos):
        super().__init__(pos, HUB_SPEED)

    def update(self, scene, screen, hor, vert, rects):
        super().update(scene)
        self.rect.x += hor * self.x_speed
        self.col1 = self.collides(rects)
        if self.col1 and (hor > 0):
            self.rect.right = self.col1.left
        if self.col1 and (hor < 0):
            self.rect.left = self.col1.right
        self.rect.y += vert * self.x_speed
        self.col2 = self.collides(rects)
        if self.col2 and (vert < 0):
            self.rect.top = self.col2.bottom
        if self.col2 and (vert > 0):
            self.rect.bottom = self.col2.top

class Player(Entity):
    def __init__(self, POS1):
        super().__init__(POS1, SPEED)
        self.x_speed = SPEED
        self.kolvo = 5
        self.count = self.kolvo
        self.score = 0
        self.image.fill('green')


    def update(self, scene, screen, a, b, c, rects):
        super().update(scene)
        if self.is_alive == False:
            print(self.score)
        if a:
            self.xvel = self.x_speed
        if b:
            self.xvel = -self.x_speed
        if (not a) and (not b):
            self.xvel = 0
        self.rect.x += self.xvel
        self.col1 = self.collides(rects)
        if self.col1 and (self.xvel > 0):
            self.rect.right = self.col1.left
        if self.col1 and (self.xvel < 0):
            self.rect.left = self.col1.right

        if self.inair:
            self.y_speed += GRAVI
        if c and not self.inair:
            self.inair = True
            self.y_speed = -JUMPSPEED
        self.rect.y += self.y_speed
        self.col2 = self.collides(rects)
        if self.col2 and (self.y_speed < 0):
            self.rect.top = self.col2.bottom
            self.y_speed = 0
        if self.col2 and (self.y_speed > 0):
            self.rect.bottom = self.col2.top
            self.y_speed = 0
            self.inair = False
        if not self.col2:
            self.inair = True

        self.all_b.update(rects, self.rect)
        self.grenades.update(screen, rects, self.rect)
        self.grenades.draw(screen)

ENEMY_SPEED = 3.5


class Enemy(Entity):
    def __init__(self, pos):
        super().__init__(pos, ENEMY_SPEED)

class Common_Enemy(Entity):
        def __init__(self, pos):
            super().__init__(pos, ENEMY_SPEED)
            self.x_speed = ENEMY_SPEED
            self.hp = 5
            self.x_vision = 12
            self.y_vision = 4
            self.x_shooting = 6
            self.randdir = 0
            self.unseed = True
            self.rand_stat = False
            self.see_player = False
            self.inair = True

        def update(self, scene, screen, rects, player):
            super().update(scene)
            if not self.is_alive:
                player.score += 1
            player_pos = player.rect
            if abs(self.rect.x - player_pos.x) <= self.x_vision * 30 and abs(
                    self.rect.y - player_pos.y) <= self.y_vision * 30:
                self.unseed = True
                if abs(self.rect.x - player_pos.x) > self.x_shooting * 30:
                    self.see_player = False
                    if self.rect.x < player_pos.x:
                        self.xvel = 1
                    elif self.rect.x > player_pos.x:
                        self.xvel = -1
                    else:
                        self.xvel = 0
                else:
                    self.see_player = True
                    self.xvel = 0
            else:
                self.see_player = False
                if self.unseed:
                    self.unseed = False
                    self.xvel = 0
                self.move_to_player(self.randdir, rects)

            self.move_to_player(self.xvel, rects)
            self.fall(rects)
            self.all_b.update(rects, self.rect)

        def move_to_player(self, vel, rects):
            self.rect.x += self.x_speed * self.xvel
            self.col1 = self.collides(rects)
            if self.col1 and (self.xvel > 0):
                self.rect.right = self.col1.left
            if self.col1 and (self.xvel < 0):
                self.rect.left = self.col1.right

        def fall(self, rects):
            if self.inair:
                self.y_speed += GRAVI
            self.rect.y += self.y_speed
            self.col2 = self.collides(rects)
            if self.col2 and (self.y_speed < 0):
                self.rect.top = self.col2.bottom
                self.y_speed = 0
            if self.col2 and (self.y_speed > 0):
                self.rect.bottom = self.col2.top
                self.y_speed = 0
                self.inair = False
            if not self.col2:
                self.inair = True


        def random_move(self):
            import random
            self.rand_stat = not self.rand_stat
            if self.rand_stat:
                self.xvel = random.choice([0.4, -0.4])
            else:
                self.xvel = 0


class FlyingEnemy(Entity):
    def __init__(self, pos):
        super().__init__(pos, ENEMY_SPEED)
        self.hp = 3
        self.size = (30, 30)
        self.rect = pygame.Rect(self.pos, self.size)
        self.image = pygame.Surface(self.size)
        self.image.fill(COLOR)
        self.speed = 8
        self.xvel = 0
        self.yvel = 0

    def idle(self):
        pass

    def update(self, scene, screen, rects, map_graph: nx.Graph, player):
        if cast_ray(self.rect.center, player.rect.center, rects):
            print('0000')
            self.move_to(player.rect.center)
        else:
            target = player.rect.center[0] // 30, player.rect.center[1] // 30
            self_pos = self.rect.center[0] // 30, self.rect.center[1] // 30
            if map_graph.has_node(target) and map_graph.has_node(self_pos):
                way = nx.shortest_path(map_graph, self_pos, target, weight=1)
                dest = (way[0][0] * 30, way[0][1] * 30)
                counter = 0
                while cast_ray(self.rect.center, dest, rects):
                    counter += 1
                    dest = (way[counter][0] * 30, way[counter][1] * 30)
            else:
                print(':[[[[[')
                dest = (player.rect.center)
            self.move_to(dest)

    def find_way(self, map):
        pass

    def get_direction(self, target):
        dx = target[0] - self.rect.x
        print(dx)
        dy = target[1] - self.rect.y
        print(dy)
        print('------------')
        gip = (dx**2 + dy**2) ** 0.5
        if gip != 0:
            sin = dx / gip
            cos = dy / gip
            self.xvel = self.speed * sin
            self.yvel = self.speed * cos
        else:
            self.xvel = 0
            self.yvel = 0

    def move_to(self, target):
        self.get_direction(target)
        self.rect.x += self.xvel
        # self.col1 = self.collides(rects)
        # if self.col1 and (self.xvel > 0):
        #     self.rect.right = self.col1.left
        # elif self.col1 and (self.xvel < 0):
        #     self.rect.left = self.col1.right
        self.rect.y += self.yvel
        # self.col2 = self.collides(rects)
        # if self.col2 and (self.yvel < 0):
        #     self.rect.top = self.col2.bottom
        # elif self.col2 and (self.yvel > 0):
        #     self.rect.bottom = self.col2.top