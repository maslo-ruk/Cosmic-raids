# Тест меню
import pygame
from data.buttons import Button

# pygame setup
pygame.init()
screen_info = pygame.display.Info() #узнаем размеры экрана пользователя
width = screen_info.current_w #ширина
height = screen_info.current_h #высота

increase_byx = (width / 631) #увеличение по x и y
increase_byy = (height / 330)
print("Ширина экрана:", width)
print("Высота экрана:", height)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

start_button = Button(0, 0, width, height, '', "../images/start_textures.png", "../images/start_textures2.png", '',
                           (643*(width/1536), 893*(width/1536)), (307*(height/864), 578*(height/854)))
new_game_button = Button(0, 0, width, height, '', "../images/newGametextures.png", "../images/newGametextures2.png", '',
                           (610, 922), (612, 727))
settings_button = Button(0, 0, width, height, '', "../images/menu_textures.png", "../images/menu_textures2.png", '',
                           (37, 143), (40, 154))
clock = pygame.time.Clock()
pygame.display.set_caption("Тестовое меню")
running = True

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
        start_button.events(event)
        new_game_button.events(event)
        settings_button.events(event)
        # if settings_button.events(event) == False:
        #     pygame.quit()
        #     exit()
            # выход через esc
    fon = pygame.image.load("../images/Space_sky.png")
    fon = pygame.transform.scale(fon, (width, height))
    screen.blit(fon, (0, 0))
    planet1 = pygame.image.load("../images/planet.png")
    planet1 = pygame.transform.scale(planet1, (width, height))
    screen.blit(planet1, (0, 0))
    planet2 = pygame.image.load("../images/planet2.png")
    planet2 = pygame.transform.scale(planet2, (width, height))
    screen.blit(planet2, (0, 0))
    galaktika1 = pygame.image.load("../images/Galactika1.png")
    galaktika1 = pygame.transform.scale(galaktika1, (width -50, height-50))
    screen.blit(galaktika1, (0, 0))
    galaktika2 = pygame.image.load("../images/galactika2.png")
    galaktika2 = pygame.transform.scale(galaktika2, (width, height))
    screen.blit(galaktika2, (0, 0))
    planet2 = pygame.image.load("../images/planet2.png")
    planet2 = pygame.transform.scale(planet2, (width, height))
    screen.blit(planet2, (0, 0))
    planetka = pygame.image.load("../images/mini_planetka.png")
    planetka = pygame.transform.scale(planetka, (width, height))
    screen.blit(planetka, (0, 0))
    exit_esc = pygame.image.load("../images/Exit.png")
    exit_esc = pygame.transform.scale(exit_esc, (width, height))
    screen.blit(exit_esc, (0, 0))


    #Дальше идут важные кнопки для самой игры
    start_button.check_mishka(pygame.mouse.get_pos())
    start_button.draw(screen)
    new_game_button.check_mishka(pygame.mouse.get_pos())
    new_game_button.draw(screen)
    settings_button.check_mishka(pygame.mouse.get_pos())
    settings_button.draw(screen)
    pygame.display.flip()
    dt = clock.tick(30) / 1000

pygame.quit()
