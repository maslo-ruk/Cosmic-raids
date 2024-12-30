import pygame
import random

WIDTH = 30
HEIGHT = 30
COLOR = pygame.Color(215, 215, 215)


class Cell:
    def __init__(self, pos, type):
        self.pos = pos
        self.type = type
        self.cell_size = 30
        if self.type == 1:
            self.sym = '#'
        else:
            self.sym = '0'

    def update_sym(self):
        if self.type == 1:
            self.sym = '#'
        else:
            self.sym = '0'

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

    def generate(self):
        pass

class Platforms(Strategy):
    def __init__(self, room, plats_average):
        super().__init__(room)
        self.av = plats_average

    def generate(self):
        while True:
            vert_margin = random.choice[1,2]
            while True:
                break

