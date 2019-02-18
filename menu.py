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
            check_img(self.img)

        if self.is_active(pygame.mouse.get_pos()):
            draw.rect(self.surface, Color("yellow"), (self.x, self.y, self.size_x, self.size_y), 1)

    def pressed(self):
        pass


class Menu:
    def __init__(self, surface, width, height, s_x, s_y, size_b, step_b, image=None):
        self.surface = surface
        self.width = width
        self.height = height
        self.buttons = []
        self.s_x, self.s_y = s_x, s_y
        self.size_b = size_b
        self.step_b = step_b
        self.img = image if type(image) in [str, pygame.Surface] else None

        self.is_active = True

    def draw(self):
        if self.img is not None:
            image = check_img(self.img)

            self.surface.blit(image, image.get_rect())

        for btn in self.buttons:
            btn.draw()

    def get_button(self, mouse_pos):
        for btn in self.buttons:
            if btn.is_active(mouse_pos):
                btn.pressed()

    def add_btn(self, btn):
        if btn is Button_menu:
            self.buttons.append(btn)


def check_img(img):
    if type(img) is str:
        image = pygame.image.load(f".resource/menu/{img}").convert()

    else:
        image = img

    return image


if __name__ == '__main__':
    pygame.init()

    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))

    menu = Menu(screen, 1280, 720, 0, 0, (100, 50), 10, image="background.jpg")

    while True:
        screen.fill(Color("white"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        menu.draw()
        pygame.display.flip()

