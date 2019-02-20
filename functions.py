import pygame
from os import access, F_OK
import json


def check_img(img, size):
    print(size)
    if type(img) in [str, pygame.Surface]:
        if type(img) is str:
            if access(img, F_OK):
                image = pygame.image.load(img).convert()

            else:
                print("This file was not found")
                return

        else:
            image = img

        image = pygame.transform.scale(image, size)

        return image

    return


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
