"""
Interface Segregation Principle
не предоставлять слишком много методов в интерфейс, некоторые из которых могут быть лишними
"""
from abc import abstractmethod

""" Класс Machine не удовл принципу """


class Machine:
    def print(self):
        pass

    def scan(self):
        pass

    def fax(self):
        pass


class OldFasionPrinter(Machine):
    def print(self):
        print("OK")

    def scan(self):  # not need for implement
        pass

    def fax(self):  # not need for implement
        pass


""" Правильное наследование """


class Printer:
    @abstractmethod
    def print(self):
        pass


class Scanner:
    @abstractmethod
    def scan(self):
        pass


class Photocopier(Printer, Scanner):
    def print(self):
        pass

    def scan(self):
        pass


class AbstractMFU(Printer, Scanner):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def scan(self):
        pass


class ConcreteMFU(AbstractMFU):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self):
        self.printer.print()

    def scan(self):
        self.scanner.scan()

