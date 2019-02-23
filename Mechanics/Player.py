from pygame import *
import os
from Blocks import *
from Items import *


MOVE_SPEED = 7
WIDTH = 40
HEIGHT = 40
COLOR = "blue"
JUMP_POWER = 12
GRAVITY = 0.25
ANIM_STAY = []

mixer.pre_init(44100, -16, 1, 512)
mixer.init()


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.x_speed = 0
        self.y_speed = 0

        self.startX = x
        self.startY = y

        self.num_of_coins = 0
        self.num_of_keycards = 0
        self.onGround = False
        self.dead = False
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.image.set_colorkey((0, 0, 0))
        self.image = image.load("%s/images\Player\hero.png" % ICON_DIR)

        self.frames = []

        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.sound_of_jump = mixer.Sound('Music/jump.ogg')
        self.sound_of_death = mixer.Sound('Music/game_over.ogg')
        self.sound_of_collecting_coins = mixer.Sound('Music/sound_of_coin.ogg')

    def update(self, left, right, up, platforms):

        if up:
            if self.onGround:
                self.y_speed = -JUMP_POWER
                self.image.fill((0, 0, 0))
                self.image = image.load("%s/images\Player\hero_up2.png" % ICON_DIR)
                self.sound_of_jump.play()

        if left:
            self.x_speed = -MOVE_SPEED
            self.image.fill((0, 0, 0))
            self.image = image.load("%s/images\Player\hero_left2.png" % ICON_DIR)

        if right:
            self.x_speed = MOVE_SPEED
            self.image.fill((0, 0, 0))
            self.image = image.load("%s/images\Player\hero_right2.png" % ICON_DIR)

        if not (left or right):
            self.x_speed = 0
            if not up:
                self.image.fill((0, 0, 0))
                self.image = image.load("%s/images\Player\hero.png" % ICON_DIR)
        if not self.onGround:
            self.y_speed += GRAVITY

        self.onGround = False
        self.rect.y += self.y_speed
        self.collide(0, self.y_speed, platforms)

        self.rect.x += self.x_speed
        self.collide(self.x_speed, 0, platforms)

    def respawn(self):
        self.dead = True


        self.teleporting(self.startX, self.startY)

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY

    def collide(self, x_speed, y_speed, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):

                if x_speed > 0:
                    self.rect.right = p.rect.left



                if x_speed < 0:
                    self.rect.left = p.rect.right

                if y_speed > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.y_speed = 0

                if y_speed < 0:
                    self.rect.top = p.rect.bottom
                    self.y_speed = 0

                if self.rect.bottom == p.rect.top:
                    if isinstance(p, Flame):
                        self.respawn()

                    elif isinstance(p, Right_Arrow):
                        self.x_speed += 10

                    elif isinstance(p, Left_Arrow):
                        self.x_speed -= 10

                    elif isinstance(p, Trampoline):
                        self.y_speed = -JUMP_POWER * 1.25
                        self.sound_of_jump.play()

                if isinstance(p, Door):
                    if self.num_of_keycards > 0:
                        self.num_of_keycards -= 1
                        p.image.fill(Color("green"))
                        p.rect = Rect(0, 0, 0, 0)

                elif isinstance(p, Item):
                    p.image.fill(Color("green"))
                    p.rect = Rect(0, 0, 0, 0)
                    if p.name == "coin":
                        self.num_of_coins += 1
                        self.sound_of_collecting_coins.play()
                    if p.name == "keycard":
                        self.num_of_keycards += 1
                        self.sound_of_collecting_coins.play()

