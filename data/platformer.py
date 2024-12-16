import pygame
from player import Player

pygame.init()
size = width, height = 500, 500
bottom = pygame.Rect(0, 400, 500, 100)
left = pygame.Rect(25, 300, 200, 50)
print(left.bottom)
right = pygame.Rect(275, 300, 200, 50)
rects = [bottom, right, left]
borders_x, borders_y = ([0, 400], [0, 400])
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("shariki")
running = True


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
    keys = pygame.key.get_pressed()
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
    # tick = clock.tick(60)
    screen.fill('blue')
    for rect in rects:
        pygame.draw.rect(screen, 'green', rect)
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


    player.update(right, left, up, rects)
    all_b.draw(screen)
    screen.blit(player.image, (player.rect.x, player.rect.y))
    lines.update()
    pygame.display.flip()
    tick = clock.tick(60)
