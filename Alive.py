from pygame import draw, Color
import pygame

from functions import check_img
from level import Level
from other import Inventory


class Alive(pygame.sprite.Sprite):
    def __init__(self, group, x, y, level, damage=1, health=10, size=(1, 2), speed=(2, 2), image=None):
        super().__init__(group)

        self.x, self.y = x, y  # In cell
        self.size_x, self.size_y = size  # In cell
        cell = level.cell_size
        self.rect = [x * cell, y * cell, size[0] * cell, size[1] * cell]

        self.location = level
        self.surface = level.surface

        self.image = check_img("hello", (level.cell_size * size[0], level.cell_size * size[1]))

        self.speed = speed  # Speed in move (module)

        self.damage = damage

        self.hp = health

    def move(self, direction=None):

        if direction == "left" and self.location.is_clear((self.x - 1, self.y)):
            self.x -= 1

        elif direction == "right" and self.location.is_clear((self.x + 1, self.y)):
            self.x += 1

        elif direction == "up" and self.location.is_clear((self.x, self.y - 1)):
            self.y -= 2

        elif direction == "down" or (self.location.is_clear((self.x, self.y + self.size_y)) and
                                     self.y * self.location.cell_size == self.rect[1]):
            self.y += 1

    def attack(self, object):
        try:
            object.get_damage(self.damage)

        except AttributeError:
            print("This object is't Alive")

    def get_damage(self, damage):
        self.hp -= damage

    def update(self, *args):
        cell = self.location.cell_size

        if self.x * cell > self.rect[0]:
            self.rect[0] += self.speed[0]

            if self.x * cell < self.rect[0]:
                self.rect[0] = self.x * cell

        elif self.x * cell < self.rect[0]:
            self.rect[0] -= self.speed[0]

            if self.x * cell > self.rect[0]:
                self.rect[0] = self.x * cell

        if self.y * cell > self.rect[1]:
            self.rect[1] += self.speed[1]

            if self.y * cell < self.rect[1]:
                self.rect[1] = self.y * cell

        elif self.y * cell < self.rect[1]:
            self.rect[1] -= self.speed[0]

            if self.y * cell > self.rect[1]:
                self.rect[1] = self.y * cell

    def check_die(self):
        return self.hp > 0


class Player(Alive):
    def __init__(self, group, x, y, level, damage=1, health=10, size=(1, 2), speed=(2, 2), image=None):
        super().__init__(self, group, x, y, level, damage, health, size, speed, image)

        self.items = Inventory(level.surface, 240, 560, 80, 10)

    def check_item(self, item):
        return item in self.items

    def get_item(self, item):
        return self.items[item]

    def update(self, *args):
        super().update(*args)

        self.items.draw()


class Enemies(Alive):
    def __init__(self, group, x, y, e_x, level, damage=1, health=10, size=(1, 2), speed=(2, 2), image=None):
        super().__init__(self, group, x, y, level, damage, health, size, speed, image)

        self.e_x = e_x

    def update(self, *args):
        if self.x < self.e_x:
            if not self.location.is_clear(self.x + 1, self.y):
                self.move("up")
            self.move("right")

        else:
            if not self.location.is_clear(self.x - 1, self.y):
                self.move("up")
            self.move("left")

        super().update(args)


if __name__ == '__main__':
    pygame.init()

    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))

    level = Level(screen, (0, 0, width, height), 40, image="resource/menu/background.jpg")
    level.set_cell((5, 11), 0)
    all_sprites = pygame.sprite.Group()
    movable = Alive(all_sprites, 5, 5, level, image="resource/menu/background.jpg")

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movable.move("left")

                if event.key == pygame.K_RIGHT:
                   movable.move("right")

                if event.key == pygame.K_DOWN:
                    movable.move("down")

                if event.key == pygame.K_UP:
                    movable.move("up")

        level.draw(wall=True, sheet=True)
        movable.move()
        all_sprites.update()
        all_sprites.draw(screen)
        # print(level.objects)

        pygame.display.flip()
