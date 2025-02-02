import random

from data.map_generator import *
from data.config import *


class Level:
    def __init__(self, length, av_room_size, scene):
        self.length = length
        self.map = []
        for i in range(av_room_size[1]):
            self.map.append('')
        self.rooms_size_x = av_room_size[0]
        self.rooms_size_y = av_room_size[1]
        self.total_length = 0
        self.rooms: list[Room] = []
        self.scene = scene
        self.enemies_amount = 10 + DIFFICULTY * 5

    def all(self):
        self.make_rooms()
        self.make_map()
        beg = False
        s_p, e_p = 0, 0
        for i in range(len(self.map)):
            beg = False
            for j in range(len(self.map[i])):
                if not beg and self.map[i][j] == '#' and self.map[i - 1][j] == '0':
                    beg = True
                    s_p = i, j
                    continue
                if beg and self.map[i][j] != '#':
                    e_p = i, j
                    print(e_p, s_p)
                    spawn = Spawn_zone(s_p[1], i, 3, e_p[1] - s_p[1])
                    self.scene.spawns.add(spawn)
                    self.scene.all_sprites.add(spawn)
                    beg =False
                if j == len(self.map[i]) - 1 and beg:
                    e_p = i, j
                    print(e_p, s_p)
                    spawn = Spawn_zone(s_p[1], i, 3, e_p[1] - s_p[1])
                    self.scene.spawns.add(spawn)
                    self.scene.all_sprites.add(spawn)
                    beg = False
        self.spawn_pos = self.rooms[0].entry[0] + 1, self.rooms[0].entry[1]
        print(self.spawn_pos, 'voov')
        return self.map

    def make_rooms(self):
        type = random.choice([True, False])
        for i in range(self.length):
            d = random.randrange(-self.rooms_size_x//2, self.rooms_size_x//2)
            room_x = self.rooms_size_x + d
            if i == 0:
                entry = (0, 20)
            else:
                entry = 0, self.rooms[-1].end[1]
            if type:
                room = Room(room_x, self.rooms_size_y, entry, None)
                strategy = Platforms(room, 10)
                room.map = strategy.all(self.scene)
                self.rooms.append(room)
            else:
                room = Room(room_x, self.rooms_size_y, entry, None)
                strategy = Stairs(room, 10, self.scene)
                room.map = strategy.all()
                self.rooms.append(room)
            self.total_length += room.width
            type = not type
    def make_map(self):
        for i in self.rooms:
            for j in range(len(i.map)):
                self.map[j] += i.map[j]