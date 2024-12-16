import pygame
from player import Player
from Block import Block

pygame.init()
size = width, height = 900, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("shariki")
running = True
map = ['------------------------------',
       '-0000000000000000000000000000-',
       '-0000000000000000000000000000-',
       '-0000000-------00000000000000-',
       '-0000000000000000000000000000-',
       '-0000000000000000000000000000-',
       '---00000000000000000000000000-',
       '-0000000000000000000000000000-',
       '-0000000000000000000000000000-',
       '-000000000---0000000000000000-',
       '-0000000000000000000000000----',
       '-00000000000000---00000000000-',
       '-00000000000000000000----0000-',
       '-0000000000000000000000000000-',
       '-0000000000000000000000000000-',
       '-0000000-----0000000000000000-',
       '-0000000000000000000000000000-',
       '-0000000000000000000000000000-',
       '-0000000000000000000000000000-',
       '------------------------------']
blocks = pygame.sprite.Group()
for i in range(len(map)):
    string = map[i]
    for j in range(len(string)):
        pos = (j * 30, i * 30)
        if string[j] == '-':
            block = Block(pos, screen)
            blocks.add(block)

class Bullets(pygame.sprite.Sprite):
    def __init__(self, start_pos, angle):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=start_pos)
        self.angle = angle

    def update(self):
        # Двигаем линию в зависимости от угла
        self.rect.x += 10 * self.angle[0]
        self.rect.y += 10 * self.angle[1]

        # Удаляем линию, если она выходит за границы экрана
        if self.rect.x < 0 or self.rect.x > 1280 or self.rect.y < 0 or self.rect.y > 720:
            self.kill()


all_b = pygame.sprite.Group()
lines = pygame.sprite.Group()
player = Player()
right = False
left = False
up = False
while running:
    tick = clock.tick(60)
    screen.fill('blue')
    blocks.draw(screen)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = mouse_x - player.rect.x
                dy = mouse_y - player.rect.y
                angle = (dx, dy)
                if dx != 0 or dy != 0:  # Проверка для избежания деления на ноль
                    norm = (dx ** 2 + dy ** 2) ** 0.5
                    direction = (dx / norm, dy / norm)
                    line = Bullets(player.rect.center, direction)
                    all_b.add(line)
                    lines.add(line)
    if keys[pygame.K_d]:
        right = True
    else:
        right = False
    if keys[pygame.K_a]:
        left = True
    else:
        left = False
    if keys[pygame.K_SPACE]:
        up = True
    else:
        up = False

    all_b.draw(screen)
    player.update(right, left, up, blocks)
    screen.blit(player.image, (player.rect.x, player.rect.y))
    lines.update()
    pygame.display.flip()
