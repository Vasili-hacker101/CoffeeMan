from pygame import Color, draw
import pygame

from functions import check_img


class Level:
    def __init__(self, surface, start_and_size, cell_size, image=None):
        self.surface = surface
        self.rect = start_and_size  # (x, y, size_x, size_y)
        self.cell_size = cell_size
        x, y, size_x, size_y = start_and_size
        self.img = check_img(image, (size_x, size_y))
        self.objects = {"wall": []}

    def draw(self, wall=False, sheet=False):
        if self.img is None:
            self.surface.fill(Color("black"))

        else:
            self.surface.blit(self.img, self.rect)

        if wall:
            for w in self.objects["wall"]:
                    draw.rect(self.surface, Color("red"), (self.cell_size * w[0], self.cell_size * w[1],
                                                           self.cell_size, self.cell_size))
        if sheet:
            x, y, size_x, size_y = self.rect

            for x in range((size_x - x) // self.cell_size + 1):
                for y in range((size_y - y) // self.cell_size + 1):
                    draw.rect(self.surface, Color("grey"), (self.cell_size * x, self.cell_size * y,
                                                            self.cell_size, self.cell_size), 1)

    def set_image(self, img):
        self.img = img if type(img) in [str, pygame.Surface] else None

    def set_cell(self, pos, code=-1):
        for k, o in self.objects.items():  # Чиститься старое значение
            if pos in o:
                del self.objects[k][o.index(pos)]

        if code != -1:
            k = list(self.objects)[code]
            self.objects[k].append(pos)

    def is_clear(self, cord):
        return not [1 for o in self.objects.values() if cord in o]

    def get_cell(self, mouse_pos):
        x, y = mouse_pos

        return x // self.cell_size, y // self.cell_size


if __name__ == '__main__':
    pygame.init()

    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))

    level = Level(screen, (0, 0, width, height), 40, image="resource/menu/background.jpg")

    while True:
        screen.fill(Color("white"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_focused():
                if event.button == 1:
                    pos = level.get_cell(pygame.mouse.get_pos())

                    code = 0 if level.is_clear(pos) else -1

                    level.set_cell(pos, code)

        level.draw(wall=True, sheet=True)
        pygame.display.flip()
