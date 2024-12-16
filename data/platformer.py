import pygame
from player import Player
from Block import Block

pygame.init()
size = width, height = 900, 600
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
map = ['-'*30]
count = 0
for i in range(18):
    if count % 2 == 1:
        map.append('-00--00000---000000000-000000-')
    else:
        map.append('-0000000000000000000000000000-')

player = Player()
right = False
left = False
up = False
while running:
    tick = clock.tick(60)
    screen.fill('white')
    # for y in range(len(map)):
    #     for x in range(len(map[y])):
    #         pos = y * 30, x * 30
    #         if map[y][x] == '-':
    #             block.place(pos)

    for rect in rects:
        pygame.draw.rect(screen, 'green', rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
    player.update(right, left, up, rects)
    screen.blit(player.image, (player.rect.x, player.rect.y))
    pygame.display.flip()
