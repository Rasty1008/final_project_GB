from abc import abstractmethod
from AnimalsABS import Animals

class PackAnimals(Animals):

    @abstractmethod
    def eat(self):
        """Прием еды"""
        pass

    @abstractmethod
    def medicines(self):
        """Прием лекарств"""
        pass

