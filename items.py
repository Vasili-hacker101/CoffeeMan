import pygame

from functions import check_img
# я хз, что из себя должен представлять родительский класс итема
#поэтому просто бахнул отрисовку и проверку Павла
class Item:

    def __init__(self, surface, x, y, cell_size, image=None):
        self.surface = surface
        self.x, self.y = x, y
        self.size = cell_size
        self.img = check_img(image, (cell_size, cell_size))
        self.sprite = pygame.sprite.Sprite()

    def draw(self):
        if self.img is None:
            self.sprite.image = pygame.image.load("no_signal.jpg")
            self.sprite.rect = (self.size, self.size)
        else:
            self.sprite.image = pygame.image.load(self.img)
            self.sprite.rect = (self.size, self.size)

    def check_colis(self):
        pass

    def if_inventory(self):
        return self.size

#физика через жопу работает
#позже залью доделаный итем