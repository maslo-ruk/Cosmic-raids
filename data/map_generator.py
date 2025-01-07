import pygame
import random
from data.player import JUMPSPEED, SPEED, GRAVI
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
        else:
            self.sym = '0'

    def update_sym(self):
        if self.type == 1:
            self.sym = '#'
        else:
            self.sym = '0'

    def __str__(self):
        return self.sym



class Platform:
    def __init__(self, cells : list[Cell]):
        self.cells = cells
        self.rect = pygame.Rect(self.cells[0].pos[0], self.cells[0].pos[1], len(self.cells),  1)

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
        print(i.rect.left)
        print(i.rect.right)
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

class Platforms(Strategy):
    def __init__(self, room, plats_average):
        super().__init__(room)
        self.av = plats_average
        self.begins = 0
        self.grid_platforms: list[list[Platform]] = []
        print(self.grid_platforms)
        self.platforms = [] * self.room.height
        self.random_gen = []
        self.map = []
        for i in range(self.room.height):
            self.map.append([])

    def all(self):
        self.generate()
        self.choose_and_build()
        a = self.build_map()
        return a

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
            self.grid_platforms.append([])
            h_pos += int(cur_grid) * (self.av + 2)
            cur_grid = not cur_grid
            while h_pos < length:
                cells = []
                if h_pos + self.av >= length:
                    break
                for i in range(self.av):
                    cells.append(Cell(((h_pos + i), v_pos), 1))
                self.grid_platforms[-1].append(Platform(cells))
                h_pos += self.av + h_step
            h_pos = 0


    def choose_and_build(self):
        plats_count = 3
        poses = []
        final_poses = set()
        poses.append((0, len(self.grid_platforms[0])-1))
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
            dir = random.choice([-1, 1])
            for i in range(new_len):
                platform.cells.append(Cell((platform.rect.right + dir + i * dir, platform.rect.top), 1))
            platform.update()
            self.platforms.append(platform)
        # for i in self.grid_platforms:
        #     for j in i:
        #         self.platforms.append(j)


    def build_map(self):
        print(self.platforms)
        for i in range(self.room.height):
            for j in range(self.room.width):
                if check_pos_in_platform(self.platforms, (j, i)):
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

