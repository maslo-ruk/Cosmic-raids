import pygame
from data.Block import Block


WIDTH = 30
HEIGHT = 60
SIZE = (WIDTH, HEIGHT)
SPEED = 6
JUMPSPEED = 14
GRAVI = 0.8
COLOR = 'red'
POS = (250, 200)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_speed = SPEED
        self.xvel = 0
        self.y_speed = 0
        self.inair = True
        self.size = SIZE
        self.pos = POS
        self.rect = pygame.Rect(POS, SIZE)
        self.image = pygame.Surface(SIZE)
        self.image.fill(COLOR)
        self.col1 = False
        self.col2 = False

    def update(self, a, b, c, rects):
        if a:
            self.xvel = self.x_speed
        if b:
            self.xvel = -self.x_speed
        if (not a) and (not b):
            self.xvel = 0
        self.rect.x += self.xvel
        self.col1 = self.collides(rects)
        if self.col1 and (self.xvel > 0):
            self.rect.right = self.col1.left
        if self.col1 and (self.xvel < 0):
            self.rect.left = self.col1.right

        if self.inair:
            self.y_speed += GRAVI
        if c and not self.inair:
            self.inair = True
            self.y_speed = -JUMPSPEED
        self.rect.y += self.y_speed
        self.col2 = self.collides(rects)
        if self.col2 and (self.y_speed < 0):
            self.rect.top = self.col2.bottom
            self.y_speed = 0
        if self.col2 and (self.y_speed > 0):
            self.rect.bottom = self.col2.top
            self.y_speed = 0
            self.inair = False
        if not self.col2:
            self.inair = True

    def collides(self, rects: list[Block]):
        for i in rects:
            if self.rect.colliderect(i.rect):
                return i.rect
        return False
