import pygame
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

def camera_confi(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WINDOW_SIZE[0] / 2, -t+WINDOW_SIZE[1] / 2

    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-ROOM_SIZE[0]), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-WINDOW_SIZE[1]), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы

    return pygame.Rect(l, t, w, h)