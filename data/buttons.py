import pygame
class Button:
    def __init__(self, x_cord, y_cord, width, height, text, image_before, image_after=None, sound=None):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.w = width
        self.h = height
        self.text = text

        self.image_before = pygame.image.load(image_before)
        self.image_before = pygame.transform.scale(self.image_before, (width, height))
        self.image_after = self.image_before

        if image_after:
            self.image_after = pygame.image.load(image_after)
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
        self.mishka_on = self.rect.collidepoint(mouse_pos)
    def events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.mishka_on:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
            print("Привета")
