from pygame import *
import os
from Player import *
#from Game import *
from functions import check_img

CELL_SIZE = 40
ICON_DIR = os.path.dirname(__file__)


class Item(sprite.Sprite):

    def __init__(self, x, y, name, img):
        sprite.Sprite.__init__(self)
        self.image = Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(Color(0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.image = image.load(f"%s/images\items\{img}" % ICON_DIR)

        self.name = name
        self.rect = Rect(x, y, CELL_SIZE, CELL_SIZE)

    #def draw(self):
    #    if self.img is None:
    #        self.sprite.image = pygame.image.load("no_signal.jpg")
    #        self.sprite.rect = (self.size, self.size)
    #    else:
    #        self.sprite.image = pygame.image.load(self.img)
    #        self.sprite.rect = (self.size, self.size)

    def update(self, hero):
        self.collide(hero)

    def collide(self, hero):
#        print(self.x, hero.x)
        if sprite.collide_rect(self, hero):
            self.image.fill(Color("black"))

    #def if_inventory(self):
    #    return self.size
