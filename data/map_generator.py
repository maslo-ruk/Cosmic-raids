import pygame
import random
from data.player import JUMPSPEED, SPEED, GRAVI, CommonEnemy, FlyingEnemy, HEIGHT, Close_Enemy
from data.functions import sep
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
        self.map = []
        for i in range(self.room.height):
            self.map.append([])

    def generate(self):
        pass


# class Part:
#     def __init__(self):
#         r


#Класс, описывающий генерацию уровня с платформами
class Platforms(Strategy):
    def __init__(self, room, plats_average):
        self.ending_poses = []
        super().__init__(room)
        self.av = plats_average
        self.begins = 0 # переменная определяющая как будет начинаться сетка платформ
        self.grid_platforms: list[list[Platform]] = [] #в эту перменную записывается сетка платформ
        self.platforms = [] * self.room.height
        self.ending_plat = None
        self.random_gen = []
        while self.room.width <= self.av + 4:
            self.room.width += 1


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
        print(length)
        v_step = 4
        h_step = self.av + 4
        v_pos = 0
        h_pos = 1
        cur_grid = False
        self.begins = False
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
                while h_pos + av >= length +1 and av != 0:
                    av -= 1
                    wall = True
                if av == 0:
                    break
                for i in range(av):
                    cells.append(Cell(((h_pos + i), v_pos), 1))
                self.grid_platforms[-1].append(Platform(cells, wall))
                h_pos += av + h_step
            h_pos = 1

    #создает выход из комнаты по имещимся платфомрмам так, чтобы выйти можно было всегда
    def find_ending(self):
        check = True
        points = list(range(len(self.grid_platforms)))
        self.ending_point = random.choice(points)
        points.remove(self.ending_point)
        while (self.room.width - self.grid_platforms[self.ending_point][-1].rect.right >= 4) and points:
            self.ending_point = random.choice(points)
            points.remove(self.ending_point)
            print(self.ending_point, points)
        if (self.room.width - self.grid_platforms[self.ending_point][-1].rect.right >= 4) and not points:
            self.ending_point = self.room.height - 2
            check = False
        vert_pos = self.grid_platforms[self.ending_point][-1].rect.y - 1 if check else self.ending_point
        self.room.end = (self.room.width - 1, vert_pos)
        for i in range(3):
            self.ending_poses.append((self.room.width - 1, vert_pos - i))
        return check

    def find_entry(self):
        print(len(self.grid_platforms), 'len')
        for i in range(len(self.grid_platforms)):
            print(i, 'íiiii')
            print(self.grid_platforms[i])
            if self.grid_platforms[i][0].rect.top >= self.room.entry[1]:
                vert_pos = self.grid_platforms[i][0].rect.top - 1
                for j in range(3):
                    self.ending_poses.append((0, vert_pos - j))
                return i

    def choose_and_build(self, scene):
        plats_count = 0
        poses = []
        final_poses = set()
        beginning = self.find_entry()
        print(self.grid_platforms[beginning][0].rect.top)
        poses.append((beginning, 0))
        if self.find_ending():
            popi = len(self.grid_platforms[self.ending_point]) - 1
            poses.append((self.ending_point, popi))
            self.ending_plat = self.grid_platforms[self.ending_point][popi]
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
            # new_len = random.randrange(self.av)
            # dir = random.choice([1, -1])
            # if dir == 1:
            #     x = platform.rect.right
            #     while platform.rect.right + new_len >= self.room.width - 2:
            #         new_len -= 1
            # else:
            #     x = platform.rect.left
            #     while platform.rect.right + new_len >= self.room.width - 2:
            #         new_len -= 1
            # for i in range(new_len):
            #     platform.cells.append(Cell((x + i * dir, platform.rect.top), 1))
            # platform.update()
            # scene.spawns.add(Spawn_zone(platform.rect.left, platform.rect.top, 3, len(platform.cells)))
            # scene.all_sprites.add(Spawn_zone(platform.rect.left, platform.rect.top, 3, len(platform.cells)))
            self.platforms.append(platform)
        self.platforms.append(self.grid_platforms[beginning][0])
        # self.platforms = []
        # for i in self.grid_platforms:
        #     for j in i:
        #         self.platforms.append(j)

    def build_map(self):
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
        return res


