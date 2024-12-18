# Тест меню
import pygame
import pygame_gui

# pygame setup
pygame.init()
screen_info = pygame.display.Info() #узнаем размеры экрана пользователя
width = screen_info.current_w #ширина
height = screen_info.current_h #высота

increase_byx = (width / 631) #увеличение по x и y
increase_byy = (height / 330)
# print("Ширина экрана:", width)
# print("Высота экрана:", height)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

clock = pygame.time.Clock()
pygame.display.set_caption("Тестовое меню")
running = True

# start_button = pygame.image.load("../images/start_textures.png")
# start_button = pygame.transform.scale(start_button, (width, height))
# screen.blit(start_button, (0, 0))
pygame.display.update()
fon = pygame.image.load("../images/Space_sky.png")
fon = pygame.transform.scale(fon, (width, height))
screen.blit(fon, (0, 0))
            # выход через esc
manager = pygame_gui.UIManager((width, height))
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (height, width)),
                                                text='Say Hello',
                                                manager=manager)
dt = clock.tick(30) / 1000
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element == hello_button:
            print('Hello World!')
    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()


pygame.quit()