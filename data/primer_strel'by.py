import pygame
import random
import sys

BALL_RADIUS = 20
LINE_WIDTH = 5
LINE_COLOR = (255, 0, 0)
BALL_COLOR = (0, 0, 255)
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('TESTS')
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0


class Line(pygame.sprite.Sprite):
    def __init__(self, start_pos, angle):
        super().__init__()
        self.image = pygame.Surface((LINE_WIDTH, 5))
        self.image.fill(LINE_COLOR)
        self.rect = self.image.get_rect(center=start_pos)
        self.angle = angle

    def update(self):
        # Двигаем линию в зависимости от угла
        self.rect.x += 10 * self.angle[0]
        self.rect.y += 10 * self.angle[1]

        # Удаляем линию, если она выходит за границы экрана
        if self.rect.x < 0 or self.rect.x > 1280 or self.rect.y < 0 or self.rect.y > 720:
            self.kill()




# Создаем группы спрайтов
all_sprites = pygame.sprite.Group()
lines = pygame.sprite.Group()



# Основной игровой цикл
while True:
    screen.fill("WHITE")  # розовый фон
    all_sprites.draw(screen)
    pygame.draw.circle(screen, "black", player_pos, 40)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = mouse_x - player_pos.x
                dy = mouse_y - player_pos.y
                angle = (dx, dy)
                if dx != 0 or dy != 0:  # Проверка для избежания деления на ноль
                    norm = (dx ** 2 + dy ** 2) ** 0.5
                    direction = (dx / norm, dy / norm)
                    line = Line(player_pos, direction)
                    all_sprites.add(line)
                    lines.add(line)


# Обновление спрайтов
    all_sprites.update()



    pygame.display.flip()
    clock.tick(60)
    dt = clock.tick(60) / 1000