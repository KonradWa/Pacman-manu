import pygame as pg

# Object tekstowy
class Text:
    def __init__(self, text, text_color, pc_x, pc_y, font_size=32, font_family=None, menu = False):
        self.text = str(text)
        self.text_color = text_color
        self.font_family = font_family
        self.font_size = font_size
        self.font = pg.font.Font("assets/PressStart2P-Regular.ttf", self.font_size)
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect()
        self.pc_x = pc_x
        self.pc_y = pc_y
        if menu:
            self.rect.center = pc_x, pc_y
        else:
            self.rect.topleft = pc_x, pc_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pc_x, self.pc_y

class Button:
    def __init__(self, text, text_color, bg_color, border_color, width, height, pc_x, pc_y, status, font_size=78,
                 font_family=None, menu = False):
        self.bg_color = bg_color
        self.border_color = border_color
        self.width = width
        self.height = height
        self.status = status

        self.text = Text(text, text_color, pc_x, pc_y, font_size, font_family, menu)
        self.rect = pg.Rect(0, 0, self.width - 3, self.height - 3)
        self.rect.center = self.text.rect.center
        self.rect2 = pg.Rect(0, 0, self.width + 1, self.height + 1)
        self.rect2.center = self.text.rect.center

    def draw(self, surface):
        surface.fill(self.border_color, self.rect2)
        surface.fill(self.bg_color, self.rect)
        self.text.draw(surface)
        # surface.blit(self.image, self.rect)