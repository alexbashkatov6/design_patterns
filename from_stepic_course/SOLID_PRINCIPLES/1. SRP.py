"""
Single Responsibility Principle
Антипаттерн - всемогущий объект (God object)

"""


class Journal:
    def __init__(self):
        pass

    def add_entry(self, text):
        pass

    def remove_entry(self, pos):
        pass

    def __str__(self):
        pass

    """ ! далее методы, которых здесь не должно быть ! """

    def save(self, filename):
        pass

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass


""" Нужен отдельный класс ! """


class PersistenceManager:

    @staticmethod
    def save_to_file(journal, filename):
        pass
