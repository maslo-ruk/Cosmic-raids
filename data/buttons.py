import pygame
class Button:
    def __init__(self, x_cord, y_cord, width, height, text, image_before, image_after=None, sound=None, diapazone_x=None, diapazone_y=None):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.w = width
        self.h = height
        self.text = text
        self.diapaz_x = diapazone_x
        self.diapaz_y = diapazone_y

        # self.flag = flag

        self.image_before = pygame.image.load(image_before).convert_alpha()
        self.image_before = pygame.transform.scale(self.image_before, (width, height))
        self.image_after = self.image_before

        if image_after:
            self.image_after = pygame.image.load(image_after).convert_alpha().convert_alpha()
            self.image_after = pygame.transform.scale(self.image_after, (width, height))
        self.rect = self.image_before.get_rect(topleft=(x_cord,y_cord))
        self.sound = None
        if sound:
            self.sound = pygame.mixer.Sound(sound)

        self.mishka_on = False

    def draw(self, screen):
        if self.mishka_on:
            current_img = self.image_after
        else:
            current_img = self.image_before
        screen.blit(current_img, self.rect.topleft)

        font = pygame.font.Font(None, 36)
        text_sur = font.render(self.text, True, ("white"))
        text_rect = text_sur.get_rect(center=self.rect.center)
        screen.blit(text_sur, text_rect)

    def check_mishka(self, mouse_pos):
        # print(mouse_pos)
        if self.diapaz_x and self.diapaz_y:
            if int(mouse_pos[0]) > int(self.diapaz_x[0]) and int(mouse_pos[0]) < int(self.diapaz_x[1]) and int(mouse_pos[1]) > int(self.diapaz_y[0]) and int(mouse_pos[1]) < int(self.diapaz_y[1]):
                self.mishka_on = True
            else:
                self.mishka_on = False
        else:
            self.mishka_on = self.rect.collidepoint(mouse_pos)
    def events(self):
        if self.mishka_on:
            # print("Вы нажали кнопку^^")
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
            return True

class Block_for_person:
        def __init__(self, x_cord, y_cord, width, height, text, image_before, image_after1=None, image_after2=None, sound=None, sound2=None,
                     diapazone_x=None, diapazone_y=None, person=None):
            self.x_cord = x_cord
            self.y_cord = y_cord
            self.w = width
            self.h = height
            self.text = text
            self.diapaz_x = diapazone_x
            self.diapaz_y = diapazone_y

            self.image_before = pygame.image.load(image_before)
            self.image_before = pygame.transform.scale(self.image_before, (width, height))
            self.image_after = self.image_before
            self.mishka_on = True

            if image_after1:
                self.image_after1 = pygame.image.load(image_after1).convert_alpha()
                self.image_after1 = pygame.transform.scale(self.image_after1, (width, height))
            if image_after2:
                self.image_after2 = pygame.image.load(image_after2).convert_alpha()
                self.image_after2 = pygame.transform.scale(self.image_after2, (width, height))
            self.rect = self.image_before.get_rect(topleft=(x_cord, y_cord))
            self.sound = sound
            self.sound2 = sound2
            if sound:
                self.sound = pygame.mixer.Sound(sound)
            self.clicked = 0
            #дальше пойдет функция для пасхалки(реакция только на одного персонажа)
            self.persona = person

        def draw(self, screen):
            if self.persona is False:
                current_img = self.image_before
                if self.clicked > 5:
                    current_img = self.image_after1
            else:
                current_img = self.image_after2
                if self.sound2:
                    self.sound2.play()
                    #проигрывается особая фраза
            screen.blit(current_img, self.rect.topleft)

            font = pygame.font.Font(None, 36)
            text_sur = font.render(self.text, True, ("white"))
            text_rect = text_sur.get_rect(center=self.rect.center)
            screen.blit(text_sur, text_rect)

        def check_mishka(self, mouse_pos):
            # print(mouse_pos)
            if self.diapaz_x and self.diapaz_y:
                if int(mouse_pos[0]) > int(self.diapaz_x[0]) and int(mouse_pos[0]) < int(self.diapaz_x[1]) and int(
                        mouse_pos[1]) > int(self.diapaz_y[0]) and int(mouse_pos[1]) < int(self.diapaz_y[1]):
                    self.mishka_on = True
                else:
                    self.mishka_on = False
            else:
                self.mishka_on = self.rect.collidepoint(mouse_pos)
        def clicking(self):
            # print(self.mishka_on)
            if self.mishka_on:
                self.clicked += 1
                print("Да")

        def events(self):
            if self.mishka_on:
                if self.sound:
                    self.sound.play()
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
                return True

