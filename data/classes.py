# Тест меню
import pygame

# pygame setup
pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("Тестовое меню")
running = True

while running:
    fon = pygame.image.load("../images/Space sky.png")
    fon = pygame.transform.scale(fon, (1280, 720))
    screen.blit(fon, (0, 0))
    galacktika1 = pygame.image.load("../images/Galactika1.png")
    galacktika1 = pygame.transform.scale(galacktika1, (800, 1000))
    screen.blit(galacktika1, (480, -300))
    galacktika2 = pygame.image.load("../images/Galactika2.png")
    galacktika2 = pygame.transform.scale(galacktika2, (800, 1000))
    screen.blit(galacktika2, (400, -300))
    spend_galackikas = 1
    galacktika2_y = -300
    galacktika1_y = -300
    while galacktika1_y < -280 and galacktika2_y < -280:
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(fon, (0, 0))
        # Изменяем значение координаты Y
        galacktika1_y += spend_galackikas
        galacktika2_y += spend_galackikas
        screen.blit(galacktika1, (480, galacktika1_y))
        screen.blit(galacktika2, (480, galacktika2_y))
        pygame.display.update()
    while galacktika1_y > -300 and galacktika2_y > -300:
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(fon, (0, 0))
        # Изменяем значение координаты Y
        galacktika1_y -= spend_galackikas
        galacktika2_y -= spend_galackikas
        screen.blit(galacktika1, (480, galacktika1_y))
        screen.blit(galacktika2, (480, galacktika2_y))
        pygame.display.update()
    # limits FPS to 60
    # independent physics.
    dt = clock.tick(30) / 1000

pygame.quit()
