import pygame
from os import access, F_OK
import json


def check_img(img, size):
    if type(img) is str:
        if access(img, F_OK):
            img = pygame.image.load(img).convert()

        else:
            print("This file was not found")

    if type(img) is not pygame.Surface:
        img = pygame.image.load("resource/no_signal.png").convert()

    return pygame.transform.scale(img, size)


def get_data():
    with open("resource/data.json") as data:
        data = json.load(data)

    return data


def set_data(data):
    if type(data) is dict:
        with open("resource/data.json", "w") as out:
            print(json.dumps(data), file=out)

    else:
        print("This is't dict")
