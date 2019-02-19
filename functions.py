import pygame
import json


def check_img(img):
    if type(img) is str:
        image = pygame.image.load(f"resource/menu/{img}").convert()

    else:
        image = img

    return image


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