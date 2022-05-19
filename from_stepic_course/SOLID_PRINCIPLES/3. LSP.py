"""
Liskov Substitution Principle
подставив наследника вместо базового, код должен продолжать работать
"""


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self.width}, height: {self.height}"


def use_it(rect: Rectangle):
    w = rect.width
    rect.height = 10
    expected_area = 10 * w


""" Если отнаследоваться от Rectangle в Square И ИЗМЕНЕНИЕМ высоты/ширины менять ОДНОВРЕМЕННО высоту и ширину
 тогда ожидаемое поведение будет отличаться - нарушение принципа Лисков
 Выход - не нужно наследование """
