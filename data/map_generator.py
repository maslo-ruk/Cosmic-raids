import pygame
import random
from data.player import JUMPSPEED, SPEED, GRAVI, Enemy, HEIGHT
import math

vx = SPEED
vy = JUMPSPEED
g = GRAVI

WIDTH = 30
HEIGHT = 30
COLOR = pygame.Color(215, 215, 215)
CELL_SIZE = 30


class Cell:
    def __init__(self, pos, type):
        self.pos = pos
        self.type = type
        self.cell_size = CELL_SIZE
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.cell_size, self.cell_size)
        if self.type == 1:
            self.sym = '#'
        elif self.type == 2:
            self.sym = 'd'
        else:
            self.sym = '0'

    def update_sym(self):
        if self.type == 1:
            self.sym = '#'
        elif self.type == 2:
            self.sym = 'd'
        else:
            self.sym = '0'

    def __str__(self):
        return self.sym



class Platform:
    def __init__(self, cells : list[Cell], wall=False):
        self.cells = cells
        self.rect = pygame.Rect(self.cells[0].pos[0], self.cells[0].pos[1], len(self.cells),  1)
        self.ends_wall = wall

    def update(self):
        self.rect = pygame.Rect(self.cells[0].pos[0], self.cells[0].pos[1], len(self.cells), 1)

    def can_get_to(self, platform2):
        n = 0
        y = platform2.top
        y_max = self.rect.top - vy**2 / 2 / g
        if y < y_max:
            return False
        x = []
        a = math.sqrt(vy**2 - 2*g*y)
        x.append(vx * (vy + a) / g)
        x.append(vx * (vy - a) / g)
        if platform2.center[0] < self.rect.center[0]:
            n = -1
        elif platform2.center[0] > self.rect.center[0]:
            n = 1
        if n == 1:
            for i in x:
                if i + self.rect.right > platform2.left:
                    return True
                else:
                    return False
        elif n == -1:
            for i in x:
                if self.rect.left - i > platform2.right:
                    return True
                else:
                    return False
        else:
            return False


def check_pos_in_platform(plats, pos):
    x = pos[0]
    y = pos[1]
    for i in plats:
        n = i.rect.top
        if y == n and (i.rect.left <= x < i.rect.right):
            return True



class Room:
    def __init__(self, width, height, entry_point, ending_point):
        self.width = width
        self.height = height
        self.entry = entry_point
        self.end = ending_point
        self.map = []



class Strategy:
    def __init__(self, room: Room):
        self.room = room
        self.map = self.room.map

    def generate(self):
        pass


