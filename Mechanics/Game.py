import pygame
from Player import *
from Blocks import *

WIN_WIDTH = 1280
WIN_HEIGHT = 720
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "black"


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l = -target_rect.x + WIN_WIDTH / 2
    t = -target_rect.y + WIN_HEIGHT / 2

    w, h = camera.width, camera.height

    l = min(0, l)
    l = max(-(camera.width - WIN_WIDTH), l)
    t = max(-(camera.height - WIN_HEIGHT), t)
    t = min(0, t)

    return Rect(l, t, w, h)


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("CoffeMan - T H E  G A M E")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))

    bg.fill(Color(BACKGROUND_COLOR))

    hero = Player(55, 55)
    left = right = False
    up = False

    entities = pygame.sprite.Group()
    platforms = []

    entities.add(hero)

    level = [
        "--------------------------------------------------------",
        "-                                                      -",
        "-                       --                             -",
        "-                                                      -",
        "-            --                                        -",
        "-                                                      -",
        "--                                                     -",
        "-                                                      -",
        "-                   ----     ---                       -",
        "-                                                      -",
        "--                                                     -",
        "-                                                      -",
        "-                            ---                       -",
        "-                                                      -",
        "-                                                      -",
        "-      ---                                             -",
        "-                                                      -",
        "-------     ^^^>>  <<-                                 -",
        "-               -**-      --                           -",
        "-                     --  -                            -",
        "-     --                                               -",
        "-                                                      -",
        "-                                                      -",
        "--------------------------------------------------------"]

    timer = pygame.time.Clock()
    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)

            elif col == "*":
                flame = Flame(x, y)
                entities.add(flame)
                platforms.append(flame)

            elif col == ">":
                rarrow = Right_Arrow(x, y)
                entities.add(rarrow)
                platforms.append(rarrow)

            elif col == "<":
                larrow = Left_Arrow(x, y)
                entities.add(larrow)
                platforms.append(larrow)

            elif col == "^":
                trampoline = Trampoline(x, y)
                entities.add(trampoline)
                platforms.append(trampoline)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.mixer.init()
    sound = pygame.mixer.Sound('main_music.ogg')
    sound.play(-1)

    camera = Camera(camera_configure, total_level_width, total_level_height)
    running = True
    while running:
        timer.tick(60)
        if hero.dead:
            sound.stop()
            hero.sound_of_death.play()
            time.wait(4000)
            sound.play()
            hero.dead = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

        screen.blit(bg, (0, 0))

        camera.update(hero)
        hero.update(left, right, up, platforms)

        for e in entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()


if __name__ == "__main__":
    main()