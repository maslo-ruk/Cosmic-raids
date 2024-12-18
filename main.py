import pygame

pygame.init()
screen_info = pygame.display.Info()

width = screen_info.current_w
height = screen_info.current_h

print("Ширина экрана:", width)
print("Высота экрана:", height)