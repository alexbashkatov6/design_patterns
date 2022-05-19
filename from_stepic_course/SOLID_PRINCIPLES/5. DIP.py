"""
Dependency Inversion Principle
Высокий уровень не должен зависеть от деталей реализации низкого уровня
"""
from abc import abstractmethod


class Relationship:
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class Relationships:
    def __init__(self):
        """ storage as list - detail of impl ! """
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append("...")


class Research:
    def __init__(self, relationships: Relationships):
        relations = relationships.relations
        """ here uses that list """
        for r in relations:
            pass


""" Правильная реализация """


class RelationshipsBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipsBrowser):

    def __init__(self):
        pass

    def add_parent_and_child(self, parent, child):
        pass

    def find_all_children_of(self, name):
        pass


class Research:
    def __init__(self, relationships: Relationships):
        relationships.find_all_children_of("")