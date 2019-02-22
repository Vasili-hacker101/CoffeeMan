from pygame import draw, Color
import pygame

from functions import check_img
from level import Level


class Player:
    def __init__(self, surface, x, y, level, size=(1, 2), image=None):
        self.surface = surface
        self.x, self.y = x, y
        self.size_x, self.size_y = size
        self.location = level

        self.img = check_img(image, (level.cell_size, level.cell_size * 2))

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        cell = self.location.cell_size
        rect = (cell * self.x, cell * self.y, cell * self.size_x, cell * self.size_y)

        if self.img is None:
            draw.rect(self.surface, Color("black"), rect)

        else:
            self.surface.blit(self.img, rect)

    def set_image(self, img):
        self.img = check_img(img, (self.size_x, self.size_y))

    def set_size(self, size):
        self.size_x, self.size_y = size
        self.img = check_img(self.img, size)

    def can_move(self, x, y):
        """
        Working in process
        This function check all cell for new pos
        and return True, if all cell is clear
        """
        pass


if __name__ == '__main__':
    pygame.init()

    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))

    level = Level(screen, (0, 0, width, height), 40, image="resource/menu/background.jpg")
    player = Player(screen, 5, 5, level)

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if level.is_clear((player.x - 1, player.y)):
                        player.move(-1, 0)

                if event.key == pygame.K_RIGHT:
                    if level.is_clear((player.x + 1, player.y)):
                        player.move(1, 0)

                if event.key == pygame.K_DOWN:
                    player.move(0, 1)
                    player.set_size((player.size_x, player.size_y // 2))

                print(level.wall)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player.move(0, -1)
                    player.set_size((player.size_x, player.size_y * 2))

        level.draw(wall=True, sheet=True)
        player.draw()
        pygame.display.flip()
