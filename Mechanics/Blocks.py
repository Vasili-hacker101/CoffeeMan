
from pygame import *
import os

PLATFORM_WIDTH = 40
PLATFORM_HEIGHT = 40
PLATFORM_COLOR = "green"
АRROW_COLOR = "black"
FLAME_COLOR = "red"

ICON_DIR = os.path.dirname(__file__)


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        #self.image = image.load("%s/platform.png" % ICON_DIR)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Flame(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(FLAME_COLOR))
        #self.image = image.load("%s/flame.png" % ICON_DIR)


class Right_Arrow(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("black"))
        self.image = image.load("%s/right.png" % ICON_DIR)


class Left_Arrow(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("black"))
        self.image = image.load("%s/left.png" % ICON_DIR)


class Trampoline(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("black"))
        self.image = image.load("%s/up.png" % ICON_DIR)