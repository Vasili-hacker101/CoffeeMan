from pygame import draw, Color
import pygame


from functions import *
from abc import ABC, abstractmethod


class Button(ABC):
    def __init__(self, surface, x, y, size_x, size_y, text, image=None, color="black"):
        self.x, self.y = x, y
        self.size_x = size_x
        self.size_y = size_y
        self.rect = (x, y, size_x, size_y)
        print(self.rect)
        self.surface = surface
        self.img = check_img(image, (size_x, size_y))
        self.color = color
        self.text = text

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def pressed(self):
        pass

    def is_active(self, mouse_pos):
        x, y = mouse_pos
        return 0 <= x - self.x <= self.size_x and 0 <= y - self.y <= self.size_y


class Button_menu(Button):
    def draw(self):
        if self.img is None:
            draw.rect(self.surface, Color(self.color), (self.x, self.y, self.size_x, self.size_y))

        else:
            self.surface.blit(self.img, self.rect)

        font = pygame.font.Font(None, self.size_y)
        text = font.render(self.text, 1, Color("White"))
        x, y = font.size(self.text)
        x, y = (self.size_x - x) // 2, (self.size_y - y) // 2
        self.surface.blit(text, (self.x + x, self.y + y))

        if self.is_active(pygame.mouse.get_pos()):
            draw.rect(self.surface, Color("yellow"), (self.x, self.y, self.size_x, self.size_y), 1)

    def pressed(self):
        data = get_data()

        data["game_status"] = self.text.lower()

        set_data(data)


