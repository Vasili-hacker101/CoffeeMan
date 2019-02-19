from pygame import Color, draw
import pygame

from functions import check_img


class Level():
    def __init__(self, surface, start_and_size, cell_size, image=None):
        self.surface = surface
        self.rect = start_and_size  # (x, y, size_x, size_y)
        self.cell_size = cell_size
        self.img = image if type(image) in [str, pygame.Surface] else None
        self.wall = []

    def draw(self, wall=False, sheet=False):
        if self.img is not None:
            image = check_img(self.img)

            self.surface.blit(image, image.get_rect())

        else:
            self.surface.blit(Color("black"))

        if wall:
            for w in self.wall:
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

    def set_cell(self, pos, code):
        if pos in self.wall:  # Чиститься старое значение
            del self.wall[self.wall.index(pos)]

        if code == 1:
            self.wall.append(pos)

    def is_clear(self, cord):
        return cord not in self.wall

    def get_cell(self, mouse_pos):
        x, y = mouse_pos

        return x // self.cell_size, y // self.cell_size


if __name__ == '__main__':
    pygame.init()

    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))

    level = Level(screen, (0, 0, width, height), 40, image="background.jpg")

    while True:
        screen.fill(Color("white"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_focused():
                if event.button == 1:
                    pos = level.get_cell(pygame.mouse.get_pos())

                    code = 1 if level.is_clear(pos) else 0

                    level.set_cell(pos, code)

        level.draw(wall=True, sheet=True)
        pygame.display.flip()
