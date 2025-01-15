import pygame
from data.config import *

small_camera_size = 5 * CELL_SIZE, 3*CELL_SIZE


class Camera:
    def __init__(self, pos):
        self.outer_rect = pygame.Rect(0, 0, WINDOW_SIZE[0], WINDOW_SIZE[1])
        pos_x = pos[0] + self.outer_rect.x // 2 - small_camera_size[0] // 2
        pos_y = pos[1] + self.outer_rect.y // 2 - small_camera_size[1] // 2
        self.inner_rect = pygame.Rect(pos_x, pos_y, small_camera_size[0], small_camera_size[1])
        self.dx = 0
        self.dy = 0

    def apply(self, target):
        self.dx = self.outer_rect.center[0] - target.rect.center[0]
        self.dy = self.outer_rect.center[1] - target.rect.center[1]

    def update(self, sprite):
            sprite.rect.x += self.dx
            sprite.rect.y += self.dy