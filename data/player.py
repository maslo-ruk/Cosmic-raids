import pygame
from data.Block import Block
from data.config import *
from data.functions import *
import networkx as nx

WIDTH = CELL_SIZE
HEIGHT = CELL_SIZE * 1.5
SIZE = (WIDTH, HEIGHT)
SPEED = 6
HUB_SPEED = 10
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

    def throw(self, velocity, dest_x, dest_y, all_sp):
        from data.projectiles import Grenade
        dx = dest_x - self.rect.centerx
        dy = dest_y - self.rect.centery
        norm = (dx ** 2 + dy ** 2) ** 0.5

        if norm != 0:  # Проверка для избежания деления на ноль
            direction = (dx / norm, dy / norm)
            self.grenade = Grenade(self.rect.center, direction)
            self.grenade.velocity_x = velocity * dx / norm #делим общую скорость на косинус
            self.grenade.velocity_y = velocity * dy / norm #делим общую скорость на синус
            self.grenade.is_launched = True
            self.grenade.time = 0  # сброс времени для нового броска
            self.grenades.add(self.grenade)
            all_sp.add(self.grenade)

    def collides(self, rects: list[Block]):
        for i in rects:
            if self.rect.colliderect(i.rect) and i.rect != self.rect:
                return i.rect
        return False


class Hub_Player(Entity):
    def __init__(self, pos):
        super().__init__(pos, HUB_SPEED)
        self.size = CELL_SIZE * 6, CELL_SIZE * 9
        self.rect = pygame.Rect(self.pos, self.size)
        self.image = pygame.Surface(self.size)
        self.image.fill(COLOR)

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
        self.granat = 3
        self.count = self.kolvo
        self.score = 0
        self.total_score = 0
        self.image.fill('green')

    def set_def(self):
        self.hp += 5 - DIFFICULTY
        if self.hp > 10:
            self.hp = 10
        self.kolvo = 5
        self.granat = 3

    def update(self, scene, screen, a, b, c, rects):
        super().update(scene)
        if self.is_alive == False:
            print(self.score)
            pygame.mixer.Sound('sounds/dark-souls-you-died-sound-effect_hm5sYFG.mp3').play()
            pygame.mixer.Sound('sounds/dark-souls-you-died-sound-effect_hm5sYFG.mp3').set_volume(1.0)
        if a:
            self.xvel = self.x_speed
        if b:
            self.xvel = -self.x_speed
        if (not a) and (not b):
            self.xvel = 0
        self.rect.x += self.xvel
        self.col1 = self.collides(rects)
        if self.col1:
            self.rect.y -= CELL_SIZE
            prev = self.col1
            self.col1 = self.collides(rects)
            print(self.col1)
            if self.col1 or self.inair:
                self.col1 = prev
                self.rect.y += CELL_SIZE
                if self.xvel > 0:
                    self.rect.right = self.col1.left
                if self.xvel < 0:
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

ENEMY_SPEED = 3.5



class Enemy(Entity):
    def __init__(self, pos):
        super().__init__(pos, ENEMY_SPEED)


class Land_enemy(Entity):
    def __init__(self, pos, borders):
        self.borders = borders
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
            pygame.mixer.Sound('sounds/tmp_7901-951678082.mp3').play()
        player_pos = player.rect
        if abs(self.rect.x - player_pos.x) <= self.x_vision * 30 and abs(
                self.rect.y - player_pos.y) <= self.y_vision * 30:
            self.unseed = True
            if abs(self.rect.x - player_pos.x) > self.x_range * 30:
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
            # self.move_to_player(self.randdir, rects)

        self.move_to_player(self.xvel, rects)
        self.fall(rects)
        self.all_b.update(rects, self.rect)

    def move_to_player(self, vel, rects):
        self.rect.x += self.x_speed * self.xvel
        self.col1 = self.collides(rects)
        # if not self.inair:
        #     self.rect.x += CELL_SIZE * self.xvel
        #     self.rect.y += GRAVI
        #     if not self.collides(rects):
        #         print('113123313')
        #         self.rect.x -= self.x_speed * self.xvel
        #     self.rect.x -= CELL_SIZE * self.xvel
        #     self.rect.y -= GRAVI
        if self.col1:
            self.rect.y -= CELL_SIZE
            prev = self.col1
            self.col1 = self.collides(rects)
            if self.col1 or self.inair:
                self.col1 = prev
                self.rect.y += CELL_SIZE
                if self.xvel > 0:
                    self.rect.right = self.col1.left
                if self.xvel < 0:
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

class CommonEnemy(Land_enemy):
        def __init__(self, pos, borders):
            super().__init__(pos, borders)
            self.x_vision = 12
            self.y_vision = 4
            self.x_range = 6
            self.image = pygame.Surface(self.size)
            self.image.fill('red')



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
            target = player.rect.center[1] // 30, player.rect.center[0] // 30
            print(target)
            self_pos = self.rect.center[1] // 30, self.rect.center[0] // 30
            print(self_pos)
            if map_graph.has_node(target) and map_graph.has_node(self_pos):
                way = nx.shortest_path(map_graph, self_pos, target, weight=1)
                dest = (way[0][1] * 30, way[0][0] * 30)
                counter = 0
                # while cast_ray(self.rect.center, dest, rects):
                #     counter += 1
                #     dest = (way[counter][1] * 30, [counter][0] * 30)
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


class Close_Enemy(Land_enemy):
    def __init__(self, pos, borders):
        super().__init__(pos, borders)
        self.atk = 2
        self.hp = 7
        self.x_vision = 12
        self.y_vision = 4
        self.x_range = 2
        self.image = pygame.Surface(self.size)
        self.image.fill('yellow')


    def punch(self, player):
        player_pos = player.rect
        if abs(self.rect.x - player_pos.x) <= self.x_range * 30 and player_pos.bottom >= self.rect.top:
            player.hp -= self.atk
        print(player.hp)
