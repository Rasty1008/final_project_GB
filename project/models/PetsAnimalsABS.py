from abc import abstractmethod
from AnimalsABS import Animals

class PetsAnimals(Animals):

    @abstractmethod
    def eat(self):
        """Прием еды"""
        pass

    @abstractmethod
    def medicines(self):
        """Прием лекарств"""
        pass