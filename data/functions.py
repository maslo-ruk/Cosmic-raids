import pygame
import random
from data.config import *

def camera_conf(camera, target):
    pos_x, pos_y = target.center
    _, _, width, height = camera
    pos_x, pos_y = WINDOW_SIZE[0] // 2 - pos_x, WINDOW_SIZE[1] // 2 - pos_y
    pos_x = min(pos_x, 0)
    pos_x = max(-(ROOM_SIZE[0] - width), pos_x)
    pos_y = min(pos_y, 0)
    pos_y = max(-(ROOM_SIZE[1] - height), pos_y)
    return pygame.Rect(pos_x, pos_y, width, height)


def sep(len, amount):
    av = len // amount
    pos = 0
    res = []
    for i in range(amount):
        res.append(av)
        pos += av
    if pos < len:
        for i in range(len - pos):
            ind = random.randrange(0, amount)
            res[ind] += 1
    disp_amount = amount // 2
    for i in range(disp_amount):
        delta = random.randrange(av // 2)
        ind = random.randrange(0, amount)
        if ind == amount:
            dir = -1
        elif ind == 0:
            dir = 1
        else:
            dir = random.choice([1, -1])
        while delta >= res[ind + dir] - 2:
            delta -= 1
        res[ind] += delta
        res[ind + dir] -= delta
    print(len, sum(res))
    return res