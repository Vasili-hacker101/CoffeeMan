from pygame import Color
import pygame

from buttons import Button_menu
from functions import check_img


class Menu:
    def __init__(self, surface, width, height, s_x=0, s_y=0, text="Menu", image=None):
        self.surface = surface
        self.width = width
        self.height = height
        self.buttons = [Button_menu(surface, 490, 200, 300, 100, "Play", image="resource/menu/background.jpg"),
                        Button_menu(surface, 490, 350, 300, 100, "Settings"),
                        Button_menu(surface, 490, 500, 300, 100, "Exit")]
        self.x, self.y = s_x, s_y
        self.text = text
        self.img = check_img(image, (width - s_x, height - s_y))

    def draw(self):
        if self.img is not None:
            self.surface.blit(self.img, (self.x, self.y, self.width, self.height))

        font = pygame.font.Font(None, 100)
        size = font.size(self.text)
        text = font.render(self.text, 1, Color("White"))
        screen.blit(text, ((self.width - self.x - size[0]) // 2, self.y + 50))

        for btn in self.buttons:
            btn.draw()

    def get_pressed(self, mouse_pos):
        for btn in self.buttons:
            if btn.is_active(mouse_pos):
                btn.pressed()

    def add_btn(self, btn):
        if type(btn) is Button_menu:
            self.buttons.append(btn)


if __name__ == '__main__':
    pygame.init()

    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))

    menu = Menu(screen, width, height, image="resource/menu/background.jpg")

    while True:
        screen.fill(Color("white"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    menu.get_pressed(pygame.mouse.get_pos())

        menu.draw()
        pygame.display.flip()

