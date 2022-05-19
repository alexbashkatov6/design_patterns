"""
OCP - open-closed principle
object is open for extension, is closed for modification
"""
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        pass


""" Класс ProductFilter не удовлетворяет OCP + взрывной комбинаторный рост"""


class ProductFilter:
    def filter_by_color(self, products, color):
        pass

    def filter_by_size(self, products, size):
        pass

    def filter_by_color_and_size(self, products, color, size):
        pass


""" Корпоративный шаблон - Specification """
""" Классы Specification, Filter и их наследование - правильно """


class Specification:
    def is_satisfied(self, item) -> bool:
        pass

    def __and__(self, other):  # ! reload for &, not for "and"
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        pass


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        pass


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        pass


class BetterFilter(Filter):
    def filter(self, items, spec):
        pass
