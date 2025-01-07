import pygame
from data.Block import Block

WIDTH = 30
HEIGHT = 30
SIZE = (WIDTH, HEIGHT)
SPEED = 6
JUMPSPEED = 14
GRAVI = 0.8
COLOR = 'red'
POS = (250, 200)


class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, speed):
        super().__init__()
        self.hp = 10
        self.x_speed = SPEED
        self.xvel = 0
        self.y_speed = 0
        self.inair = True
        self.size = SIZE
        self.pos = pos
        self.rect = pygame.Rect(self.pos, self.size)
        self.image = pygame.Surface(self.size)
        self.image.fill(COLOR)
        self.col1 = False
        self.col2 = False
        self.all_b = pygame.sprite.Group()
        self.lines = pygame.sprite.Group()
        self.is_alive = True

    def update(self, *args, **kwargs):
        if self.hp <= 0:
            self.die()

    def shoot(self, dest_x, dest_y):
        from data.Projectiles import Bullets
        dx = dest_x - self.rect.x
        dy = dest_y - self.rect.y
        angle = (dx, dy)
        if dx != 0 or dy != 0:  # Проверка для избежания деления на ноль
            norm = (dx ** 2 + dy ** 2) ** 0.5
            direction = (dx / norm, dy / norm)
            line = Bullets(self.rect.center, direction)
            self.all_b.add(line)
            self.lines.add(line)

    def die(self):
        self.is_alive = False
        self.kill()

    def collides(self, rects: list[Block]):
        for i in rects:
            if self.rect.colliderect(i.rect) and i.rect != self.rect:
                return i.rect
        return False


class Player(Entity):
    def __init__(self, POS1):
        super().__init__(POS1, SPEED)
        self.x_speed = SPEED
        self.kolvo = 5
        self.count = self.kolvo


    def update(self, screen, a, b, c, rects):
        super().update()
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

        self.lines.update(rects, self.rect)
        self.all_b.draw(screen)

ENEMY_SPEED = 3.5

class Enemy(Entity):
        def __init__(self, pos):
            super().__init__(pos, ENEMY_SPEED)
            self.x_speed = ENEMY_SPEED
            self.hp = 5
            self.x_vision = 12
            self.y_vision = 4
            self.x_shooting = 6
            self.randdir = 0
            self.rand_stat = False
            self.see_player = False

        def update(self, screen, rects, player_pos):
            super().update()
            if abs(self.rect.x - player_pos.x) <= self.x_vision * 30 and abs(
                    self.rect.y - player_pos.y) <= self.y_vision * 30:
                if abs(self.rect.x - player_pos.x) > self.x_shooting * 30:
                    self.see_player = False
                    if self.rect.x < player_pos.x:
                        self.xvel = 1
                    elif self.rect.x > player_pos.x:
                        self.xvel = -1
                    else:
                        self.xvel = 0
                else:
                    self.see_player = True
                    self.xvel = 0
            else:
                self.see_player = False
                self.xvel = 0
                self.move_to_player(self.randdir, rects)
            self.move_to_player(self.xvel, rects)
            self.lines.update(rects, self.rect)
            self.all_b.draw(screen)

        def move_to_player(self, vel, rects):
            self.rect.x += self.x_speed * vel
            self.col1 = self.collides(rects)
            if self.col1 and (vel > 0):
                self.rect.right = self.col1.left
            if self.col1 and (vel < 0):
                self.rect.left = self.col1.right

        def random_move(self):
            import random
            self.rand_stat = not self.rand_stat
            if self.rand_stat:
                self.randdir = random.choice([0.4, -0.4])
            else:
                self.randdir = 0