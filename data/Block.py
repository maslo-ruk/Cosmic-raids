import random

import pygame
from data.config import *

COLOR = pygame.Color(215, 215, 215)

class Images:
    def __init__(self):
        self.size = (CELL_SIZE, CELL_SIZE)
        kubik1 = pygame.image.load("images/for_hub/kubic_1.png")
        kubik1 = pygame.transform.scale(kubik1, self.size)
        kubik2 = pygame.image.load("images/for_hub/kubik_2.png")
        kubik2 = pygame.transform.scale(kubik2, self.size)
        self.imags = [kubik1, kubik2, kubik1]

imag = Images()
imags = imag.imags

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, screen):
        super().__init__()
        self.size = (CELL_SIZE, CELL_SIZE)
        # kubik1 = pygame.image.load("images/for_hub/kubic_1.png")
        # kubik1 = pygame.transform.scale(kubik1, self.size).convert_alpha()
        # kubik2 = pygame.image.load("images/for_hub/kubik_2.png")
        # kubik2 = pygame.transform.scale(kubik2, self.size).convert_alpha()
        # imags = [kubik1, kubik2, kubik1]
        self.pos = pos
        self.rect = pygame.Rect(self.pos, self.size)
        self.image = random.choice(imags).convert_alpha()
        self.screen = screen

class Door(pygame.sprite.Sprite):
    def __init__(self, pos, screen):
        super().__init__()
        self.size = (CELL_SIZE, CELL_SIZE)
        # kubik1 = pygame.image.load("images/for_hub/kubic_1.png")
        # kubik1 = pygame.transform.scale(kubik1, self.size).convert_alpha()
        # kubik2 = pygame.image.load("images/for_hub/kubik_2.png")
        # kubik2 = pygame.transform.scale(kubik2, self.size).convert_alpha()
        # imags = [kubik1, kubik2, kubik1]
        self.pos = pos
        self.rect = pygame.Rect(self.pos, self.size)
        self.image = random.choice(imags).convert_alpha()
        self.screen = screen
