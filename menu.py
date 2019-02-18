from pygame import draw, Color
import pygame

from button import Button


class Button_menu(Button):
    def draw(self):
        if self.img is None:
            draw.rect(self.surface, Color(self.color), (self.x, self.y, self.size_x, self.size_y))

            font = pygame.font.Font(None, self.size_y)
            text = font.render(self.text, 1, Color("White"))
            screen.blit(text, (self.x, self.y))

        else:
            if self.img is str:
                image = pygame.image.load(self.img).convert()
                self.surface.blit(image, image.get_rect())

            elif self.img is pygame.Surface:
                image = self.img
                self.surface.blit(image, image.get_rect())

        if self.is_active(pygame.mouse.get_pos()):
            draw.rect(self.surface, Color("yellow"), (self.x, self.y, self.size_x, self.size_y), 1)

    def pressed(self):
        pass


class Menu:
    def __init__(self, surface, width, height, s_x, s_y, size_b, step_b):
        self.surface = surface
        self.width = width
        self.height = height
        self.buttons = []
        self.s_x, self.s_y = s_x, s_y
        self.size_b = size_b
        self.step_b = step_b

        self.is_active = True

    def draw(self):
        for btn in self.buttons:
            btn.draw()

    def get_button(self, mouse_pos):
        for btn in self.buttons:
            if btn.is_active(mouse_pos):
                btn.pressed()

    def add_btn(self, btn):
        if btn is Button_menu:
            self.buttons.append(btn)


if __name__ == '__main__':
    pygame.init()

    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))

    menu = Menu(screen, 1280, 720, 0, 0, (100, 50), 10)

    while True:
        screen.fill(Color("white"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        menu.draw()
        pygame.display.flip()

