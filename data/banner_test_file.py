#тест среда для баннера
import pygame
from data.buttons import Button


pygame.init()
screen_info = pygame.display.Info() #узнаем размеры экрана пользователя
width = screen_info.current_w #ширина
height = screen_info.current_h #высота

increase_byx = (width / 631) #увеличение по x и y
increase_byy = (height / 330)
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
pygame.display.set_caption("Тестовый баннер")
running = True

def main_banner():
    fon = pygame.image.load("../images/for_banner/fone_for_banner_test.png")
    fon = pygame.transform.scale(fon, (width, height))
    screen.blit(fon, (0, 0))
    banner = pygame.image.load("../images/for_banner/place_for_character_test.png")
    banner = pygame.transform.scale(banner, (width, height))
    screen.blit(banner, (0, 0))
    do_it_1 = Button(0, 0, width, height, '', "../images/for_banner/do_it_1_test.png",
                     "../images/for_banner/do_it_1_test2.png", '',
                     (486 * (width / 1536), 952 * (width / 1536)), (707 * (height / 864), 794 * (height / 854)))
    do_it_10 = Button(0, 0, width, height, '', "../images/for_banner/do_it_10_test.png",
                      "../images/for_banner/do_it_10_test2.png", '',
                      (998 * (width / 1536), 1462 * (width / 1536)), (707 * (height / 864), 794 * (height / 854)))
    shoping = Button(0, 0, width, height, '', "../images/for_banner/shop_test.png",
                     "../images/for_banner/shop_test2.png", '',
                     (65 * (width / 1536), 306 * (width / 1536)), (707 * (height / 864), 794 * (height / 854)))
    close = Button(0, 0, width, height, '', "../images/for_banner/close_butn.png",
                   "../images/for_banner/close_butn2.png", '',
                   (11 * (width / 1536), 63 * (width / 1536)), (6 * (height / 864), 66 * (height / 854)))
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                close.events()
                do_it_1.events()
                if close.events():
                    exit()
            do_it_1.events()
            do_it_10.events()
            shoping.events()
            close.events()
            # выход через esc
        screen.blit(fon, (0, 0))
        screen.blit(banner, (0, 0))
        do_it_1.check_mishka(pygame.mouse.get_pos())
        do_it_1.draw(screen)
        do_it_10.check_mishka(pygame.mouse.get_pos())
        do_it_10.draw(screen)
        shoping.check_mishka(pygame.mouse.get_pos())
        shoping.draw(screen)
        close.check_mishka(pygame.mouse.get_pos())
        close.draw(screen)
        pygame.display.flip()
        dt = clock.tick(30) / 1000

    pygame.quit()