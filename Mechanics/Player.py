from pygame import *
import os
from Blocks import *
MOVE_SPEED = 7
WIDTH = 40
HEIGHT = 40
COLOR = "blue"
JUMP_POWER = 12
GRAVITY = 0.25

mixer.pre_init(44100, -16, 1, 512)
mixer.init()


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.x_speed = 0
        self.y_speed = 0

        self.startX = x
        self.startY = y

        self.onGround = False
        self.dead = False
        self.image = Surface((WIDTH, HEIGHT))

        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.sound_of_jump = mixer.Sound('jump.ogg')
        self.sound_of_death = mixer.Sound('game_over.ogg')


    def update(self, left, right, up, platforms):

        if up:
            if self.onGround:
                self.y_speed = -JUMP_POWER
                self.sound_of_jump.play()

        if left:
            self.x_speed = -MOVE_SPEED

        if right:
            self.x_speed = MOVE_SPEED

        if not (left or right):
            self.x_speed = 0

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

