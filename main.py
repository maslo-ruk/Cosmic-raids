import pygame
import sys
from data.buttons import Button

pygame.init()
width, hidth = 1000, 500

screen = pygame.display.set_mode((width, hidth))
button_test_1 = Button(width/2 -(631/2), 0, 631, 330, '',"start_textures.png", "start_textures2.png", '', (448, 549), (118, 220))

def main_menu():
    running = True
    while running:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            button_test_1.events(event)
        button_test_1.check_mishka(pygame.mouse.get_pos())
        button_test_1.draw(screen)
        pygame.display.flip()
main_menu()

