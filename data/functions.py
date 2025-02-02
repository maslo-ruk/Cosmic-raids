import pygame
import random
from data.config import *
import networkx as nx

def camera_conf(camera, target, scene):
    r_s = scene.size
    pos_x, pos_y = target.center
    _, _, width, height = camera
    pos_x, pos_y = WINDOW_SIZE[0] // 2 - pos_x, WINDOW_SIZE[1] // 2 - pos_y
    pos_x = min(pos_x, 0)
    pos_x = max(-(r_s[0] - width), pos_x)
    pos_y = min(pos_y, 0)
    pos_y = max(-(r_s[1] - height), pos_y)
    return pygame.Rect(pos_x, pos_y, width, height)


def sep(length, amount):
    av = length // amount
    pos = 0
    res = []
    for i in range(amount):
        res.append(av)
        pos += av
    if pos < length:
        for i in range(length - pos):
            ind = random.randrange(0, amount)
            res[ind] += 1
    disp_amount = amount // 2
    for i in range(disp_amount):
        try:
            delta = random.randrange(av // 2)
        except Exception:
            break
        ind = random.randrange(0, amount)
        if ind == amount - 1:
            dir = -1
        elif ind == 0:
            dir = 1
        else:
            dir = random.choice([1, -1])
        while delta >= res[ind + dir] - 2:
            delta -= 1
        res[ind] += delta
        res[ind + dir] -= delta
    return res
import pygame, sqlite3

def cast_ray(self_pos, target_pos, rects):
    for i in rects:
        if i.rect.clipline(target_pos, self_pos):
            return False
    return True

def generate(size):
    pass

def get_character():
    con = sqlite3.connect('db/characters_and_achievements.sqlite')
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM characters
                WHERE selected = 1""").fetchall()
    return result

def get_level():
    con = sqlite3.connect('db/characters_and_achievements.sqlite')
    cur = con.cursor()
    result = cur.execute("""SELECT cur_level FROM player
                    WHERE id = 1""").fetchall()
    return result

def make_graph(map):
    graph = nx.Graph()
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '0':
                graph.add_node((i, j))
                if j != len(map[i]) - 1:
                    if map[i][j+1] == '0':
                        graph.add_node((i, j+ 1))
                        graph.add_edge((i, j), (i, j + 1))
                if i != len(map) - 1:
                    if map[i+ 1][j] == '0':
                        graph.add_node((i + 1, j))
                        graph.add_edge((i, j), (i + 1, j))
    return graph


def make_new_game():
    con = sqlite3.connect('db/characters_and_achievements.sqlite')
    cur = con.cursor()
    result = cur.execute("""INSERT INTO player(cur_level, completed_levels) VALUES(0, 0)""").fetchall()
