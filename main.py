# Example file showing a circle moving on screen
# Примеры событий
# python -m pygame.examples.eventlist

import pygame

# pygame setup
pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("Белий кролик")
running = True
MYEVENTTYPE = pygame.USEREVENT + 1
pygame.time.set_timer(MYEVENTTYPE, 1000)

while running:
    screen.fill("purple")
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.circle(screen, 'white', event.pos, 20)
            pygame.draw.ellipse(screen, 'white', (event.pos[0] - 15,
                                                  event.pos[1] - 40, 10, 40), 20)
            pygame.draw.ellipse(screen, 'white', (event.pos[0] + 5,
                                                  event.pos[1] - 40, 10, 40), 20)
        if event.type == MYEVENTTYPE:
            print("Мое событие")

    pygame.display.flip()
    # limits FPS to 60
    # independent physics.
    dt = clock.tick(30) / 1000

pygame.quit()
