import pygame
from data.Block import Block

WIDTH = 30
HEIGHT = 60
SIZE = (WIDTH, HEIGHT)
SPEED = 6
JUMPSPEED = 14
GRAVI = 0.8
COLOR = 'green'
POS = (250, 200)


class Entity(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.hp = 15
        self.x_speed = SPEED
        self.xvel = 0
        self.y_speed = 0
        self.inair = True
        self.size = SIZE
        self.pos = pos
        self.rect = pygame.Rect(self.pos, self.size)
        self.image = pygame.Surface(self.size)

        self.col1 = False
        self.col2 = False
        self.all_b = pygame.sprite.Group()
        self.lines = pygame.sprite.Group()
        self.is_alive = True


    def update(self, *args, **kwargs):
        if self.hp <= 0:
            self.kill()
            self.is_alive = False

    def shoot(self, dest_x, dest_y):
        from data.projectiles import Bullets
        dx = dest_x - self.rect.x
        dy = dest_y - self.rect.y
        angle = (dx, dy)
        if dx != 0 or dy != 0:  # Проверка для избежания деления на ноль
            norm = (dx ** 2 + dy ** 2) ** 0.5
            direction = (dx / norm, dy / norm)
            line = Bullets(self.rect.center, direction)
            self.all_b.add(line)
            self.lines.add(line)

    def throw(self, velocity, dest_x, dest_y):
        from data.projectiles import Grenade
        dx = dest_x - self.rect.centerx
        dy = dest_y - self.rect.centery
        norm = (dx ** 2 + dy ** 2) ** 0.5

        if norm != 0:  # Проверка для избежания деления на ноль
            direction = (dx / norm, dy / norm)

            self.velocity_x = velocity * dx / norm
            self.velocity_y = -velocity * dy / norm
            self.is_launched = True
            self.time = 0  # сброс времени для нового броска
            grenade = Grenade(self.rect.center, direction)
            self.all_b.add(grenade)

class Player(Entity):
    def __init__(self, POS1):
        super().__init__(POS1)
        self.x_speed = SPEED
        self.kolvo = 5
        self.count = self.kolvo
        self.image.fill('green')



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

    def collides(self, rects: list[Block]):
        for i in rects:
            if self.rect.colliderect(i.rect) and i.rect != self.rect:
                return i.rect
        return False


class Enemy(Entity):
    def __init__(self, pos):
        super().__init__(pos)
        self.image.fill('red')


    def update(self, screen, rects):
        super().update()
        self.lines.update(rects, self.rect)
        self.all_b.draw(screen)