import pygame
from data.config import *

small_camera_size = 5 * CELL_SIZE, 3*CELL_SIZE


class Camera(object):
    def __init__(self, camera_func, width, height, scene):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.scene = scene

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def apply_point(self, target):
        return target[0] - self.state.left, target[1] - self.state.top

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect, self.scene)