#Класс, описывающий генерацию уровня с платформами
class Platforms(Strategy):
    def __init__(self, room, plats_average):
        super().__init__(room)
        self.av = plats_average
        self.begins = 0 # переменная определяющая как будет начинаться сетка платформ
        self.grid_platforms: list[list[Platform]] = [] #в эту перменную записывается сетка платформ
        self.platforms = [] * self.room.height
        self.random_gen = []
        self.map = []
        for i in range(self.room.height):
            self.map.append([])

    #функция которая вызывается, когда комната создается на сцене
    def all(self, scene):
        self.generate()
        self.choose_and_build(scene)
        a = self.build_map()
        return a

    # Функция, генерирующая платформенную сетку
    def generate(self):
        length = self.room.width
        height = self.room.height
        v_step = 4
        h_step = self.av + 4
        v_pos = 0
        h_pos = 0
        cur_grid = random.choice([True, False])
        self.begins = cur_grid
        while v_pos < height:
            v_pos += v_step
            if v_pos >= height:
                break
            self.grid_platforms.append([])
            h_pos += int(cur_grid) * (self.av + 2)
            cur_grid = not cur_grid
            while h_pos < length:
                cells = []
                av = self.av
                wall = False
                if h_pos + av >= length and av != 0 and not self.grid_platforms[-1][-1].ends_wall:
                    av -= 1
                    wall = True
                elif h_pos + av >= length and self.grid_platforms[-1][-1].ends_wall:
                    break
                elif h_pos + av >= length and av == 0:
                    break
                for i in range(av):
                    cells.append(Cell(((h_pos + i), v_pos), 1))
                self.grid_platforms[-1].append(Platform(cells, wall))
                h_pos += av + h_step
            h_pos = 0

    #создает выход из комнаты по имещимся платфомрмам так, чтобы выйти можно было всегда
    def find_ending(self):
        check = True
        points = list(range(len(self.grid_platforms)))
        self.ending_point = random.choice(points)
        points.remove(self.ending_point)
        while self.ending_point % 2 == 0 and self.begins or self.ending_point % 2 != 0 and not self.begins and points:
            self.ending_point = random.choice(points)
            points.remove(self.ending_point)
        while self.room.width - self.grid_platforms[self.ending_point][-1].rect.right >= 4 and points:
            self.ending_point = random.choice(points)
            points.remove(self.ending_point)
        if self.room.width - self.grid_platforms[self.ending_point][-1].rect.right >= 4 and not points:
            self.ending_point = self.room.height - 2
            check = False
            print('wtf')
        vert_pos = self.grid_platforms[self.ending_point][-1].rect.y - 1 if check else self.ending_point
        self.ending_poses = []
        for i in range(3):
            self.ending_poses.append((self.room.width - 1, vert_pos - i))
        return True


    def choose_and_build(self, scene):
        plats_count = 3
        poses = []
        final_poses = set()
        if self.find_ending():
            popi = len(self.grid_platforms[0]) - 1
            poses.append((self.ending_point, popi))
        else:
            plats_count += 1
        a = list(range(0, len(self.grid_platforms)))
        for i in range(plats_count):
            choice = a.pop(random.randrange(0, len(a)))
            plat = random.randrange(0, len(self.grid_platforms[choice]))
            poses.append((choice, plat))
        for y_0, x_0 in poses:
            y = y_0
            x = x_0
            while y >= len(self.grid_platforms):
                y -= 1
            while x >= len(self.grid_platforms[y]):
                x -= 1
            final_poses.add((y, x))
            while y < len(self.grid_platforms):
                if self.begins and y % 2 == 0 or (not self.begins) and y % 2 == 1:
                    if x != self.grid_platforms[y][-1]:
                        m = random.choice([0, 1])
                    else:
                        m = 0
                else:
                    if x != 0:
                        m = random.choice([-1, 0])
                    else:
                        m = 0
                if self.grid_platforms[y][x].ends_wall:
                    m = 0
                y += 1
                if y >= len(self.grid_platforms):
                    break
                x += m
                while x >= len(self.grid_platforms[y]):
                    x -= 1
                final_poses.add((y, x))
        for i, j in final_poses:
            try:
                platform = self.grid_platforms[i][j]
            except Exception:
                print(i, j)
            new_len = random.randrange(-self.av, self.av)
            dir = 0
            for i in range(new_len):
                platform.cells.append(Cell((platform.rect.right + dir + i * dir, platform.rect.top), 1))
            platform.update()
            scene.spawns.add(Spawn_zone(platform.rect.left, platform.rect.top, 3, len(platform.cells)))
            scene.all_sprites.add(Spawn_zone(platform.rect.left, platform.rect.top, 3, len(platform.cells)))
            self.platforms.append(platform)

    def build_map(self):
        print(self.platforms)
        for i in range(self.room.height):
            for j in range(self.room.width):
                if (j, i) in self.ending_poses:
                    self.map[i].append(Cell((j, i), 2))
                elif check_pos_in_platform(self.platforms, (j, i)):
                    self.map[i].append(Cell((j, i), 1))
                else:
                    self.map[i].append(Cell((j, i), 0))
        res = []
        for i in self.map:
            res.append('')
            for j in i:
                res[-1] += str(j)
        for i in res:
            print(i)
        return res


class Spawn_zone(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, height, width):
        super().__init__()
        self.name = 'bildabot' + str(pos_x)
        self.rect = pygame.Rect(pos_x * CELL_SIZE, (pos_y - height) * CELL_SIZE, width * CELL_SIZE, height * CELL_SIZE)
        print(self.name, self.rect.x, self.rect.y)
        self.pos = (pos_x, pos_y + height)
        self.bottom = pos_y
        self.height=  height
        self.width = width
        self.image = False
        # self.image = pygame.Surface((self.rect.size[0], self.rect.size[1]))
        # self.image.fill('white')

    def spawn(self):
        pos = random.randrange(self.rect.x, self.rect.x + self.width)
        print(self.name ,self.rect.x, self.rect.y)
        new_enemy = Enemy((pos, self.rect.bottom - HEIGHT))
        return new_enemy

class Level:
    def __init__(self, length, av_room_size):
        self.length = length
        self.rooms_size_x = 100
        self.rooms_size_y = av_room_size[1]
        self.rooms = []

    def make_rooms(self):
        for i in range(self.length):
            d = random.randrange(-self.rooms_size_x, self.rooms_size_x)
            room_x = self.rooms_size_x + d
            d = random.randrange(-self.rooms_size_y, self.rooms_size_y)
            room_y = self.rooms_size_y + d

    def add_room(self, x, y, prev_room):
        new_room = Room(x, y, )