class Stairs(Strategy):
    def __init__(self, room, stairs_average, scene):
        super().__init__(room)
        self.scene = scene
        self.av = stairs_average
        self.width = self.room.width
        self.height = self.room.height
        self.entry = self.room.entry
        self.end = self.room.end
        self.cells = []
        self.door_cells = []
        self.poses = list(range(4, self.room.height, 8))
        for j in range(3):
            b = self.entry[0], self.entry[1] - j
            self.door_cells.append((self.entry[0], self.entry[1] - j))

    def find_ending(self):
        self.end = self.room.width - 1, self.poses.pop(random.randrange(len(self.poses)))
        while self.end[1] > self.entry[1] + self.width//2 or self.end[1] < self.entry[1] - self.width//2:
            try:
                self.end = self.room.width - 1, self.poses.pop(random.randrange(len(self.poses)))
            except Exception:
                self.width += 1
                self.room.width = self.width
        self.room.end = self.end
        while self.end[1] == self.entry[1] + 1:
            self.find_ending()
        for j in range(3):
            b = self.end[0], self.end[1] - j
            self.door_cells.append((self.end[0], self.end[1] - j))

    def set_ending(self, ending):
        self.end = self.room.width - 1, ending
        self.room.end = self.end

    def generate(self):
        h_pos = 0
        v_pos = self.entry[1] + 1
        end = self.end[1]
        dir = (end - v_pos) // abs(end - v_pos)
        check = dir > 0
        step = 1
        amount = abs(end - v_pos + 2 * check) // step
        # while amount >= self.width // 2:
        #     # if step >= 4:
        #     #     break
        #     step += 1
        #     amount = abs(end - v_pos + 2 * check) // step
        # if step >= 4:
        #     while amount > self.width:
        #         self.set_ending(self.end[1] - 1)
        #         end = self.end[1]
        #         dir = (end - v_pos) // abs(end - v_pos)
        #         check = dir > 0
        #         amount = abs(end - v_pos + 2 * check) // step

        lengths = sep(self.width, amount)
        for i in range(len(lengths)):
            for j in range(v_pos, self.height):
                for k in range(h_pos, h_pos + lengths[i]):
                    self.cells.append((k, j))
            # spawn = Spawn_zone(h_pos, v_pos, 3, lengths[i])
            # self.scene.spawns.add(spawn)
            # self.scene.all_sprites.add(spawn)
            v_pos += step * dir
            h_pos += lengths[i]

    def build_map(self):
        for i in range(self.room.height):
            for j in range(self.room.width):
                if (j, i) in self.door_cells:
                    self.map[i].append(Cell((j, i), 2))
                elif (j, i) in self.cells:
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

    def all(self):
        self.find_ending()
        self.generate()
        return self.build_map()


class Spawn_zone(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, height, width):
        super().__init__()
        self.name = 'bildabot' + str(pos_x)
        self.rect = pygame.Rect(pos_x * CELL_SIZE, (pos_y - height) * CELL_SIZE, width * CELL_SIZE, height * CELL_SIZE)
        self.pos = (pos_x, pos_y + height)
        self.bottom = pos_y
        self.height=  height
        self.width = width
        self.image = False
        # self.image = pygame.Surface((self.rect.size[0], self.rect.size[1]))
        # self.image.fill('white')

    def spawn(self, enemy_type):
        pos = random.randrange(self.rect.x, self.rect.x + self.width)
        new_enemy = enemy_type((pos, self.rect.bottom - HEIGHT), self.rect)
        return new_enemy