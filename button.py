from abc import ABC, abstractmethod


class Button(ABC):
    def __init__(self, x, y, size_x, size_y, surface, text, image=None, color="black"):
        self.x, self.y = x, y
        self.size_x = size_x
        self.size_y = size_y
        self.surface = surface
        self.img = image
        self.color = color
        self.text = text

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def pressed(self):
        pass

    def is_active(self, mouse_pos):
        x, y = mouse_pos
        return 0 <= x - self.x <= self.size_x and 0 <= y - self.y <= self.size_y
